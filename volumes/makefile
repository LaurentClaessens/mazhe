####### Compiler, tools and options

CXX           = LC_ALL=C g++ -std=c++14
DEL_FILE      = rm -f

####### Implicit rules

clean: 
	-$(DEL_FILE) *.o
	-$(DEL_FILE) *~ core *.core


####### Compile
all:  volumes
volumes: volumes.h
	$(CXX) -o volumes volumes.cpp
