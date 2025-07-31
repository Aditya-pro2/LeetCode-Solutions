class Solution {
public:
    class Info
    {
        public:
            int u, cost, stops;

            Info(int a, int b, int c)
            {
                u = a;
                cost = b;
                stops = c;
            }
    };

    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k)
    {
        queue<Info> q;
        vector<int> dist(n, INT_MAX);
        dist[src] = 0;
        q.push(Info(src, 0, -1));
        while (!q.empty())
        {
            Info curr = q.front();
            q.pop();
            for (auto i : flights)
            {
                if (i[0] == curr.u)
                {
                    int v = i[1], w = i[2];
                    if (dist[v] > curr.cost + w && curr.stops + 1 <= k)
                    {
                        dist[v] = curr.cost + w;
                        q.push(Info(v, dist[v], curr.stops + 1));
                    }
                }
            }
        }
        if (dist[dst] == INT_MAX)
            return -1;
        return dist[dst];
    }
};