class Solution {
public:
    int minimumDifference(vector<int>& nums) {
        int n = nums.size() / 2;
        vector<int> left(nums.begin(), nums.begin()+n);
        vector<int> right(nums.begin()+n, nums.end());
        int total = accumulate(nums.begin(), nums.end(), 0);
        auto getSums = [&](vector<int> &arr) {
            int m = arr.size();
            vector<vector<int>> sums(m+1);
            for(int mask = 0; mask < (1<<m); mask++) {
                int sum = 0;
                int count = 0;
                for(int i = 0; i < m; i++) {
                    if(mask & (1<<i)) {
                        sum += arr[i];
                        count++;
                    }
                }
                sums[count].push_back(sum);
            }
            for(auto &v: sums) {
                sort(v.begin(), v.end());
            }
            return sums;
        };
        vector<vector<int>> sumsLeft = getSums(left);
        vector<vector<int>> sumsRight = getSums(right);
        int ans = INT_MAX;
        for(int k = 0; k <= n; k++) {
            int need = n-k;
            for(int s1: sumsLeft[k]) {
                int tar = total/2 - s1;
                auto &v = sumsRight[need];
                auto it = lower_bound(v.begin(), v.end(), tar);
                if(it != v.end()) {
                    int s2 = *it;
                    ans = min(ans, abs(total - 2*(s1+s2)));
                }
                if(it != v.begin()) {
                    it--;
                    int s2 = *it;
                    ans = min(ans, abs(total - 2*(s1+s2)));
                }
            }
        }
        return ans;
    }
};