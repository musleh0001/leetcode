#![allow(dead_code)]
struct Solution;

impl Solution {
    fn str_str(haystack: String, needle: String) -> i32 {
        if let Some(index) = haystack.find(&needle) {
            index as i32
        } else {
            -1
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn str_str_v1() {
        let result = Solution::str_str(String::from("sadbutsad"), String::from("sad"));
        assert_eq!(result, 0);
    }

    #[test]
    fn str_str_v2() {
        let result = Solution::str_str(String::from("leetcode"), String::from("leeto"));
        assert_eq!(result, -1);
    }
}
