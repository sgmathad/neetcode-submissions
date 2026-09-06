class Solution {
public:
    int scoreOfString(string s) {
       int total = 0;
       for(int j = 1; j < s.length(); j++)
       {
         total += abs(s[j] - s[j - 1]);
       } 

       return total;
    }
};