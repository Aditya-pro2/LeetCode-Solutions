class Solution {
public:
    bool isSafe(vector<string> board, int row, int col, int n)
    {
        for (int i = 0; i < row; i++)                           //Vertical
            if (board[i][col] == 'Q')
                return false;
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)  //Left Diagonal
            if (board[i][j] == 'Q')
                return false;
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++)   //Right Diagonal
            if (board[i][j] == 'Q')
                return false;
        return true;
    }

    void nQueens(vector<vector<string>>& ans, vector<string>& board, int row, int n)
    {
        if (row == n)
        {
            ans.push_back(board);
            return;
        }
        for (int j = 0; j < n; j++)
        {
            if (isSafe(board, row, j, n))
            {
                board[row][j] = 'Q';
                nQueens(ans, board, row + 1, n);
                board[row][j] = '.';
            }
        }
    }

    vector<vector<string>> solveNQueens(int n)
    {
        vector<vector<string>> ans;
        vector<string> board(n, string(n, '.'));
        nQueens(ans, board, 0, n);
        return ans;
    }
};