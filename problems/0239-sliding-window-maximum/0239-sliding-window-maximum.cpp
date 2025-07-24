class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        priority_queue<pair<int, int>> p;
        for (int i = 0; i < k; i++)
            p.push(make_pair(nums[i], i));
        ans.push_back(p.top().first);
        for (int i = k; i < nums.size(); i++)
        {
            while (!p.empty() && p.top().second <= (i - k))
                p.pop();
            p.push(make_pair(nums[i], i));
            ans.push_back(p.top().first);
        }
        return ans;
    }
};