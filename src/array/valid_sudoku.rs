#![allow(dead_code, unused_imports)]
use std::collections::HashSet;

struct Solution;

impl Solution {
    fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        // Initialize HashSets for rows, columns, and 3x3 boxes
        let mut rows: Vec<HashSet<char>> = vec![HashSet::new(); 9];
        let mut cols: Vec<HashSet<char>> = vec![HashSet::new(); 9];
        let mut boxes: Vec<HashSet<char>> = vec![HashSet::new(); 9];

        // Iterate through the 9x9 board
        for i in 0..9 {
            for j in 0..9 {
                let cell = board[i][j];

                // Skip empty cells
                if cell == '.' {
                    continue;
                }

                // Check row
                if !rows[i].insert(cell) {
                    return false; // Duplicate in row
                }

                // Check column
                if !cols[j].insert(cell) {
                    return false; // Duplicate in column
                }

                // Check 3x3 box
                // Box index: (i / 3) * 3 + (j / 3)
                let box_idx = (i / 3) * 3 + j / 3;
                if !boxes[box_idx].insert(cell) {
                    return false; // Duplicate in box
                }
            }
        }

        true // No duplicates found
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn is_valid_sudoku_v1() {
        let input = vec![
            vec!['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ];
        let result = Solution::is_valid_sudoku(input);
        assert_eq!(result, true);
    }

    #[test]
    fn is_valid_sudoku_v2() {
        let input = vec![
            vec!['8', '3', '.', '.', '7', '.', '.', '.', '.'],
            vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ];
        let result = Solution::is_valid_sudoku(input);
        assert_eq!(result, false);
    }
}
