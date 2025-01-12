#![allow(dead_code)]
struct Solution;

impl Solution {
    fn candy(ratings: Vec<i32>) -> i32 {
        let mut result = vec![1; ratings.len()];

        for index in 1..ratings.len() {
            if ratings[index - 1] < ratings[index] {
                result[index] = result[index - 1] + 1;
            }
        }

        for index in (0..ratings.len() - 1).rev() {
            if ratings[index] > ratings[index + 1] {
                result[index] = std::cmp::max(result[index], result[index + 1] + 1);
            }
        }

        result.iter().sum()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn candy_v1() {
        let result = Solution::candy(vec![1, 0, 2]);
        assert_eq!(result, 5);
    }

    #[test]
    fn candy_v2() {
        let result = Solution::candy(vec![1, 2, 2]);
        assert_eq!(result, 4);
    }

    #[test]
    fn candy_v3() {
        let result = Solution::candy(vec![1, 2, 87, 87, 87, 2, 1]);
        assert_eq!(result, 13);
    }
}
