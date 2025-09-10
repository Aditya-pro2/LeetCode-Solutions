class Solution {
public:
    string predictPartyVictory(string senate) {
        const int n = senate.size();
        queue<int> rad, dir;
        for (int i = 0; i < n; i++)
        {
            if (senate[i] == 'R')
                rad.push(i);
            else
                dir.push(i);
        }
        for (int i = n; !rad.empty() && !dir.empty(); i++)
        {
            if (rad.front() < dir.front())
                rad.push(i);
            else
                dir.push(i);
            rad.pop();
            dir.pop();
        }
        return rad.empty() ? "Dire" : "Radiant";
    }
};