class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        vector<vector<int>> r(2, vector<int>(3, 0));
        vector<vector<int>> c(2, vector<int>(3, 0));
        vector<int> d1(2, 0);
        vector<int> d2(2, 0);
        for (int i = 0; i < moves.size(); i++)
        {
            int x = moves[i][0], y = moves[i][1], idx = i % 2;
            if ((++r[idx][x] == 3) || (++c[idx][y] == 3) || (x == y && ++d1[idx] == 3) || (x + y == 2 && ++d2[idx] == 3))
                return idx == 0 ? "A" : "B";
        }
        return moves.size() == 9 ? "Draw" : "Pending";
    }
};