class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int, int> c, f;
        int ans = 0, d = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (f.count(nums[i]) == 0)
                f[nums[i]] = i;
            if (++c[nums[i]] > d) {
                d = c[nums[i]];
                ans = i - f[nums[i]] + 1;
            } else if (c[nums[i]] == d)
                ans = min(ans, i - f[nums[i]] + 1);
        }
        return ans;
    }
};