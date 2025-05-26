mod array;
mod two_pointer;

fn main() {
    vector_methods();
}

fn vector_methods() {
    // init vec
    println!("init vec");
    let mut v1: Vec<i32> = Vec::new();
    let mut v2: Vec<u8> = Vec::with_capacity(5);
    let mut v3 = vec![99; 3];

    // adding element
    println!("\n\nadding element");
    v1.push(3);
    v1.insert(0, 2);
    v2.extend([5, 6, 7, 8, 9]);

    // removing element
    println!("\n\nremoving element");
    let last = v2.pop();
    println!("last = {last:?}");

    let removed = v2.remove(0);
    println!("removed = {removed:?}");

    v3.clear();

    // accessing element
    println!("\n\naccessing element");
    println!("get = {:?}", v2.get(1));
    println!("{:?}", v2[1]);
    println!("first = {:?}", v2.first());
    println!("last = {:?}", v2.last());

    // modified
    println!("\n\nmodified");
    v3.extend([3, 1, 2]);

    v3[0] = 4;
    v3.swap(0, 1);
    v3.sort();

    // querying
    println!("\n\nquerying");
    println!("len = {}", v3.len());
    println!("is_empty = {}", v3.is_empty());
    println!("contains = {}", v3.contains(&2));

    println!("{v1:?}");
    println!("{v2:?}");
    println!("{v3:?}");

    // iteration and transformation
    println!("\n\niteration and transformation");
    for x in v2.iter() {
        println!("{x}");
    }

    for x in v3.iter_mut() {
        *x *= 2;
    }
    println!("{v3:?}");

    let doubled: Vec<u8> = v2.iter().map(|x| x * 2).collect();
    println!("{doubled:?}");

    let evens: Vec<i32> = v3.iter().filter(|&&x| x % 2 == 0).copied().collect();
    println!("{evens:?}");

    // slicing
    println!("slicing");
    let v = vec![1, 2, 3, 4];
    let _slice = v.as_slice(); // &[1, 2, 3, 4]
    let (_left, _right) = v.split_at(2); // left = &[1, 2], right = &[3, 4]

    // capacity management
    println!("capacity management");
    let mut v = Vec::with_capacity(10);
    println!("{}", v.capacity()); // 10
    v.push(1); // v = [1]
    v.shrink_to_fit(); // Capacity may reduce to 1 (implementation-dependent)

    // advance
    println!("advance");
    let mut v = vec![1, 2, 2, 3, 4, 2];
    v.retain(|&x| x % 2 == 0); // v = [2, 2, 4]
    println!("{v:?}");

    v.dedup(); // v = [2, 4]
    v.reverse(); // v = [4, 2]
    println!("{v:?}");
}
