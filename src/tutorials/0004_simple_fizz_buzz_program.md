# Simple Fizz Buzz Program

> The FizzBuzz program is a common coding challenge used to assess basic programming skills.
> The program iterates through a sequence of numbers, typically from 1 to 100.
> For each number, it checks for divisibility by 3 and 5.
> If a number is divisible by 3, it prints "Fizz".
> If it's divisible by 5, it prints "Buzz".
> If it's divisible by both 3 and 5, it prints "FizzBuzz".
> If none of the conditions are met, it prints the number itself.

Now, let's try to write the FizzBuzz program in **redy**.

```redy
fn main() {
  for i: 1..=100 {
    if i % 15 == 0 {
      println#("FizzBuzz")
    } else if i % 3 == 0 {
      println#("Fizz")
    } else if i % 5 == 0 {
      println#("Buzz")
    } else {
      println#("{}", i)
    }
  }
}
```

If you run this code, you will get the FizzBuzz output from 1 to 100. Let's understand what's going on here.

The first line `for i: 1..=100 { ... }` creates a **loop** that iterates a number `i` from `1` to `100` (inclusive). The code inside the curly braces `{ ... }` will be executed for each number.

Inside the loop, we use `if...else if...else` statements, which are used to execute different code blocks based on conditions.

  - `i % 15 == 0`: This condition checks if the number `i` is perfectly divisible by 15. The `%` operator calculates the remainder of a division. If the remainder is `0`, it means `i` is a multiple of 15.
  - `i % 3 == 0` and `i % 5 == 0`: These conditions check for divisibility by 3 and 5, respectively.
  - `else { println#("{}", i) }`: If none of the above conditions are true, the program executes the code in this block, simply printing the number itself.

Notice that the condition `i % 15 == 0` comes first. This is because a number divisible by 15 is also divisible by 3 and 5. If we checked for `i % 3 == 0` first, it would print "Fizz" and then move on, never reaching the "FizzBuzz" condition.
