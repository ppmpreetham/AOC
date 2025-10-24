use std::fs;

fn gaint_squid(board: &str) -> i32 {
    let boards = board.split::<&str>("\r\n\r\n").collect::<Vec<&str>>();
    let nums = boards[0].split(',').collect::<Vec<&str>>();
    let actual_boards = boards[1..]
        .iter()
        .map(|b| {
            b.lines()
                .map(|l| {
                    l.split_whitespace()
                        .map(|n| n.parse::<i32>().unwrap())
                        .collect::<Vec<i32>>()
                })
                .collect::<Vec<Vec<i32>>>()
        })
        .collect::<Vec<Vec<Vec<i32>>>>();
    println!("{:?}", nums);
    println!("{:?}", actual_boards);
    
    // bingo logic
    let mut winners = Vec::new();
    1
}

fn main() {
    let board = fs::read_to_string(
        "C:/Users/ppmpr/OneDrive/Documents/GitHub/AOC/_2021/_day-04/example.txt",
    )
    .unwrap();
    gaint_squid(&board);
}
