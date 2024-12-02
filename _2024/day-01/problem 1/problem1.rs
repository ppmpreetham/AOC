use std::fs;

fn main() {
    let data: String = fs::read_to_string("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC24/day-01/problem 1/input.txt").expect("Error reading file");
    let mut list1: Vec<i32> = Vec::new();
    let mut list2: Vec<i32> = Vec::new();
    
    for i in data.split("\n") {
        let temp: Vec<&str> = i.trim().split("   ").collect();
        if temp.len() == 2 {
            list1.push(temp[0].parse().unwrap());
            list2.push(temp[1].parse().unwrap());
        }
    }

    list1.sort();
    list2.sort();

    let mut new_lst : Vec<i32> = Vec::new();
    for i in 0..list1.len() {
        new_lst.push(i32::abs(list1[i] - list2[i]));
    }

    println!("{}", new_lst.iter().sum::<i32>());
}