# Introduction

> This project is a work in progress and cannot yet compile a **Hello World** program.


## Overview

**redy** is a new programming language to achieve both high performance and robust safety.

It emphasizes performance in all aspects, including reducing computation, memory usage, and improving the cache hit rate, as well as minimizing the size of compiled binaries, which is often overlooked in an era of abundant computing resources.

---

## Features

> Most features have not yet been implemented, but the design is fully defined.

### Complete Memory Safety

**redy** uses an ownership system inspired by Rust. All heap memory is automatically freed when it goes out of scope, completely preventing memory leaks.

### Zero-Cost Access Control

All potential illegal memory access is detected at compile time, eliminating runtime overhead. Say goodbye to segmentation faults!

### Blazing Fast

Runtime costs, such as boundary checks, are minimized through various compile-time analysis methods to achieve the **best possible performance**.

### No Lifetime Annotation Required

The compiler uses **Control Flow Graph(CFG)** and **Static Single Assignment(SSA)** to do **Non-Lexical Constraint-Based Lifetime Checking**. This system is more flexible than Rust's while remaining safe. If the lifetime relationships are intuitive, the compiler can often infer them without requiring explicit annotations.


## Quick Start

### Install redy

There are two ways to install redy:
  1. Install a pre-built binary (recommended).
  2. Build from source.

Detailed instructions are available in the [installation guide](install.md).

### Start Coding

We use `.ry` as the extension for source files.
To get started, let's create an empty directory and file `main.ry`, then open `main.ry` in any text editor.

Now we're ready, let's go to [Hello World](tutorials/0001_helloworld.md) and write your first program.
