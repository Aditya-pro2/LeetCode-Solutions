class Solution {
public:
    static bool compare(vector<int>& v1, vector<int>& v2)
    {
        if (v1[0] < v2[0])
            return true;
        else if (v1[0] == v2[0])
        {
            if (v1[1] < v2[1])
                return true;
            else if (v1[1] == v2[1])
            {
                if (v1[2] < v2[2])
                    return true;
            }
        }
        return false;
    }

    int maxHeight(vector<vector<int>>& cuboids)
    {
        for (int i = 0; i < cuboids.size(); i++)
            sort(cuboids[i].begin(), cuboids[i].end());
        sort(cuboids.begin(), cuboids.end(), compare);
        vector<int> height(cuboids.size(), 0);
        int h = 0;
        for (int i = 0; i < cuboids.size(); i++)
        {
            height[i] = cuboids[i][2];
            for (int j = 0; j < i; j++)
                if (cuboids[i][0] >= cuboids[j][0] && cuboids[i][1] >= cuboids[j][1] && cuboids[i][2] >= cuboids[j][2])
                    height[i] = max(height[i], height[j] + cuboids[i][2]);
        }
        int maxHeight = *max_element(height.begin(), height.end());
        return maxHeight;
    }
};