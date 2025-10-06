class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        std::transform(paragraph.begin(), paragraph.end(), paragraph.begin(), ::tolower);
        unordered_map<string, int> freq;
        string word = "";
        for (int i = 0; i < paragraph.size(); i++)
        {
            if (paragraph[i] != ' ' && paragraph[i] != '!' && paragraph[i] != '?' && paragraph[i] != '\'' && paragraph[i] != ';' && paragraph[i] != '.' && paragraph[i] != ',')
                word += paragraph[i];
            else if (!word.empty())
            {
                freq[word]++;
                word = "";
            }
        }
        if (!word.empty())
            freq[word]++;
        string ans = "";
        int f = 0;
        for (auto itr : freq)
            if (itr.second > f && find(banned.begin(), banned.end(), itr.first) == banned.end())
            {
                ans = itr.first;
                f = itr.second;
            }
        return ans;
    }
};