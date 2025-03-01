#![allow(dead_code)]

use std::collections::HashSet;

struct Solution;

impl Solution {
    fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let num_set: HashSet<i32> = nums.into_iter().collect();
        let mut max_length = 0;

        for &num in &num_set {
            if !num_set.contains(&(num - 1)) {
                let mut current_num = num;
                let mut current_length = 1;

                while num_set.contains(&(current_num + 1)) {
                    current_num += 1;
                    current_length += 1;
                }

                max_length = max_length.max(current_length);
            }
        }

        max_length
    }

    fn longest_consecutive_rusty(nums: Vec<i32>) -> i32 {
        let num_set: HashSet<i32> = nums.into_iter().collect();

        num_set
            .iter()
            .filter(|&&num| !num_set.contains(&(num - 1)))
            .map(|&num| (num..).take_while(|x| num_set.contains(x)).count() as i32)
            .max()
            .unwrap_or(0)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn longest_consecutive_v1() {
        let result = Solution::longest_consecutive_rusty(vec![100, 4, 200, 1, 3, 2]);
        assert_eq!(result, 4);
    }

    #[test]
    fn longest_consecutive_v2() {
        let result = Solution::longest_consecutive_rusty(vec![0, 3, 7, 2, 5, 8, 4, 6, 0, 1]);
        assert_eq!(result, 9);
    }

    #[test]
    fn longest_consecutive_v3() {
        let result = Solution::longest_consecutive_rusty(vec![1, 0, 1, 2]);
        assert_eq!(result, 3);
    }
}
