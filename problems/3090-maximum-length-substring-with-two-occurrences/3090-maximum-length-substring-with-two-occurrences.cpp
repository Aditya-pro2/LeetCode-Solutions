class Solution {
public:
    int maximumLengthSubstring(string s) {
        vector<int> freq(26, 0);
        int ans = 0;
        for (int i = 0, j = 0; i < s.size() && j < s.size(); )
        {
            char c = s[j];
            if (freq[c - 'a'] + 1 > 2)
            {
                freq[s[i] - 'a']--;
                i++;
            }
            else
            {
                freq[c - 'a']++;
                ans = max(ans, j - i + 1);
                j++;
            }
        }
        return ans;
    }
};