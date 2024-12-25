use std::collections::HashMap;
use std::hash::BuildHasher;
use std::hash::Hasher;
use std::hash::RandomState;

struct RandomizedSet {
    map: HashMap<i32, usize>,
    vec: Vec<i32>,
}

/*
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {
    fn new() -> Self {
        Self {
            map: HashMap::new(),
            vec: Vec::new(),
        }
    }

    fn insert(&mut self, val: i32) -> bool {
        if self.map.contains_key(&val) {
            return false;
        }

        self.vec.push(val);
        self.map.insert(val, self.vec.len() - 1);

        true
    }

    fn remove(&mut self, val: i32) -> bool {
        if let Some(&index) = self.map.get(&val) {
            let last_val = self.vec[self.vec.len() - 1];
            self.vec[index] = last_val;
            self.map.insert(last_val, index);
            self.vec.pop();
            self.map.remove(&val);

            return true;
        }

        false
    }

    fn get_random(&self) -> i32 {
        self.vec[Self::get_random_number() % self.vec.len()]
    }

    fn get_random_number() -> usize {
        RandomState::new()
            .build_hasher()
            .finish()
            .try_into()
            .unwrap()
    }
}

pub fn main() {
    let mut randomized_set = RandomizedSet::new();

    println!("{}", randomized_set.insert(1)); // true
    println!("{}", randomized_set.remove(2)); // false
    println!("{}", randomized_set.insert(2)); // true
    println!("{}", randomized_set.get_random()); // Randomly returns 1 or 2
    println!("{}", randomized_set.remove(1)); // true
    println!("{}", randomized_set.insert(2)); // false (already present)
    println!("{}", randomized_set.get_random()); // Always returns 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_randomized_set() {
        let mut randomized_set = RandomizedSet::new();

        assert_eq!(randomized_set.insert(1), true);
        assert_eq!(randomized_set.remove(2), false);
        assert_eq!(randomized_set.insert(2), true);

        let random = randomized_set.get_random();
        assert!(random == 1 || random == 2);
        assert_eq!(randomized_set.remove(1), true);
        assert_eq!(randomized_set.insert(2), false);
        assert_eq!(randomized_set.get_random(), 2);
    }

    #[test]
    fn test_randomized_set_edge_cases() {
        let mut randomized_set = RandomizedSet::new();

        assert_eq!(randomized_set.insert(-1), true);
        assert_eq!(randomized_set.insert(-2), true);
        assert_eq!(randomized_set.remove(-1), true);
        assert_eq!(randomized_set.remove(-1), false); // Already removed
        assert_eq!(randomized_set.get_random(), -2);
    }
}

/*
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
