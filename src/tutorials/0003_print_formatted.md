# Print Formatted

Let's print a formatted string:

```redy
fn main() {
  n := 5
  println#("3 + 2 is {}", n)
}
```

```bash
redy main.ry
# Compiling... : main.ry
# Completed!   : main.ry

./out/main
# 3 + 2 is 5
```

As you can see, we finally printed a value stored in `n`!<br/>
Actually, `println#()` can be passed multiple arguments.<br/>
the first argument is called `format string`, and the arguments remaining after that are called `format args`.
All brackets(`{}`) contained in the `format string` will be replaced by the `format args`.
