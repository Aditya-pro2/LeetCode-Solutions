class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        long long int mn = INT_MIN;
        long long int mid, ans, mx = 0, sum;
        int tmp;
        for (auto &i : nums)
        {
            mx += i;               // Max possible sum of subarray
            mn = max(mn, i * 1LL); // Max of minimum possible sum of subarray
        }
        while (mn <= mx)
        {
            mid = (mx - mn) / 2 + mn;
            tmp = 1, sum = 0;
            for (auto &i : nums)
            {
                sum += i;
                if (sum > mid)
                {
                    tmp++;
                    sum = i;
                }
            }
            if (tmp == k)
            {
                ans = mid;
                mx = mid - 1;
            }
            else if (tmp > k)
            {
                mn = mid + 1;
            }
            else
            {
                ans = mid;
                mx = mid - 1;
            }
        }
        return ans;
    }
};