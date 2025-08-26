class Solution {
public:
    bool isRobotBounded(string instructions) {
        int dx = 0, dy = 1, x = 0, y = 0;
        for (auto i : instructions)
        {
            if (i == 'G')
            {
                x += dx;
                y += dy;
            }
            else if (i == 'L')
            {
                swap(dx, dy);
                dx = -dx;
            }
            else
            {
                swap(dx, dy);
                dy = -dy;
            }            
        }
        return (x == 0 && y == 0) || (!(dx == 0 && dy == 1));
    }
};