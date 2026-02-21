#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    string sortString(string s) {
        vector<int> freq(26,0);
        for (char c : s) {
            freq[c - 'a']++;
        }
        string result = "";
        int n = s.size();
        while (result.size() < n) {
            for (int i = 0; i < 26; i++) {
                if (freq[i] > 0) {
                    result += (char)('a' + i);
                    freq[i]--;
                }
            }
            for (int i =25; i >= 0; i--) {
                if (freq[i] > 0) {
                    result += (char)('a' + i);
                    freq[i]--;
                }
            }
        }
        return result;
    }
};