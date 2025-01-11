struct Solution;

impl Solution {
    fn reverse_words(s: String) -> String {
        s.split_whitespace().rev().collect::<Vec<&str>>().join(" ")
    }
}

fn main() {
    let result = Solution::reverse_words(String::from("the sky is blue"));
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn reverse_words_v1() {
        let result = Solution::reverse_words(String::from("the sky is blue"));
        assert_eq!(result, String::from("blue is sky the"));
    }

    #[test]
    fn reverse_words_v2() {
        let result = Solution::reverse_words(String::from("  hello world  "));
        assert_eq!(result, String::from("world hello"));
    }
}
