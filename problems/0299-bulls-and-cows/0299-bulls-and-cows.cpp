class Solution {
public:
    string getHint(string secret, string guess) {
        int n = secret.size(), x = 0, y = 0;
        unordered_map<char, int> m;
        for (char ch : secret)
            m[ch]++;
        for (int i = 0; i < n; i++)
            if (secret[i] == guess[i])
            {
                x++;
                m[secret[i]]--;
            }
        for (int i = 0; i < n; i++)
            if (m[guess[i]] > 0 && secret[i] != guess[i])
            {
                y++;
                m[guess[i]]--;
            }
        return to_string(x) + "A" + to_string(y) + "B";
    }
};