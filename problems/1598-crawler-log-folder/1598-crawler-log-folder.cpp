class Solution {
public:
    int minOperations(vector<string>& logs) {
        stack<int> st;
        for (int i = 0; i < logs.size(); i++)
        {
            if (logs[i] == "../")
            {
                if (!st.empty())
                    st.pop();
            }
            else if (logs[i] == "./") {}
            else
                st.push(1);
        }
        return st.size();
    }
};