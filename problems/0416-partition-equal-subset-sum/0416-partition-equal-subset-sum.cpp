class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int s = 0;
        for (int i : nums)
            s += i;
        int n = nums.size(), W = s / 2;
        vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= W; j++)
            {
                if (nums[i - 1] <= j)
                    dp[i][j] = max(nums[i - 1] + dp[i - 1][j - nums[i - 1]], dp[i - 1][j]);
                else
                    dp[i][j] = dp[i - 1][j];
            }
        return 2 * dp[n][W] == s;
    }
};