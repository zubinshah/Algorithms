CC = cc
GXX = gcc
CFLAGS = -I


# 1. add the target name to ALLTARGETS
# 2. define the rules for the target 
# 3. add a smoketest for this target test_isUnique




## adding a new programming exercise, append the module name 
ALLTARGETS = isUnique isStrPermu


### isUnique 
isUnique: isUnique.o
	g++ isUnique.cpp -o isUnique

### isStrPermu
isStrPermu: isStrPermutation.o
	$(CXX) isStrPermutation.cpp -o isStrPermu

.PHONY: all clean smoketest sanity
all: $(ALLTARGETS)

clean:
	rm -fr $(ALLTARGETS)
	rm -fr *.o *.temp *.tmp

smoketest:
	@python ./smoketest.py
