class Solution {
public:
    bool isSafe(vector<vector<char>>& sudoku, int row, int col, char digit)
    {
        for (int i = 0; i < 9; i++)
            if (sudoku[i][col] == digit)
                return false;
        for (int j = 0; j < 9; j++)
            if (sudoku[row][j] == digit)
                return false;
        int startRow = (row / 3) * 3, startCol = (col / 3) * 3;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (sudoku[i + startRow][j + startCol]  == digit)
                    return false;
        return true;
    }

    bool sudokuSolver(vector<vector<char>>& sudoku, int row, int col)
    {
        if (row == 9)
            return true;
        int nextRow = row, nextCol = col + 1;
        if (col == 8)
        {
            nextRow = row + 1;
            nextCol = 0;
        }
        if (sudoku[row][col] != '.')
            return sudokuSolver(sudoku, nextRow, nextCol);
        for (char i = '1'; i <= '9'; i++)
        {
            if (isSafe(sudoku, row, col, i))
            {
                sudoku[row][col] = i;
                if (sudokuSolver(sudoku, nextRow, nextCol))
                    return true;
                sudoku[row][col] = '.';
            }
        }
        return false;
    }

    void solveSudoku(vector<vector<char>>& sudoku)
    {
        sudokuSolver(sudoku, 0, 0);
    }
};