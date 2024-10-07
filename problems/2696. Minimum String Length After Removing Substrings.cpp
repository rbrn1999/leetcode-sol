// link: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

// Modify In Place
#include<map>
#include <string>
using std::string;

class Solution {
public:
    int minLength(string s) {
        int writePtr = 0;
        std::map<char, char> charMap;
        charMap['B'] = 'A';
        charMap['D'] = 'C';

        for (int readPtr=0; readPtr < s.length(); readPtr++) {
            s[writePtr] = s[readPtr];

            if (writePtr > 0 &&
             charMap.find(s[writePtr]) != charMap.end() &&
             s[writePtr-1] == charMap[s[writePtr]]) {
                writePtr--;
             } else {
                writePtr++;
             }
        }
        return writePtr;
    }
};
