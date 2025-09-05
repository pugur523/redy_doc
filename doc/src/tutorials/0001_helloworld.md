# Hello World!

This is **Hello World** program in **redy**. Try pasting it to your `main.ry`.

```redy
fn main() {
  println#("Hello World from redy!")
}
```

To run this program, you need to "compile" the program first, so run the command below, then the executable binary will be generated in `./out/`
```bash
redy main.ry
# Compiling... : main.ry
# Completed!   : main.ry
```

Now let's run our first redy program!

```bash
./out/main
# Hello World from redy!
```

When you run the executable, it prints the string "Hello World" as standard output, as we can see in the console.

# How the Hello World Program Works

What does that hello world program mean is very simple to understand, let's go through it line by line.

> `fn main() {`

The first line means that "**We will declare `function`(`fn`) named `main`**", and "**Start defining the content of the function(`{`)**".  
`function` in programming means typically something like a collection of processes.

> `println#("Hello, World from redy!")`

The next line is also simple, calling function* named `println#()` with argument `"Hello, World from redy!"`. `println#()` is provided function* that **print**s **l**i**n**e to the console, and we called it with single string argument. the characters surrounded by double quotation are considered as `literal string`, a set of the characters that can be handled at a time.

Note that `println#()` is not a function actually, but it's a bit complicated to explain why now, so we'll come back to that later, just consider it as a function.  

> `}`

The last line is the simplest one, that means "**End defining this function**",
and the program ends here, so we created the functional program in only 3 lines!
