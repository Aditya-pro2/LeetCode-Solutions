class Solution {
public:
    int xorBeauty(vector<int>& nums) {
        int a = 0, b = 0;
        for (int i : nums)
        {
            a |= i;
            b ^= i;
        }
        return (a & b);
    }
};