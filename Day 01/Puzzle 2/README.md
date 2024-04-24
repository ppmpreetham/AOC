# Day 1: Trebuchet?!
## Puzzle-2
## Explanation
I have used the same Two Pointer approach. But this time, I have cheated a bit. 

I tried to map each numeric words to it's corresponding number, (i.e):
```python
mapping={
"one":"1",
"two":"2",
"three":"3",
"four":"4",
"five":"5",
"six":"6",
"seven":"7",
"eight":"8",
"nine":"9"
}
```
But, it didn't work out quite well. It converted `eightwothree` into `eigh23`, since it replaces `two` first and then `eight`, while I was looping through the dictionary.  I then realized that the first and the last letters of each numeric word would probably accompany for the next one. So, I tried to hide the letter inside each word and remove them at the end.
That would convert `eightwothree`into `eig8ht2woth3re`. 

I then mapped all of them like this:
```python
mapping={
"one":"o1ne",
"two":"t2wo",
"three":"th3re",
"four":"fo4ur",
"five":"fi5ve",
"six":"si6x",
"seven":"sev7en",
"eight":"ei8ght",
"nine":"ni9ne"
}
```

Now I can just use the previous Two Pointer technique I've used in the Puzzle-1.

My puzzle answer was  `53080`.

## Question
Your calculation isn't quite right. It looks like some of the digits are actually  _spelled out with letters_:  `one`,  `two`,  `three`,  `four`,  `five`,  `six`,  `seven`,  `eight`, and  `nine`  _also_  count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

In this example, the calibration values are  `29`,  `83`,  `13`,  `24`,  `42`,  `14`, and  `76`. Adding these together produces  `281`.

_What is the sum of all of the calibration values?_

Your puzzle answer was  `53268`.
