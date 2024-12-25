struct Solution;

impl Solution {
    // Boyer-Moore Voting Algorithm
    fn majority_element(nums: Vec<i32>) -> i32 {
        let (mut majority, mut count) = (0, 0);

        for &num in nums.iter() {
            if count == 0 {
                majority = num;
            }

            if majority == num {
                count += 1;
            } else {
                count -= 1;
            }
        }

        majority
    }

    fn majority_element_v2(nums: Vec<i32>) -> i32 {
        let mut count = std::collections::HashMap::new();
        let (mut result_key, mut max_count) = (0, 0);

        for num in nums {
            let value = count.entry(num).and_modify(|e| *e += 1).or_insert(1);
            result_key = if *value > max_count { num } else { result_key };
            max_count = std::cmp::max(*value, max_count);
        }

        result_key
    }

    fn majority_element_rusty(nums: Vec<i32>) -> i32 {
        nums.iter()
            .fold((0, 0), |(mut majority, mut count), &num| {
                if count == 0 {
                    majority = num
                };
                count = if majority == num {
                    count + 1
                } else {
                    count - 1
                };
                (majority, count)
            })
            .0
    }
}

pub fn main() {
    let result = Solution::majority_element(vec![3, 2, 3]);
    println!("{result}");

    let result = Solution::majority_element_v2(vec![3, 2, 3]);
    println!("{result}");

    let result = Solution::majority_element_rusty(vec![3, 2, 3]);
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn majority_element_v1() {
        let result = Solution::majority_element_rusty(vec![3, 2, 3]);
        assert_eq!(result, 3);
    }

    #[test]
    fn majority_element_v2() {
        let result = Solution::majority_element_rusty(vec![2, 2, 1, 1, 1, 2, 2]);
        assert_eq!(result, 2);
    }

    #[test]
    fn majority_element_v3() {
        let result = Solution::majority_element_rusty(vec![2, 2, 1, 1, 5, 1, 2, 2]);
        assert_eq!(result, 2);
    }
}
