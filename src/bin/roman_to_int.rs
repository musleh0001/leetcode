use std::collections::HashMap;

struct Solution;

impl Solution {
    #[allow(dead_code)]
    fn roman_to_int_v2(s: String) -> i32 {
        let roman = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]);
        let mut result = 0;
        let chars: Vec<char> = s.chars().collect();

        for index in 0..chars.len() {
            let current_value = *roman.get(&chars[index]).unwrap();

            if index + 1 < chars.len() && current_value < *roman.get(&chars[index + 1]).unwrap() {
                result -= current_value;
            } else {
                result += current_value;
            }
        }

        result
    }

    fn roman_to_int(s: String) -> i32 {
        let mut result = 0;
        let chars: Vec<char> = s.chars().collect();
        let mut i = 0;

        while i < chars.len() {
            match chars[i..] {
                ['I', 'V', ..] => {
                    result += 4;
                    i += 2; // Skip the next character
                }
                ['I', 'X', ..] => {
                    result += 9;
                    i += 2;
                }
                ['X', 'L', ..] => {
                    result += 40;
                    i += 2;
                }
                ['X', 'C', ..] => {
                    result += 90;
                    i += 2;
                }
                ['C', 'D', ..] => {
                    result += 400;
                    i += 2;
                }
                ['C', 'M', ..] => {
                    result += 900;
                    i += 2;
                }
                _ => {
                    result += match chars[i] {
                        'I' => 1,
                        'V' => 5,
                        'X' => 10,
                        'L' => 50,
                        'C' => 100,
                        'D' => 500,
                        'M' => 1000,
                        _ => panic!("Invalid Roman numeral"),
                    };
                    i += 1; // Move to the next character
                }
            }
        }

        result
    }
}

fn main() {
    let s = String::from("III");
    let result = Solution::roman_to_int(s);
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn roman_to_int_v1() {
        let s = String::from("III");
        let result = Solution::roman_to_int(s);

        assert_eq!(result, 3);
    }

    #[test]
    fn roman_to_int_v2() {
        let s = String::from("LVIII");
        let result = Solution::roman_to_int(s);

        assert_eq!(result, 58);
    }

    #[test]
    fn roman_to_int_v3() {
        let s = String::from("MCMXCIV");
        let result = Solution::roman_to_int(s);

        assert_eq!(result, 1994);
    }
}
