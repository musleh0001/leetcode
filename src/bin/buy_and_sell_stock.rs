struct Solution;

impl Solution {
    // two pointer
    fn max_profit(prices: Vec<i32>) -> i32 {
        let (mut buy, mut sell, mut max_profit) = (0, 1, 0);

        while sell < prices.len() {
            if prices[buy] < prices[sell] {
                max_profit = std::cmp::max(max_profit, prices[sell] - prices[buy]);
            } else {
                buy = sell;
            }

            sell += 1;
        }

        max_profit
    }
}

pub fn main() {
    let result = Solution::max_profit(vec![7, 1, 5, 3, 6, 4]);
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn max_profit_v1() {
        let result = Solution::max_profit(vec![7, 1, 5, 3, 6, 4]);
        assert_eq!(result, 5);
    }

    #[test]
    fn max_profit_v2() {
        let result = Solution::max_profit(vec![7, 6, 4, 3, 1]);
        assert_eq!(result, 0);
    }
}
