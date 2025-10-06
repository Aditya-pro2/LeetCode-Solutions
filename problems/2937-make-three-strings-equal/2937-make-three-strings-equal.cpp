class Solution {
public:
    int findMinimumOperations(string s1, string s2, string s3) {
        int i = 0, j = 0, k = 0;
        int a = s1.size(), b = s2.size(), c = s3.size();
        for (; i < a && j < b && k < c; i++, j++, k++)
        {
            if (s1[i] == s2[j] && s2[j] == s3[k])
                continue;
            else
                break;
        }
        return i == 0 ? -1 : (a + b + c) - (i + j + k);
    }
};