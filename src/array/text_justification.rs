#![allow(dead_code)]
struct Solution;

impl Solution {
    pub fn full_justify(words: Vec<String>, max_width: i32) -> Vec<String> {
        let max_width = max_width as usize;
        let mut result = Vec::new();
        let mut line = Vec::new();
        let mut line_length = 0;

        for word in words {
            if line_length + line.len() + word.len() > max_width {
                result.push(Self::justify_line(&line, line_length, max_width, false));
                line.clear();
                line_length = 0;
            }
            line.push(word.clone());
            line_length += word.len();
        }

        // Handle the last line (left-justified)
        if !line.is_empty() {
            result.push(Self::justify_line(&line, line_length, max_width, true));
        }

        result
    }

    fn justify_line(
        words: &Vec<String>,
        line_length: usize,
        max_width: usize,
        is_last_line: bool,
    ) -> String {
        if words.len() == 1 || is_last_line {
            // Left-justify
            let mut line = words.join(" ");
            line.push_str(&" ".repeat(max_width - line.len()));
            return line;
        }

        let spaces_needed = max_width - line_length;
        let slots = words.len() - 1;
        let space_per_slot = spaces_needed / slots;
        let extra_spaces = spaces_needed % slots;

        let mut line = String::new();
        for (i, word) in words.iter().enumerate() {
            line.push_str(word);
            if i < slots {
                line.push_str(&" ".repeat(space_per_slot + if i < extra_spaces { 1 } else { 0 }));
            }
        }

        line
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn full_justify_v1() {
        let result = Solution::full_justify(
            vec![
                "This".to_string(),
                "is".to_string(),
                "an".to_string(),
                "example".to_string(),
                "of".to_string(),
                "text".to_string(),
                "justification.".to_string(),
            ],
            16,
        );
        assert_eq!(
            result,
            vec![
                "This    is    an".to_string(),
                "example  of text".to_string(),
                "justification.  ".to_string()
            ]
        );
    }

    #[test]
    fn full_justify_v2() {
        let result = Solution::full_justify(
            vec![
                "What".to_string(),
                "must".to_string(),
                "be".to_string(),
                "acknowledgment".to_string(),
                "shall".to_string(),
                "be".to_string(),
            ],
            16,
        );
        assert_eq!(
            result,
            vec![
                "What   must   be".to_string(),
                "acknowledgment  ".to_string(),
                "shall be        ".to_string()
            ]
        );
    }
}
