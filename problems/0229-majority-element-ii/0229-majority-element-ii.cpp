class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int, int> m;
        vector<int> ans;
        for (int i : nums)
        {
            if (m.count(i))
                m[i]++;
            else
                m[i] = 1;
        }
        for (auto i : m)
        {
            if (i.second > nums.size() / 3)
                ans.push_back(i.first);
        }
        return ans;
    }
};