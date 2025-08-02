class DSU {
    vector<int> size, parent;

public:
    DSU(int n)
    {
        size.resize(n + 1, 1);
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int u)
    {
        if (parent[u] == u)
            return u;
        return parent[u] = find(parent[u]);
    }
    void unionBySize(int u, int v)
    {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u == root_v)
            return;
        if (size[root_u] < size[root_v]) {
            parent[root_u] = root_v;
            size[root_v] += size[root_u];
        }
        else
        {
            parent[root_v] = root_u;
            size[root_u] += size[root_v];
        }
    }
};

class Solution {
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<int> parent(n + 1, 0);
        vector<int> candidate1, candidate2;
        for (auto& e : edges)
        {
            int u = e[0], v = e[1];
            if (parent[v] == 0)
                parent[v] = u;
            else
            {
                candidate1 = {parent[v], v};
                candidate2 = {u, v};
                e[1] = 0;
            }
        }
        DSU ds(n + 1);
        for (auto& e : edges)
        {
            int u = e[0], v = e[1];
            if (v == 0)
                continue;
            if (ds.find(u) == ds.find(v))
            {
                if (candidate1.empty())
                    return {u, v};
                return candidate1;
            }
            else
                ds.unionBySize(u, v);
        }
        return candidate2;
    }
};