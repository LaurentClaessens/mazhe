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


#ifndef __UTILITIES_14772__
#define __UTILITIES_14772__

#include <string>
#include <iostream>
#include <fstream>
#include <sstream>


using std::string;
using std::ostringstream;
using std::istringstream;

// replace string 's1' by 's2' in the string 'str'
// this is in-place replacement.
// All the occurrences of 's1' are replaced by 's2' in 'str'
// http://stackoverflow.com/questions/3418231/replace-part-of-a-string-with-another-string
void replace( string &str,string s1,string s2 );

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

#endif // __UTILITIES_14772__   
