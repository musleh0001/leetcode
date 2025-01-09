struct Solution;

impl Solution {
    #[allow(dead_code)]
    fn int_to_roman(mut num: i32) -> String {
        let roman_numerals = vec![
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ];

        let mut result = String::new();

        for (value, symbol) in roman_numerals {
            while num >= value {
                result.push_str(symbol);
                num -= value;
            }
        }

        result
    }
}

fn main() {
    let result = Solution::int_to_roman(3749);
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn int_to_roman_v1() {
        let result = Solution::int_to_roman(3749);
        assert_eq!(result, String::from("MMMDCCXLIX"));
    }

    #[test]
    fn int_to_roman_v2() {
        let result = Solution::int_to_roman(58);
        assert_eq!(result, String::from("LVIII"));
    }

    #[test]
    fn int_to_roman_v3() {
        let result = Solution::int_to_roman(1994);
        assert_eq!(result, String::from("MCMXCIV"));
    }
}
