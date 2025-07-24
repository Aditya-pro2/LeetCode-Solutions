class Solution {
public:
    class Row
    {
        public:
            int count, idx;

            Row(int a, int b)
            {
                count = a;
                idx = b;
            }

            bool operator < (const Row &obj) const
            {
                if (this->count == obj.count)
                    return this->idx > obj.idx;
                return this->count > obj.count;
            }
    };

    vector<int> kWeakestRows(vector<vector<int>>& mat, int k)
    {
        vector<Row> rows;
        vector<int> ans;
        for (int i = 0; i < mat.size(); i++)
        {
            int c = 0;
            for (int j = 0; j < mat[i].size() && mat[i][j] == 1; j++)
                c++;
            rows.push_back(Row(c, i));
        }
        priority_queue<Row> p(rows.begin(), rows.end());
        for (int i = 0; i < k; i++)
        {
            ans.push_back(p.top().idx);
            p.pop();
        }
        return ans;
    }
};