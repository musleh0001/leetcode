#![allow(dead_code)]

use std::collections::HashMap;

struct Solution;

impl Solution {
    fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut frequency_map = HashMap::new();
        for &num in &nums {
            *frequency_map.entry(num).or_insert(0) += 1;
        }

        let max_freq = *frequency_map.values().max().unwrap_or(&0);
        let mut buckets = vec![vec![]; (max_freq + 1) as usize];

        for (num, freq) in frequency_map {
            buckets[freq as usize].push(num);
        }

        let mut result = Vec::new();
        for i in (0..buckets.len()).rev() {
            for &num in &buckets[i] {
                result.push(num);
                if result.len() == k as usize {
                    return result;
                }
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn top_k_frequent_v1() {
        let result = Solution::top_k_frequent(vec![1, 1, 1, 2, 2, 3], 2);
        assert_eq!(result, vec![1, 2]);
    }

    #[test]
    fn top_k_frequent_v2() {
        let result = Solution::top_k_frequent(vec![1], 1);
        assert_eq!(result, vec![1]);
    }
}
