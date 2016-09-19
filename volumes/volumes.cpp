/*
Copyright 2015-2016 Laurent Claessens
contact : moky.math@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
//*/


#include <iostream>
#include <fstream>
#include <sstream>

#include "volumes.h"
#include "Utilities.h"

using std::string;
using std::ifstream;
using std::ofstream;


UnicodeCouple::UnicodeCouple( string c,string r )
{
    code="\\IeC {"+c+"}";
    replacement=r;
};
void UnicodeCouple::perform_substitution(string &str) const
{
    replace(str,code,replacement);
};

void IeC_remove(string &line){
    std::vector<UnicodeCouple> change_list;
    change_list.push_back(UnicodeCouple("\\^\\i ","î") );
    change_list.push_back(UnicodeCouple("\\'e","é"));
    change_list.push_back(UnicodeCouple("\\^e","ê"));
    change_list.push_back(UnicodeCouple("\\^o","ô"));
    change_list.push_back(UnicodeCouple("\\\"o","ö"));
    change_list.push_back(UnicodeCouple("\\\"u","ü"));
    change_list.push_back(UnicodeCouple("\\`e","è")  );
    change_list.push_back(UnicodeCouple("\\`A","Á")  );
    change_list.push_back(UnicodeCouple("\\`u","ù")  );
    change_list.push_back(UnicodeCouple("\\`a","à")  );
    change_list.push_back(UnicodeCouple("\\'E","É")  );

    for (int i=0;i!=change_list.size();i++){
        change_list[i].perform_substitution(line);
    };
}

bool isChapterLine(const string& line){
    string chapter_mark="\\contentsline {chapter}";
    int is=chapter_mark.size();
    string deb(line,0,is);
    if (deb==chapter_mark){return true;}
    return false;
}

Chapter::Chapter(const string& line)
{
    string a1=line;
    replace(a1,"\\contentsline {chapter}{","");
    size_t initpos=0;
    if(a1[0]==*"\\"){ initpos=a1.find("}")+1 ;};
    a1.replace(0,initpos,"");

    size_t lbrace=a1.rfind("{");
    size_t cbrace=a1.rfind("{",lbrace-1);

    string spage=a1.substr(cbrace+1,lbrace-cbrace-2);
    page=atoi(spage.c_str());

    name= a1.substr(0,cbrace-1);
};

string Chapter::getName() const { return name; }
int Chapter::getPage() const { return page; }

string create_front_page(int voln){
    ifstream gardeVolume("gardeVolume.tex");
    string svol=NumberToString(voln);
    string output_filename="vol-garde"+svol+".tex";
    ofstream garde(output_filename.c_str());
    string line;

    while(!gardeVolume.eof()){
        getline(gardeVolume,line);
        replace(line,"CHANGE HERE",svol);
        garde<<line<<std::endl;
     };
    string command="pdflatex "+output_filename;
    std::cout<<command<<std::endl;
    system(command.c_str());
    replace(output_filename,".tex",".pdf");
    return output_filename;
}

LatexDocument::LatexDocument(string pdf, string toc) :
    pdf_filename(pdf)
{
    ifstream tocfile(toc.c_str());
    string line;

    while(!tocfile.eof()){
        getline(tocfile,line);
        if (isChapterLine(line)){
            IeC_remove(line);
            chapter_list.push_back(Chapter(line));
        };
    };
    tocfile.close();
};

int LatexDocument::titleToPage(string chap_name) const
{
    bool found=false;
    for (int i=0; !found and i<chapter_list.size() ;i++){
        Chapter chap=chapter_list[i];
        if (chap.getName()==chap_name){
            return chap.getPage();
        }
    }
    string s="Woops. Chapter '"+chap_name+"' not found";
    throw  s;
}

void LatexDocument::extractFromTo(string Ichap,string Fchap,string output) const
{
    bool If=false;
    bool Ff=false;
    int Ipage=0;
    int Fpage=0;
    for (int i=0; (!If or !Ff) and i<chapter_list.size() ;i++){
        Chapter chap=chapter_list[i];
        if (chap.getName()==Ichap){
            Ipage=chap.getPage();
            If=true;
        }
        if (chap.getName()==Fchap){
            Fpage=chap.getPage()-1;
            Ff=true;
        }
    }
    if (!If) { 
        string s="Woops. Chapter '"+Ichap+"' not found";
        throw  s;
    }
    if (!Ff) { 
        string s="Woops. Chapter '"+Fchap+"' not found";
        throw  s;
    }
    string sIpage=NumberToString(Ipage);
    string sFpage=NumberToString(Fpage);
    string command="pdftk "+pdf_filename+" cat "+sIpage+"-"+sFpage+" output "+output;
    std::cout<<command<<std::endl;
    system(command.c_str());
};

void LatexDocument::extractListOfNotations(string filename) const
{
    int init_page=titleToPage("Liste des notations");
    string spage=NumberToString(init_page);
    string command="pdftk "+pdf_filename+" cat "+spage+"-end"+" output "+filename;
    std::cout<<command<<std::endl;
    system(command.c_str());
}

void LatexDocument::divide(std::vector<string> sc_list) const
{
    extractFromTo("Table des matières","Introduction","vol-toc.pdf");
    extractListOfNotations("vol-ton.pdf");
    
    // Creating the pdf containing the math and the pdf containing the front page
    for (int i=0;i<sc_list.size()-1;i++){
        string mat_filename="vol-mat"+NumberToString(i+1)+".pdf";
        try{
            extractFromTo(sc_list[i],sc_list[i+1],mat_filename);
        }
        catch (string s){
            std::cout<<s<<std::endl;
        }
        string front_filename=::create_front_page(i+1);

        // merging the whole
        string command="pdftk "+front_filename+" vol-toc.pdf"+" "+mat_filename+" vol-ton.pdf"+" cat output lefrido-volume"+NumberToString(i+1)+".pdf";
        std::cout<<command<<std::endl;
        system(command.c_str());
    }

}
    
int main ()
{
    std::vector<string> starting_chapters;
    starting_chapters.push_back("Introduction");
    starting_chapters.push_back("Analyse réelle");
    starting_chapters.push_back("Variables aléatoires et théorie des probabilités");
    starting_chapters.push_back("Liste des notations");
    LatexDocument frido_book("0-book.pdf","Inter_frido-mazhe_pytex.toc");

    frido_book.divide(starting_chapters);
}
