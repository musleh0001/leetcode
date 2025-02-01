#![allow(dead_code)]
use std::collections::HashMap;

struct Solution;

impl Solution {
    fn group_anagrams_sort(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map = HashMap::new();

        for s in strs {
            let mut sorted_chars: Vec<char> = s.chars().collect();
            sorted_chars.sort();
            let sorted_key: String = sorted_chars.into_iter().collect();

            map.entry(sorted_key).or_insert_with(Vec::new).push(s);
        }

        map.into_values().collect()
    }

    fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map = HashMap::new();

        for s in strs {
            let mut count = [0u8; 26];

            for c in s.bytes() {
                count[(c - b'a') as usize] += 1;
            }

            map.entry(count).or_insert_with(Vec::new).push(s);
        }

        map.into_values().collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    // #[ignore = "output orientation not match"]
    #[test]
    fn group_anagrams_v1() {
        let input = vec![
            "eat".to_string(),
            "tea".to_string(),
            "tan".to_string(),
            "ate".to_string(),
            "nat".to_string(),
            "bat".to_string(),
        ];
        let output = vec![
            vec!["eat".to_string(), "tea".to_string(), "ate".to_string()],
            vec!["tan".to_string(), "nat".to_string()],
            vec!["bat".to_string()],
        ];

        let result = Solution::group_anagrams(input);
        assert_eq!(result, output);
    }

    #[test]
    fn group_anagrams_v2() {
        let input = vec!["".to_string()];
        let output = vec![vec!["".to_string()]];

        let result = Solution::group_anagrams(input);
        assert_eq!(result, output);
    }

    #[test]
    fn group_anagrams_v3() {
        let input = vec!["a".to_string()];
        let output = vec![vec!["a".to_string()]];

        let result = Solution::group_anagrams(input);
        assert_eq!(result, output);
    }
}
