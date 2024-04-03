public class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int i, int j, int wordIndex) {
        // Check boundaries and if current cell matches the word character at wordIndex
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(wordIndex)) {
            return false;
        }
        // If all characters are checked
        if (wordIndex == word.length() - 1) {
            return true;
        }
        // Mark the current cell as visited by altering the character (to avoid using extra space for a visited matrix)
        char temp = board[i][j];
        board[i][j] = '#'; // Mark as visited
        // Explore all possible directions
        boolean found = dfs(board, word, i + 1, j, wordIndex + 1) ||
                        dfs(board, word, i - 1, j, wordIndex + 1) ||
                        dfs(board, word, i, j + 1, wordIndex + 1) ||
                        dfs(board, word, i, j - 1, wordIndex + 1);
        // Backtrack and unmark the visited cell
        board[i][j] = temp;
        return found;
    }
}