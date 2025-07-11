class Solution {
public:
    int firstUniqChar(string s) {
        queue<int> q;
        int freq[26] = {0};
        for (int i = 0; i < s.size(); i++)
        {
            int idx = s[i] - 'a';
            q.push(i);
            freq[idx]++;
            while ((!q.empty()) && freq[s[q.front()] - 'a'] > 1)
                q.pop();
        }
        return q.empty() ? -1 : q.front();
    }
};