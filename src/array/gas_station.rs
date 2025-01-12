#![allow(dead_code)]
struct Solution;

impl Solution {
    // greddy
    fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        if gas.iter().sum::<i32>() < cost.iter().sum::<i32>() {
            return -1;
        }

        let (mut start, mut tank) = (0, 0);

        for index in 0..gas.len() {
            tank += gas[index] - cost[index];

            if tank < 0 {
                start = index + 1;
                tank = 0;
            }
        }

        start as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn can_complete_circuit_v1() {
        let result = Solution::can_complete_circuit(vec![1, 2, 3, 4, 5], vec![3, 4, 5, 1, 2]);
        assert_eq!(result, 3);
    }

    #[test]
    fn can_complete_circuit_v2() {
        let result = Solution::can_complete_circuit(vec![2, 3, 4], vec![3, 4, 3]);
        assert_eq!(result, -1);
    }
}
