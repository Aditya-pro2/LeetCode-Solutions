class Solution {
public:
    class Car
    {
        public:
            int idx, distSq;

            Car(int a, int b)
            {
                idx = a;
                distSq = b;
            }

            bool operator < (const Car &obj) const
            {
                return this->distSq > obj.distSq;
            }
    };

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k)
    {
        vector<Car> v;
        vector<vector<int>> ans;
        for (int i = 0; i < points.size(); i++)
        {
            int d = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1]);
            v.push_back(Car(i, d));
        }
        priority_queue<Car> p(v.begin(), v.end());
        for (int i = 0; i < k; i++)
        {
            ans.push_back(points[p.top().idx]);
            p.pop();
        }
        return ans;
    }
};