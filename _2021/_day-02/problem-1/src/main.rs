use std::fs;
fn wow(numbers: &str) -> usize {
    let mut length = 0;
    let mut depth = 0;
    for num in numbers.lines() {
        let nums = num.split(" ").collect::<Vec<&str>>();
        match nums[0] {
            "forward" => length += nums[1].parse::<usize>().unwrap(),
            "down" => depth += nums[1].parse::<usize>().unwrap(),
            "up" => depth -= nums[1].parse::<usize>().unwrap(),
            _ => (),
        }
    }
    length * depth
}
fn main() {
    let nums = fs::read_to_string(
        "C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2021/_day-02/example.txt",
    )
    .unwrap();
    println!("{}", wow(&nums));
}
