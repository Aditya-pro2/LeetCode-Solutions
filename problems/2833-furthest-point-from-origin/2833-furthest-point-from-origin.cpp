class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
        int x = 0, y = 0, z = 0;
        for (auto i : moves)
        {
            if (i == 'L')
                x++;
            else if (i == 'R')
                y++;
            else
                z++;
        }
        return abs(x - y) + z;
    }
};