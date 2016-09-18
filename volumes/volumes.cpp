/*
Copyright 2015 Laurent Claessens
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
#include <vector>
#include <cstdlib>
#include <string>
#include <sstream>
using namespace std;


// replace string 's1' by 's2' in the string 'str'
// this is in-place replacement. All the occurrences of 's1' are replaced by 's2' in 'str'
// http://stackoverflow.com/questions/3418231/replace-part-of-a-string-with-another-string
void replace( string &str,string s1,string s2 ){
    size_t position=str.find(s1);
    while( position != string::npos ){
        str.replace(  position,s1.length(),s2 );
        position=str.find(s1);
    };
}

template <typename T>
string NumberToString(T number)
{
    ostringstream ss;
    ss<<number;
    return ss.str();
}


template <typename T>
string StringToNumber(const string &text)
{
    istringstream ss(text);
    T result;
    return ss>>result;
}


// Provide a couple like "\IeC {\^\i }" stands for "î".
// You only gives what is in the bracket.
class IeC_couple{
    public:
        string code;
        string replacement;
    IeC_couple( string c,string r ){
        code="\\IeC {"+c+"}";
        replacement=r;
    };
    void perform_substitution(string &str){
        replace(str,code,replacement);
    };
};

// replace "\IeC {\'e}" by "é" and other such replacements.
void IeC_remove(string &line){
    vector<IeC_couple> change_list;
    change_list.push_back(IeC_couple("\\^\\i ","î") );
    change_list.push_back(IeC_couple("\\'e","é"));
    change_list.push_back(IeC_couple("\\^e","ê"));
    change_list.push_back(IeC_couple("\\^o","ô"));
    change_list.push_back(IeC_couple("\\\"o","ö"));
    change_list.push_back(IeC_couple("\\\"u","ü"));
    change_list.push_back(IeC_couple("\\`e","è")  );
    change_list.push_back(IeC_couple("\\`A","Á")  );
    change_list.push_back(IeC_couple("\\`u","ù")  );
    change_list.push_back(IeC_couple("\\`a","à")  );
    change_list.push_back(IeC_couple("\\'E","É")  );

    for (int i=0;i!=change_list.size();i++){
        change_list[i].perform_substitution(line);
    };
}

bool is_chapter_line(string line){
        string chapter_mark="\\contentsline {chapter}";
        int is=chapter_mark.size();
        string deb(line,0,is);
        if (deb==chapter_mark){return true;}
        return false;
}

// We parse a line like that :
// \contentsline {chapter}{\numberline {30}Exemples avec Sage}{1284}{chapter.30}
// or :
// \contentsline {chapter}{Index}{7}{chapter*.1}
// There can be braces in the chapter title. 
class chapter{
    public:
        string name;
        int page;

    chapter(string line){
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
};

// Create the LaTeX file of the front page from the one of 'filename' and the volume number 'voln'
// It just change "CHANGE HERE" to the volume number in 'gardeVolume.tex'
// return the name of the created file.
string create_front_page(int voln){
    ifstream gardeVolume("gardeVolume.tex");
    string svol=NumberToString(voln);
    string output_filename="vol-garde"+svol+".tex";
    ofstream garde(output_filename.c_str());
    string line;

    while(!gardeVolume.eof()){
        getline(gardeVolume,line);
        replace(line,"CHANGE HERE",svol);
        garde<<line<<endl;
     };
    string command="pdflatex "+output_filename;
    cout<<command<<endl;
    system(command.c_str());
    replace(output_filename,".tex",".pdf");
    return output_filename;
}

// Describe a LaTeX document. One has to provide coherent pdf filename and a tof filename that are produced by LaTeX.
class latex_document{
    public:
        string pdf_filename;
        vector<chapter> chapter_list;

    latex_document(string pdf, string toc){
        pdf_filename=pdf;

        ifstream tocfile(toc.c_str());
        string line;

        while(!tocfile.eof()){
            getline(tocfile,line);
            if (is_chapter_line(line)){
                IeC_remove(line);
                chapter_list.push_back(chapter(line));
            };
        };
        tocfile.close();
    }

    // return the starting page of the chapter 'chap_name'
    int title_to_page(string chap_name){
        bool found=false;
        for (int i=0; !found and i<chapter_list.size() ;i++){
            chapter chap=chapter_list[i];
            if (chap.name==chap_name){
                return chap.page;
            }
        }
        string s="Woops. Chapter '"+chap_name+"' not found";
        throw  s;
    }

    // create a pdf file 'output' containing the chapters from 'Ichap' to 'Fchap' (the latter is not included).
    void extract_from_to(string Ichap,string Fchap,string output){
        bool If=false;
        bool Ff=false;
        int Ipage=0;
        int Fpage=0;
        for (int i=0; (!If or !Ff) and i<chapter_list.size() ;i++){
            chapter chap=chapter_list[i];
            if (chap.name==Ichap){
                Ipage=chap.page;
                If=true;
            }
            if (chap.name==Fchap){
                Fpage=chap.page-1;
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
        cout<<command<<endl;
        system(command.c_str());
    };
    //
    // create a pdf file from the 'Liste des notations' up to the end
    void extract_list_of_notations(string filename){
        int init_page=title_to_page("Liste des notations");
        string spage=NumberToString(init_page);
        string command="pdftk "+pdf_filename+" cat "+spage+"-end"+" output "+filename;
        cout<<command<<endl;
        system(command.c_str());
    }
    void divide(vector<string> sc_list){

        extract_from_to("Table des matières","Introduction","vol-toc.pdf");

        extract_list_of_notations("vol-ton.pdf");
    
        // Creating the pdf containing the math and the pdf containing the front page
        for (int i=0;i<sc_list.size()-1;i++){
            string mat_filename="vol-mat"+NumberToString(i+1)+".pdf";
            try{
                extract_from_to(sc_list[i],sc_list[i+1],mat_filename);
            }
            catch (string s){
                cout<<s<<endl;
            }
            string front_filename=::create_front_page(i+1);

            // merging the whole
            string command="pdftk "+front_filename+" vol-toc.pdf"+" "+mat_filename+" vol-ton.pdf"+" cat output lefrido-volume"+NumberToString(i+1)+".pdf";
            cout<<command<<endl;
            system(command.c_str());
        }

    }
};
    
int main ()
{
    vector<string> starting_chapters;
    starting_chapters.push_back("Introduction");
    starting_chapters.push_back("Analyse réelle");
    starting_chapters.push_back("Variables aléatoires et théorie des probabilités");
    starting_chapters.push_back("Liste des notations");
    latex_document frido("0-lefrido.pdf","Inter_frido-mazhe_pytex.toc");

    frido.divide(starting_chapters);
}
