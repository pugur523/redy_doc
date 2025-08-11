Now that you've written some basic programs in **redy**, let's dive a little deeper into the fundamental building blocks of **redy**: **data types** and **variables**.

# Data Types

A **data type** tells the compiler what kind of data a value holds. **redy** has several built-in data types, just like other programming languages.

  - **Integers (`i32`, `i64`, `u32`, etc.):** Whole numbers without a fractional part. The letters `i` and `u` stand for "signed" and "unsigned" respectively, and the number (e.g., `32`) indicates the number of bits used to store the value.
  - **Booleans (`bool`):** A value that can only be either `true` or `false`.
  - **Strings (`str`):** A sequence of characters.

There are many more data types in **redy**, but we will stick to these for now.

# Variables

A **variable** is a named storage location for a value. In **redy**, you can declare a variable assign a value to it using `:=`.

```redy
fn main() {
  my_number := 42            // An integer variable
  is_active := true          // A boolean variable
  greeting := "Hello, redy!" // A string variable
 
  println#("The number is {}", my_number)
  println#("Is active? {}", is_active)
  println#("Greeting: {}", greeting)
}
```

Once you compile and run this program, it will print out the values of these variables.<br/>
Notice that **redy** can often **infer** the data type of a variable without you explicitly writing it, which makes your code cleaner.
