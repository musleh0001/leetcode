#![allow(dead_code)]
struct Solution;

impl Solution {
    fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        nums.dedup();
        nums.len() as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn remove_duplicates_v1() {
        let result = Solution::remove_duplicates(&mut vec![1, 1, 2]);
        assert_eq!(result, 2);
    }

    #[test]
    fn remove_duplicates_v2() {
        let result = Solution::remove_duplicates(&mut vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4]);
        assert_eq!(result, 5);
    }
}
