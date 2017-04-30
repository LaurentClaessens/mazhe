####### Compiler, tools and options

CXX           = LC_ALL=C g++ -std=c++14
DEL_FILE      = rm -f

####### Implicit rules

clean: 
	-$(DEL_FILE) *.o
	-$(DEL_FILE) *~ core *.core


####### Compile
all:  volumes
Utilities : Utilities.h Utilities.cpp
	$(CXX) -c  -o Utilities.o Utilities.cpp
volumes: Utilities volumes.h volumes.cpp
	$(CXX) -g  -o volumes Utilities.o   volumes.cpp
