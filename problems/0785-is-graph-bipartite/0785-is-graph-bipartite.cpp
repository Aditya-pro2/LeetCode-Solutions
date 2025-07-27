class Graph
{
    int V;
    list<int>* l;

    public:
        Graph(int a)
        {
            V = a;
            l = new list<int>[V];
        }

        void addEdges(vector<vector<int>>& a)
        {
            for (int i = 0; i < a.size(); i++)
                for (int j : a[i])
                    l[i].push_back(j);
        }

        bool helper()
        {
            queue<int> q;
            vector<int> color(V, -1);
            for (int i = 0; i < V; i++)
            {
                if (color[i] != -1)
                    continue;
                q.push(i);
                color[i] = 0;
                while (q.size() > 0)
                {
                    int curr = q.front();
                    q.pop();
                    list<int> neighbours = l[curr];
                    for (int v : neighbours)
                    {
                        if (color[v] == -1)
                        {
                            color[v] = !color[curr];
                            q.push(v);
                        }
                        else if (color[v] == color[curr])
                            return false;
                    }
                }
            }
            return true;
        }
};

class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        Graph g(graph.size());
        g.addEdges(graph);
        return g.helper();
    }
};