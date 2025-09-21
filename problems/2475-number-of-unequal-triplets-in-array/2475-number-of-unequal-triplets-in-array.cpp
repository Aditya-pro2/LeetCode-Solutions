class Solution {
public:
    int unequalTriplets(vector<int>& nums) {
        int trips = 0, pairs = 0, count[1001] = {};
        for (int i = 0; i < nums.size(); i++)
        {
            trips += pairs - count[nums[i]] * (i - count[nums[i]]);
            pairs += i - count[nums[i]];
            count[nums[i]] += 1;
        }
        return trips;
    }
};