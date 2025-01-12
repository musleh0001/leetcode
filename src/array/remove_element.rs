#![allow(dead_code)]
struct Solution;

impl Solution {
    fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        nums.retain(|&x| x != val);
        nums.len() as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn remove_element_v1() {
        let mut nums1 = vec![3, 2, 2, 3];
        let result = Solution::remove_element(&mut nums1, 3);
        assert_eq!(result, 2);
    }

    #[test]
    fn remove_element_v2() {
        let mut nums1 = vec![0, 1, 2, 2, 3, 0, 4, 2];
        let result = Solution::remove_element(&mut nums1, 2);
        assert_eq!(result, 5);
    }
}
