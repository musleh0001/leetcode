pub struct Solution;

impl Solution {
    // Boyer-Moore Voting Algorithm
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let (mut m, mut c) = (0, 0);

        for &num in nums.iter() {
            if c == 0 {
                m = num;
            }

            if m == num {
                c += 1;
            } else {
                c -= 1;
            }
        }

        m
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn majority_element_v1() {
        let result = Solution::majority_element(vec![3, 2, 3]);
        assert_eq!(result, 3);
    }

    #[test]
    fn majority_element_v2() {
        let result = Solution::majority_element(vec![2, 2, 1, 1, 1, 2, 2]);
        assert_eq!(result, 2);
    }

    #[test]
    fn majority_element_v3() {
        let result = Solution::majority_element(vec![2, 2, 1, 1, 5, 1, 2, 2]);
        assert_eq!(result, 2);
    }
}
