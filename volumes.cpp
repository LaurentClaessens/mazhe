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
        cout<<"replacer|"<<code<<"| par "<<replacement<<endl;
        replace(str,code,replacement);
    };
};

// replace "\IeC {\'e}" by "é" and other such replacements.
void IeC_remove(string &line){
    IeC_couple icirconflex("\\^\\i ","î");
    IeC_couple eaccute("\\'e","é");
    vector<IeC_couple> change_list(2)
    change_list.push_back(icirconflex)
    change_list.push_back(eaccute)


    eaccute.perform_substitution(line);
    cout<<line<<endl;


};

int main ()
{
    ifstream tocfile("test.toc");
    string line;
    getline(tocfile,line);
    tocfile.close();

    
    cout<<line<<endl;
    IeC_remove(line);
    cout<<"le résultat final est "<<endl<< line<<endl;
};
