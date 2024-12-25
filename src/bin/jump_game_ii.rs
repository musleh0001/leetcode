struct Solution;

impl Solution {
    fn jump(nums: Vec<i32>) -> i32 {
        let (mut result, mut left, mut right) = (0, 0, 0);

        while right < nums.len() - 1 {
            let mut farthest = 0;

            for index in left..right + 1 {
                farthest = std::cmp::max(farthest, index + nums[index] as usize);
            }

            left = right + 1;
            right = farthest;
            result += 1;
        }

        result
    }
}

pub fn main() {
    let result = Solution::jump(vec![3, 0, 6, 1, 5]);
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn jump_v1() {
        let result = Solution::jump(vec![2, 3, 1, 1, 4]);
        assert_eq!(result, 2);
    }

    #[test]
    fn jump_v2() {
        let result = Solution::jump(vec![2, 3, 0, 1, 4]);
        assert_eq!(result, 2);
    }
}
