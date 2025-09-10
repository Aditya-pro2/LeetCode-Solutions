class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double s = 0;
        for (int i = 0; i < k; i++)
            s += nums[i];
        double m = s / k;
        for (int i = 1, j = k; j < nums.size(); i++, j++)
        {
            s = s - nums[i - 1] + nums[j];
            if (m < (s / k))
                m = s / k;
        }
        return m;
    }
};