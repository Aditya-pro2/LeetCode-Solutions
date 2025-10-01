class Solution {
public:
    int minMaxGame(vector<int>& nums) {
        while (nums.size() > 1)
        {
            for (int i = 0; i < nums.size() / 2; i++)
            {
                if (i & 1)
                    nums[i] = max(nums[2 * i], nums[(2 * i) + 1]);
                else
                    nums[i] = min(nums[2 * i], nums[(2 * i) + 1]);
            }
            nums.resize(nums.size() / 2);
        }
        return nums[0];
    }
};