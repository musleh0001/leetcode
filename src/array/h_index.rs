#![allow(dead_code)]
struct Solution;

impl Solution {
    fn h_index(citations: Vec<i32>) -> i32 {
        let mut citations = citations;
        let mut h = 0;

        citations.sort_unstable_by(|a, b| b.cmp(a));

        for (index, &citation) in citations.iter().enumerate() {
            if citation >= (index + 1) as i32 {
                h = (index + 1) as i32;
            } else {
                break;
            }
        }

        h
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn h_index_v1() {
        let result = Solution::h_index(vec![3, 0, 6, 1, 5]);
        assert_eq!(result, 3);
    }

    #[test]
    fn h_index_v2() {
        let result = Solution::h_index(vec![1, 3, 1]);
        assert_eq!(result, 1);
    }
}
