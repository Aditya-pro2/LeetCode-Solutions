class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int cur = nums[0];
        for (int i = 1; i < nums.size() && nums[i] == nums[i - 1] + 1; cur += nums[i++]);
        sort(nums.begin(), nums.end());
        if (!binary_search(nums.begin(), nums.end(), cur))
            return cur;
        for (auto it = upper_bound(nums.begin(), nums.end(), cur); it != nums.end(); it++)
        {
            if (*it == cur + 1)
                ++cur;
        }
        return cur + 1;
    }
};