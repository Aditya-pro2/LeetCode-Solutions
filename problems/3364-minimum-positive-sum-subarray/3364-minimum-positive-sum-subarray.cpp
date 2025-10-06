class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size(), m = INT_MAX;
        vector<int> p(n + 1, 0);
        for (int i = 0; i < n; i++)
            p[i + 1] = p[i] + nums[i];
        bool x = false;
        for (int k = l; k <= r; k++)
            for (int i = 0; i + k <= n; i++)
            {
                int s = p[i + k] - p[i];
                if (s > 0)
                {
                    m = min(m, s);
                    x = true;
                }
            }
        return x ? m : -1;
    }
};