struct Solution;

impl Solution {
    fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 || s.len() <= num_rows as usize {
            return s;
        }

        let mut rows = vec![String::new(); num_rows as usize];
        let mut current_row = 0;
        let mut going_down = false;

        for c in s.chars() {
            rows[current_row].push(c);

            if current_row == 0 || current_row == (num_rows - 1) as usize {
                going_down = !going_down;
            }

            if going_down {
                current_row += 1;
            } else {
                current_row -= 1;
            }
        }

        rows.concat()
    }
}

fn main() {
    let result = Solution::convert(String::from("PAYPALISHIRING"), 3);
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn convert_v1() {
        let result = Solution::convert(String::from("PAYPALISHIRING"), 3);
        assert_eq!(result, String::from("PAHNAPLSIIGYIR"));
    }

    #[test]
    fn convert_v2() {
        let result = Solution::convert(String::from("PAYPALISHIRING"), 4);
        assert_eq!(result, String::from("PINALSIGYAHRPI"));
    }
}
