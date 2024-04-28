// link: https://leetcode.com/problems/minimum-array-end/


// Brute Force
class Solution {
public:
    long long minEnd(int n, int x) {
        long long cur = x;
        for (int i=0; i<n-1; i++)
            cur = (cur + 1) | x;

        return cur;
    }
};

// Fill in 0 bits

class Solution {
public:
    long long minEnd(int n, int x) {
        int bits = n-1;
        long long result = x;
        int e = 0;
        while (bits > 0) {
            int bit = bits & 1;
            if (((1LL << e) & x) == 0) {
                if (bit)
                    result |= 1LL << e; // 1LL: long long (1)
                bits >>= 1;
            }
            e += 1;
        }
        return result;
    }
};
