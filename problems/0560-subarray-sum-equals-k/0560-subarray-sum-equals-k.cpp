class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        m[0] = 1;
        int s = 0, ans = 0;
        for (int i : nums)
        {
            s += i;
            if (m.count(s - k))
                ans += m[s - k];
            if (m.count(s))
                m[s]++;
            else
                m[s] = 1;
        }
        return ans;
    }
};