#![allow(dead_code)]

struct Solution;

impl Solution {
    fn encode(strs: Vec<String>) -> String {
        let mut encoded = String::new();
        for s in strs {
            encoded.push_str(&format!("{}#{}", s.len(), s));
        }

        encoded
    }

    fn decode(s: String) -> Vec<String> {
        let mut decoded = Vec::new();
        let mut i = 0;
        let chars: Vec<char> = s.chars().collect();

        while i < chars.len() {
            let mut len = 0;
            while i < chars.len() && chars[i] != '#' {
                len = len * 10 + (chars[i] as u8 - b'0') as usize;
                i += 1;
            }
            i += 1;
            let end = i + len;
            if end <= chars.len() {
                let str_slice: String = chars[i..end].iter().collect();
                decoded.push(str_slice);
                i = end;
            } else {
                break;
            }
        }

        decoded
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn encode_v1() {
        let result = Solution::encode(vec![
            "md".to_string(),
            "musleh".to_string(),
            "uddin".to_string(),
            "khan".to_string(),
        ]);
        assert_eq!(result, String::from("2#md6#musleh5#uddin4#khan"));
    }

    #[test]
    fn encode_v2() {
        let result = Solution::encode(vec!["l##d".to_string(), "2#code".to_string()]);
        assert_eq!(result, String::from("4#l##d6#2#code"));
    }

    #[test]
    fn decode_v1() {
        let output = vec![
            "md".to_string(),
            "musleh".to_string(),
            "uddin".to_string(),
            "khan".to_string(),
        ];
        let result = Solution::decode(String::from("2#md6#musleh5#uddin4#khan"));
        assert_eq!(result, output);
    }

    #[test]
    fn decode_v2() {
        let output = vec!["l##d".to_string(), "2#code".to_string()];
        let result = Solution::decode(String::from("4#l##d6#2#code"));
        assert_eq!(result, output);
    }
}
