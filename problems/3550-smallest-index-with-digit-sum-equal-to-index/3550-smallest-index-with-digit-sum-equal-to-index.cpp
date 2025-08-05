class Solution {
    int sum(int n)
    {
        if (n < 10)
            return n;
        return (n % 10) + sum(n / 10);
    }
public:
    int smallestIndex(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++)
            if (i == sum(nums[i]))
                return i;
        return -1;
    }
};