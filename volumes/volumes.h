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


#ifndef __VOLUMES_H_9066__
#define __VOLUMES_H_9066__

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <string>

using std::string;

class UnicodeCouple
{
    // Provide a couple like "\IeC {\^\i }" stands for "î".
    // You only gives what is in the bracket.
    private:
        string code;
        string replacement;
    public:
        UnicodeCouple( string c,string r );
        void perform_substitution(string &str) const;
};

// replace "\IeC {\'e}" by "é" and other such replacements.
void IeC_remove(string &line);

// return 'true' if 'line' represents a "chapter" line.
bool isChapterLine(const string& line);


class Chapter{
    /*
    We parse a line like :
    \contentsline {chapter}{\numberline {30}Exemples avec Sage}{1284}{chapter.30}
    or :
    \contentsline {chapter}{Index}{7}{chapter*.1}
    There can be braces in the chapter title. 
    */
    public:
        Chapter(const string& line);
        int getPage() const;
        string getName() const;
    private :
        string name;
        int page;
};

// Create the LaTeX file of the front page from the one of 'filename'
// and the volume number 'voln' 
// It just change "CHANGE HERE" to the volume number in 'gardeVolume.tex'
// return the name of the created file.
string create_front_page(int voln);

class LatexDocument{
    // Describe a LaTeX document. One has to provide coherent pdf filename
    // and a toc filename that are produced by LaTeX.
    private :
        string pdf_filename;
        std::vector<Chapter> chapter_list;

    public :
        LatexDocument(string pdf, string toc);
        
        // return the starting page of the chapter 'chap_name'
        int titleToPage(string chap_name) const;

        // create a pdf file 'output' containing the chapters from
        // 'Ichap' to 'Fchap' (the latter is not included).
        void extractFromTo(const string Ichap,
            const string Fchap,const string output) const;

        // create a pdf file from the 'Liste des notations' up to the end
        void extractListOfNotations(string filename) const;
    
        void divide(std::vector<string> sc_list) const;
};
   

#endif // __VOLUMES_H_9066__
