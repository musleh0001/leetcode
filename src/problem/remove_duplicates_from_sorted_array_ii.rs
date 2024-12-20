use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut count_map = HashMap::new();

        nums.retain(|&num| {
            let count = count_map.entry(num).or_insert(0);

            if *count < 2 {
                *count += 1;
                true
            } else {
                false
            }
        });
        nums.len() as i32
    }

    pub fn remove_duplicates_v2(nums: &mut Vec<i32>) -> i32 {
        if nums.len() <= 2 {
            return nums.len() as i32;
        }

        let mut j = 2;

        for i in 2..nums.len() {
            if nums[i] != nums[j - 2] {
                nums[j] = nums[i];
                j += 1;
            }
        }

        j as i32
    }

    /*
        # Walk through
        - input: [1, 1, 1, 2, 2, 3]
        - step 01:
            - i = 2; j = 2; [1, 1, 1, 2, 2, 3]
        - step 02:
            - i = 3; j = 2; [1, 1, 2, 2, 2, 3]; j = 3;
        - step 03:
            - i = 4; j = 3; [1, 1, 2, 2, 2, 3]; j = 4;
        - step 04:
            - i = 5; j = 4; [1, 1, 2, 2, 3, 3]; j = 5;

        result => 5
    */
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn remove_duplicates_v1() {
        let mut nums = vec![1, 1, 1, 2, 2, 3];

        let result = Solution::remove_duplicates(&mut nums);
        assert_eq!(result, 5);
    }

    #[test]
    fn remove_duplicates_v2() {
        let result = Solution::remove_duplicates(&mut vec![0, 0, 1, 1, 1, 1, 2, 3, 3]);
        assert_eq!(result, 7);
    }

    #[test]
    fn remove_duplicates_v3() {
        let result = Solution::remove_duplicates_v2(&mut vec![1, 1, 1, 2, 2, 3]);
        assert_eq!(result, 5);
    }

    #[test]
    fn remove_duplicates_v4() {
        let result = Solution::remove_duplicates_v2(&mut vec![0, 0, 1, 1, 1, 1, 2, 3, 3]);
        assert_eq!(result, 7);
    }

    #[test]
    fn remove_duplicates_v5() {
        let result = Solution::remove_duplicates_v2(&mut vec![]);
        assert_eq!(result, 0);
    }
}
