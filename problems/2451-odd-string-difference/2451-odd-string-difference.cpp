class Solution {
public:
    string oddString(vector<string>& words) {
        const int m = words[0].size() - 1;
        vector<int> same(m, 0);
        for (int j = 0; j < m; j++)
        {
            int diff1 = words[0][j + 1] - words[0][j];
            int diff2 = words[1][j + 1] - words[1][j];
            int diff3 = words[2][j + 1] - words[2][j];
            if (diff1 != diff2 && diff1 != diff3)
                return words[0];
            if (diff2 != diff1 && diff2 != diff3)
                return words[1];
            if (diff3 != diff1 && diff3 != diff2)
                return words[2];
            same[j] = diff1;
        }
        for (int i = 3, n = words.size(); i < n; i++)
            for (int j = 0; j < m; j++)
                if (words[i][j + 1] - words[i][j] != same[j])
                    return words[i];
        return "";
    }
};