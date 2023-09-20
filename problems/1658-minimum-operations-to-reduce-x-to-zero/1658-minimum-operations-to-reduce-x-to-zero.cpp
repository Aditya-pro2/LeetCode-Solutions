class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int n = nums.size();
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int low=0, high=0, window_sum=0, ans = INT_MAX, target=sum-x;
        if(target < 0)
            return -1;

        while(high<n){
            window_sum += nums[high];
            while(window_sum > target)
                window_sum -= nums[low++];

            if(window_sum == target)
                ans = min(ans, n-(high-low+1));

            high++;
        }

        return ans == INT_MAX ? -1 : ans;
    }
};