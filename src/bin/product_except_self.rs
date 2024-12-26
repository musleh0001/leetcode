struct Solution;

impl Solution {
    fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = vec![1; nums.len()];

        let mut prefix = 1;
        for index in 0..nums.len() {
            result[index] = prefix;
            prefix *= nums[index];
        }

        let mut postfix = 1;
        for index in (0..nums.len()).rev() {
            result[index] *= postfix;
            postfix *= nums[index];
        }

        result
    }
}

pub fn main() {
    let result = Solution::product_except_self(vec![1, 2, 3, 4]);
    println!("{result:?}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn product_except_self_v1() {
        let result = Solution::product_except_self(vec![1, 2, 3, 4]);
        assert_eq!(result, vec![24, 12, 8, 6]);
    }

    #[test]
    fn product_except_self_v2() {
        let result = Solution::product_except_self(vec![-1, 1, 0, -3, 3]);
        assert_eq!(result, vec![0, 0, 9, 0, 0]);
    }
}
