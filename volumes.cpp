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
using namespace std;


// replace string 's1' by 's2' in the string 'str'
// this is in-place replacement. All the occurences of 's1' are replaced by 's2' in 'str'
// http://stackoverflow.com/questions/3418231/replace-part-of-a-string-with-another-string
void replace( string &str,string s1,string s2 ){
    size_t position=str.find(s1);
    while( position != string::npos ){
        str.replace(  position,s1.length(),s2 );
        position=str.find(s1);
    };
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
    // create a pdf file 'output' containing the chapters from 'Ichap' to 'Fchap' (the latter is not included).
    void extract_from_to(string Ichap,string Fchap,string output){
        bool If=false;
        bool Ff=false;
        int Ipage=0;
        int Fpage=0;
        for (int i=0; !If or !Ff ;i++){
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
        cout<<Ipage<<" "<<Fpage<<endl;
        string command="";
        command<<"pdftk "<<pdf_filename<<" cat ";
        cout<<command<<endl;
    };
};

int main ()
{
    latex_document frido("0-lefrido.pdf","Inter_frido-mazhe_pytex.toc");
    frido.extract_from_to("Retour sur les groupes","Chaînes de Markov à temps discret","mat2.pdf");
}
