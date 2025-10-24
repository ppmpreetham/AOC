use std::fs;
fn checkIncreasing(numbers: &str) -> usize {
    let mut count = 0;
    let nums: Vec<i32> = numbers
        .lines()
        .filter_map(|line| line.parse::<i32>().ok())
        .collect();
    for i in 0..nums.len() - 3 {
        if nums[i + 3] > nums[i] {
            count += 1;
        }
    }
    count
}
fn main() {
    let inps =
        fs::read_to_string("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2021/_day-01/input.txt")
            .unwrap();
    let ans = checkIncreasing(&inps);
    println!("{ans}")
}
