/*  Data Structure: Arrays and Strings
 * 
 * 	Implement an algorithm to determine if a string has all unique chracters
 *  Additionally: Implement this without using additional data structures or memory space.
 *		-- basic use for arrays and strings 
 *		-- brute force : O(n^2) complexity and O(1) space complexity
 * 
 *  Notes: 
 * 		consider ASCII for this problem. 
 *		UNICODE will increase the size of storage from char (1 byte) to int (4 bytes)
 *

 *  If we can't use additional data structure then compare every char of the 
 *  string with every other char, and the time complexity is O(n^s) and O(1) space.
 *
 *
 *	If we are allowed to modify the input string then we could sort the string
 *  in O(n log n) time and then check linearly for neighboring chars are identical.
 * 
 *  The time complexity for this code is O(n) (one which stores a bitmask), where
 *  n is the length of the string. The space complexity is O(1).
 *  
 *  The time complexity can also be thought of O(1) , since the for loop will 
 *  never iterate through more than 128 characters. 
 * 
 * 	Time complexity : O( Min(C, N) )
 *  Space complexity : O(C) 
 * 		where C is the size of the character set and N is the length of string
 *
 */

#include <iostream>
#include <string>
using namespace std;


// O(n2) worst case, but without using any additional memory
bool isUniqueChars (string str) {

	if (str.size() > 128) 
		return false;

	// looping and figure out 
	for (int i = 0; i < str.size(); i++) {
		for (int j = i+1; j < str.size(); j++) {
			if (str[i] == str[j]) {
				//cout << str << ":does not have unique chars" << endl;
				return false;
			}
		}
	}
	//cout << str << ":does have unique chars" << endl;
	return true;
}

// use a bitmask to store the characters
/* Bitmask will not be an optimized solution for a UNICODE use case, where there
 * are 2^32 possibilities and the bitmask (space requirements) will be a 
 * constraint. Using a hash or dictionary to store known chars will be optimized.
 */
bool isUniqueChars_Ver2 (string str) {
	if (str.size() > 128) 
		return false;

	//assumign ascii chars only
	char *charset = new char[128/8];	//one bit to store a char value
	for (int i = 0; i < str.size(); i++) {

		char c = str[i];
		if (charset[c/8] & (0x1 << (c%8))) {
			//cout << "non unique char " << c << endl;
			delete [] charset;
			return false;
		}
		else {
			charset[c/8] |= (0x1 << (c%8));
		}
	}

	delete [] charset;
	return true;
}

int 
main (int argc, char **argv) {
	//cout << "Program: isUnique" << endl << endl;

	if (argc != 2) {
		cout << "Error: Incorrect number of arguments." << endl;
	}

	std::string str(argv[1]);
	//if (isUniqueChars(str) == true) {
	if (isUniqueChars_Ver2(str) == true) {
		cout << str << ": has all unique chars" << endl;
	} 
	else {
		cout << str << ": does not have all unique chars" << endl;
	}
    return 0;
}

