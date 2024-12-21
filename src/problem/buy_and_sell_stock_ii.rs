pub struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit = 0;

        for index in 1..prices.len() {
            if prices[index] > prices[index - 1] {
                max_profit += prices[index] - prices[index - 1];
            }
        }

        max_profit
    }

    pub fn max_profit_v2(prices: Vec<i32>) -> i32 {
        let mut max_profit = 0;

        for index in 0..(prices.len() - 1) {
            let profit = prices[index + 1] - prices[index];

            if profit > 0 {
                max_profit += profit;
            }
        }

        max_profit
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn max_profit_v1() {
        let result = Solution::max_profit_v2(vec![7, 1, 5, 3, 6, 4]);
        assert_eq!(result, 7);
    }

    #[test]
    fn max_profit_v2() {
        let result = Solution::max_profit_v2(vec![1, 2, 3, 4, 5]);
        assert_eq!(result, 4);
    }

    #[test]
    fn max_profit_v3() {
        let result = Solution::max_profit_v2(vec![7, 6, 4, 3, 1]);
        assert_eq!(result, 0);
    }
}
