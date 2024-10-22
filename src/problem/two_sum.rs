pub struct Solution;

impl Solution {
    pub fn two_sum() {
        println!("Two Sum");
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn two_sum_v1() {
        Solution::two_sum();
        assert_eq!(1, 1);
    }
}