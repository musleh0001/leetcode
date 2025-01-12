#![allow(dead_code)]
struct Solution;

impl Solution {
    fn length_of_last_word(s: String) -> i32 {
        s.trim_end()
            .split_whitespace()
            .last()
            .map_or(0, |word| word.len() as i32)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn length_of_last_word_v1() {
        let result = Solution::length_of_last_word(String::from("Hello World"));
        assert_eq!(result, 5);
    }

    #[test]
    fn length_of_last_word_v2() {
        let result = Solution::length_of_last_word(String::from("   fly me   to   the moon  "));
        assert_eq!(result, 4);
    }

    #[test]
    fn length_of_last_word_v3() {
        let result = Solution::length_of_last_word(String::from("luffy is still joyboy"));
        assert_eq!(result, 6);
    }
}
