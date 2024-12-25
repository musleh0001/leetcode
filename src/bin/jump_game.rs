struct Solution;

impl Solution {
    fn can_jump_greedy(nums: Vec<i32>) -> bool {
        let mut goal = nums.len() - 1;

        for (index, &num) in nums.iter().enumerate().rev() {
            if index + num as usize >= goal {
                goal = index;
            }
        }

        goal == 0
    }

    fn can_jump_greedy_v2(nums: Vec<i32>) -> bool {
        let mut farthest = 0;

        for index in 0..nums.len() {
            if index > farthest {
                return false;
            }
            farthest = std::cmp::max(farthest, index + nums[index] as usize);
        }

        true
    }

    fn can_jump_dp(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut dp = vec![false; n];
        dp[0] = true;

        for i in 0..n {
            if dp[i] {
                let max_jump = nums[i] as usize;
                for j in i + 1..=std::cmp::min(i + max_jump, n - 1) {
                    dp[j] = true;
                }
            }
        }

        dp[n - 1]
    }
}

pub fn main() {
    let result = Solution::can_jump_dp(vec![2, 3, 1, 1, 4]);
    println!("{result}");

    let result = Solution::can_jump_greedy(vec![2, 3, 1, 1, 4]);
    println!("{result}");

    let result = Solution::can_jump_greedy_v2(vec![2, 3, 1, 1, 4]);
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn can_jump_v1() {
        let result = Solution::can_jump_greedy(vec![2, 3, 1, 1, 4]);
        assert_eq!(result, true);
    }

    #[test]
    fn can_jump_v2() {
        let result = Solution::can_jump_greedy(vec![3, 2, 1, 0, 4]);
        assert_eq!(result, false);
    }

    #[test]
    fn can_jump_v3() {
        let result = Solution::can_jump_dp(vec![2, 3, 1, 1, 4]);
        assert_eq!(result, true);
    }

    #[test]
    fn can_jump_v4() {
        let result = Solution::can_jump_dp(vec![3, 2, 1, 0, 4]);
        assert_eq!(result, false);
    }
}
