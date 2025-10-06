class Solution {
public:
    bool isGood(vector<int>& nums) {
        int sz = size(nums);
        for (int i = 0; i < sz;)
        {
            if (nums[i] >= sz)
                return false;
            int pos = nums[i] - 1;
            if (nums[pos] == nums[i])
                i++;
            else
                swap(nums[pos], nums[i]);
        }
        for (int i = 0; i < sz; i++)
            if (nums[i] != i + 1 && i != sz - 1)
                return false;
        return sz >= 2 && nums.back() == sz - 1 && nums[sz - 2] == sz - 1;
    }
};