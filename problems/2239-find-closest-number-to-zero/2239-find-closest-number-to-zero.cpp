class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int m = INT_MAX, idx = 0;
        for (int i : nums)
        {
            if (m > abs(i))
            {
                m = abs(i);
                idx = i;
            }
            else if (m == abs(i) && idx < i)
                idx = i;
        }
        return idx;
    }
};