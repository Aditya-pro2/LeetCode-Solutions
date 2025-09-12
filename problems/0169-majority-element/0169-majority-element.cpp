class Solution {
public:
    void merge(vector<int>& a, int si, int mid, int ei)
    {
        vector<int> temp;
        int i = si, j = mid + 1;
        while (i <= mid && j <= ei)
        {
            if (a[i] <= a[j])
                temp.push_back(a[i++]);
            else
                temp.push_back(a[j++]);
        }
        while (i <= mid)
            temp.push_back(a[i++]);
        while (j <= ei)
            temp.push_back(a[j++]);
        for (int k = si, x = 0; k <= ei; k++)
            a[k] = temp[x++];
    }

    void mergeSort(vector<int>& a, int si, int ei)
    {
        if (si >= ei)
            return;
        int mid = (si + ei) / 2;
        mergeSort(a, si, mid);
        mergeSort(a, mid + 1, ei);
        merge(a, si, mid, ei);
    }

    int majorityElement(vector<int>& nums)
    {
        int n = nums.size();
        mergeSort(nums, 0, n - 1);
        return nums[n / 2];
    }
};