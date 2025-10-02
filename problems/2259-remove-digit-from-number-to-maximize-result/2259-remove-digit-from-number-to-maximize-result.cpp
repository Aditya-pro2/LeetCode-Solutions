class Solution {
public:
    string removeDigit(string number, char digit) {
        int i = 0;
        string ans = "";
        for (i = 0; i < number.size(); i++)
        {
            string temp = "";
            if (number[i] == digit)
                temp = number.substr(0, i) + number.substr(i + 1);
            ans = max(ans, temp);
        }
        return ans;
    }
};