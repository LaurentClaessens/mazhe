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
#include <vector>
#include <cstdlib>
#include <string>
#include <sstream>

// replace string 's1' by 's2' in the string 'str'
// this is in-place replacement. All the occurrences of 's1' are replaced by 's2' in 'str'
// http://stackoverflow.com/questions/3418231/replace-part-of-a-string-with-another-string
void replace( std::string &str,std::string s1,std::string s2 );

#endif // __VOLUMES_H_9066__
