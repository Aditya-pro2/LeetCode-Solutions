class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int a = edges[0][0], b = edges[0][1];
        for (int i : edges[1])
            if (i == a)
                return a;
        return b;
    }
};