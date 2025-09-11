class Solution {
    bool canEatBananas(vector<int>& piles, int h, int banana) {
        int n = piles.size(), pilesCount = 0;
        for (int i = 0; i < n; i++)
        {
            if (piles[i] % banana == 0)
                pilesCount += (piles[i] / banana);
            else
                pilesCount += ((piles[i] / banana) + 1);
            if (pilesCount > h)
                return false;
        }
        return true;
    }
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.rbegin(), piles.rend());
        int n = piles.size(), start = 1, end = piles[0], ans = 0;
        while (start <= end)
        {
            int mid = start + ((end - start) >> 1);
            if (canEatBananas(piles, h, mid))
            {
                ans = mid;
                end = mid - 1;
            }
            else
                start = mid + 1;
        }
        return ans;
    }
};