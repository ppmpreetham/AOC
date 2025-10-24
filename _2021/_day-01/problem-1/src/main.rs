use std::fs;

fn numofIncreasingElements(numbers: &str) -> usize {
    let mut count = 0;
    let inps: Vec<i32> = numbers
        .lines()
        .filter_map(|line| line.parse().ok())
        .collect();
    // println!("{:?}", inps);
    for num in 1..inps.len() {
        if inps[num] > inps[num - 1] {
            count += 1;
        }
    }
    count
}
fn main() {
    let numbers =
        fs::read_to_string("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2021/_day-01/input.txt")
            .unwrap();
    let count = numofIncreasingElements(&numbers);
    println!("Number of increasing elements: {}", count);
}
