#![allow(dead_code)]
struct Solution;

impl Solution {
    fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = std::collections::HashSet::new();

        for &num in &nums {
            if !seen.insert(num) {
                return true;
            }
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn contains_duplicate_v1() {
        let result = Solution::contains_duplicate(vec![1, 2, 3, 1]);
        assert_eq!(result, true);
    }

    #[test]
    fn contains_duplicate_v2() {
        let result = Solution::contains_duplicate(vec![1, 2, 3, 4]);
        assert_eq!(result, false);
    }

    #[test]
    fn contains_duplicate_v3() {
        let result = Solution::contains_duplicate(vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2]);
        assert_eq!(result, true);
    }
}
