#![allow(dead_code)]
struct Solution;

impl Solution {
    fn rotate(nums: &mut Vec<i32>, k: i32) {
        let effective_k = k % nums.len() as i32;
        nums.rotate_right(effective_k as usize);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn rotate_v1() {
        let mut nums = vec![1, 2, 3, 4, 5, 6, 7];
        Solution::rotate(&mut nums, 3);

        assert_eq!(nums, vec![5, 6, 7, 1, 2, 3, 4]);
    }

    #[test]
    fn rotate_v2() {
        let mut nums = vec![-1, -100, 3, 99];
        Solution::rotate(&mut nums, 2);

        assert_eq!(nums, vec![3, 99, -1, -100]);
    }

    #[test]
    fn rotate_v3() {
        let mut nums = vec![-1];
        Solution::rotate(&mut nums, 2);

        assert_eq!(nums, vec![-1]);
    }
}
