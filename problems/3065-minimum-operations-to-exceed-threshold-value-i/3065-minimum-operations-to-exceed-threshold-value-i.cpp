class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int c = 0;
        for (auto i : nums)
        {
            if (i < k)
                c++;
        }
        return c;
    }
};