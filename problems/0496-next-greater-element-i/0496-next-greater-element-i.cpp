class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& a, vector<int>& b) {
        vector<int> c;
        for (int i = 0; i < a.size(); i++)
        {
            int m = -1;
            for (int j = 0; j < b.size(); j++)
            {
                int x = j;
                if (a[i] == b[j])
                {
                    while (x != b.size())
                    {
                        if (b[x] > a[i])
                        {
                            m = b[x];
                            break;
                        }
                        x++;
                    }
                }
            }
            c.push_back(m);
        }
        return c;
    }
};