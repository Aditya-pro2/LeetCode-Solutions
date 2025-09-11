class Solution {
    bool isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
               ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U';
    }

public:
    string sortVowels(string s)
    {
        int freq[128] = {0};
        for (char ch : s)
            if (isVowel(ch))
                freq[(int)ch]++;
        int idx = 0;
        for (int i = 0; i < (int)s.size(); i++)
        {
            if (isVowel(s[i]))
            {
                while (idx < 128 && freq[idx] == 0)
                    ++idx;
                s[i] = (char)idx;
                freq[idx]--;
            }
        }
        return s;
    }
};