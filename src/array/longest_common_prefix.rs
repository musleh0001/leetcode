#![allow(dead_code)]
struct Solution;

impl Solution {
    fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return String::from("");
        }

        let mut prefix = strs[0].clone();

        for s in strs.iter().skip(1) {
            while !s.starts_with(&prefix) {
                prefix.pop();
                if prefix.is_empty() {
                    return "".to_string();
                }
            }
        }

        prefix
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn longest_common_prefix_v1() {
        let result = Solution::longest_common_prefix(vec![
            String::from("flower"),
            String::from("flow"),
            String::from("flight"),
        ]);
        assert_eq!(result, String::from("fl"));
    }

    #[test]
    fn longest_common_prefix_v2() {
        let result = Solution::longest_common_prefix(vec![
            String::from("dog"),
            String::from("racecar"),
            String::from("car"),
        ]);
        assert_eq!(result, String::from(""));
    }
}
