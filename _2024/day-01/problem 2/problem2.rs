use std::fs;

fn main(){
    let data: String = fs::read_to_string("C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC24/day-01/problem 2/input.txt").expect("no file found");
    let mut list1: Vec<i32> = Vec::new();
    let mut list2: Vec<i32> = Vec::new();

    for line in data.lines(){
        let temp: Vec<&str> = line.split("   ").collect();
        list1.push(temp[0].parse().unwrap());
        list2.push(temp[1].parse().unwrap());
    }
    
    let mut counter_list: Vec<i32> = Vec::new();
    for _ in 0..*list1.iter().max().unwrap() as usize {
        counter_list.push(0);
    }

    for i in list2{
        counter_list[i as usize]+=1;
    }

    let mut final_list: Vec<i32> = Vec::new();
    for i in 0..list1.len()-1{
        if list1[i] < counter_list.len() as i32 {
            final_list.push(list1[i]*counter_list[list1[i] as usize]);
        }
    }

    println!("{}",final_list.iter().sum::<i32>());
}