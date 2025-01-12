#![allow(dead_code)]

struct Solution;

impl Solution {
    fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut count = [0; 26];

        for ch in s.chars() {
            count[(ch as u8 - b'a') as usize] += 1;
        }

        for ch in t.chars() {
            count[(ch as u8 - b'a') as usize] -= 1;
        }

        count.iter().all(|&x| x == 0)
    }

    fn is_anagram_sort(s: String, t: String) -> bool {
        let mut s_chars: Vec<char> = s.chars().collect();
        let mut t_chars: Vec<char> = t.chars().collect();

        s_chars.sort();
        t_chars.sort();

        s_chars == t_chars
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn is_anagram_v1() {
        let result = Solution::is_anagram(String::from("anagram"), String::from("nagaram"));
        assert_eq!(result, true);
    }

    #[test]
    fn is_anagram_v2() {
        let result = Solution::is_anagram("rat".to_string(), "car".to_string());
        assert_eq!(result, false);
    }
}
