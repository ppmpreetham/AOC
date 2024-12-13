import Data.List (sort)

main :: IO ()
main = do
    contents <- readFile "input.txt"
    let linesOfFile = lines contents
        (list1, list2) = unzip [ (read x :: Int, read y :: Int) | line <- linesOfFile, let parts = words line, let x = head parts, let y = parts !! 1 ]
        sortedList1 = sort list1
        sortedList2 = sort list2
        newList = zipWith (\x y -> abs (x - y)) sortedList1 sortedList2
    print (sum newList)