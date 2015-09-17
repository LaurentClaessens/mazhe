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
};

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
};

bool is_chapter_line(string line){
        string chapter_mark="\\contentsline {chapter}{\\numberline {";
        int is=chapter_mark.size();
        string deb(line,0,is);
        if (deb==chapter_mark){return true;}
        return false;
};

// We parse a line like that :
// \contentsline {chapter}{\numberline {30}Exemples avec Sage}{1284}{chapter.30}
// There can be braces in the chapter title. 
class chapter{
    public:
        string name;
        int page;

    chapter(string line){
        size_t lbrace=line.rfind("{");
        size_t cbrace=line.rfind("{",lbrace-1);
        string spage=line.substr(cbrace+1,lbrace-cbrace-2);
        page=atoi(spage.c_str());
        size_t fbrace=line.find("}");
        size_t init=line.find("}",fbrace+1)+1;
        name= line.substr(init,cbrace-init-1);
    };
};

int main ()
{
    ifstream tocfile("test.toc");
    string line;

    while(!tocfile.eof()){
        getline(tocfile,line);
        if (is_chapter_line(line)){
            IeC_remove(line);
            cout<<line<<endl;
            chapter c=chapter(line);
            cout<<c.page<<endl;
            cout<<c.name<<endl;
        };
    };
    tocfile.close();
};
