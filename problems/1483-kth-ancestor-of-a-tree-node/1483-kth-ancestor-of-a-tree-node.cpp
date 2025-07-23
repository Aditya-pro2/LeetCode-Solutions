class TreeAncestor {
public:
    int LOG;
    vector<vector<int>> up;

    TreeAncestor(int n, vector<int>& parent) {
        LOG = 1;
        while ((1 << LOG) <= n)
            LOG++;
        up.assign(LOG, vector<int>(n, -1));
        for (int v = 0; v < n; v++)
            up[0][v] = parent[v];
        for (int j = 1; j < LOG; j++)
        {
            for (int v = 0; v < n; v++)
            {
                int mid = up[j-1][v];
                up[j][v] = (mid == -1 ? -1 : up[j-1][mid]);
            }
        }
    }
    
    int getKthAncestor(int node, int k) {
        for (int j = 0; j < LOG && node != -1; j++)
            if (k & (1 << j))
                node = up[j][node];
        return node;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */