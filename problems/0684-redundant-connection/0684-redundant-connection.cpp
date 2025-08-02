class DisjointSet
{
    public:
        int n;
        vector<int> par, rank;

        DisjointSet(int a)
        {
            n = a;
            for (int i = 0; i < n; i++)
            {
                par.push_back(i);
                rank.push_back(0);
            }
        }

        int find(int x)
        {
            if (par[x] == x)
                return x;
            return par[x] = find(par[x]);
        }

        bool unionByRank(int x, int y)
        {
            int parX = find(x), parY = find(y);
            if (parX == parY)
                return true;
            if (rank[parX] > rank[parY])
                par[parY] = parX;
            else
            {
                par[parX] = parY;
                if (rank[parX] == rank[parY])
                {
                    rank[parX]++;
                }    
            }
            return false;
        }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        DisjointSet dj(edges.size() + 1);
        for (auto i : edges)
            if (dj.unionByRank(i[0], i[1]))
                return {i[0], i[1]};
        return {};
    }
};