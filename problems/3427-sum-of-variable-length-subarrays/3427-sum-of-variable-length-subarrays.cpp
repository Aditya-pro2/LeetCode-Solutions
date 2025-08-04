class Solution {
public:
    int subarraySum(vector<int>& nums) {
        int res = nums[0];
        for (int i = 1, n = nums.size(); i < n; i++){
            int j = i - nums[i] - 1;
            nums[i] += nums[i - 1];
            res += nums[i] - (j >= 0 ? nums[j] : 0);
        }
        return res;
    }
};