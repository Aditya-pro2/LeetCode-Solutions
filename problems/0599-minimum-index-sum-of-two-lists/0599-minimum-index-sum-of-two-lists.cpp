class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        int n = list1.size(), m = list2.size();
        unordered_map<string, int> map;
        for (int i = 0; i < n; i++)
            map[list1[i]] = i;
        vector<string> ans;
        int min = INT_MAX;
        for (int i = 0; i < m; i++)
        {
            const string& w = list2[i];
            if (map.find(w) == map.end())
                continue;
            int sum = i + map[w];
            if (sum < min)
            {
                ans = {w};
                min = sum;
            }
            else if (sum == min)
                ans.push_back(w);
        }
        return ans;
    }
};