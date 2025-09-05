#!/usr/bin/env python3

from pygments.lexer import RegexLexer, words, bygroups
from pygments.token import (
    Keyword,
    Name,
    String,
    Comment,
    Number,
    Operator,
    Punctuation,
    Whitespace,
    Text,
)


class RedyLexer(RegexLexer):
    name = "redy"
    aliases = ["ry"]
    filenames = ["*.ry"]
    mimetypes = ["text/x-redy"]

    keywords = {
        "fn",
        "mut",
        "const",
        "static",
        "extern",
        "if",
        "else",
        "match",
        "loop",
        "while",
        "for",
        "break",
        "continue",
        "ret",
        "struct",
        "enum",
        "trait",
        "impl",
        "mod",
        "pub",
        "true",
        "false",
        "async",
        "await",
        "fast",
        "unsafe",
        "this",
        "type",
        "typeof",
        "sizeof",
        "as",
    }

    types = {
        "i8",
        "i16",
        "i32",
        "i64",
        "i128",
        "isize",
        "u8",
        "u16",
        "u32",
        "u64",
        "u128",
        "usize",
        "f32",
        "f64",
        "bool",
        "char",
        "str",
        "String",
        "Vec",
        "Option",
        "Result",
        "Box",
        "void",
    }

    builtins = {
        "println#",
        "print#",
        "format#",
        "min",
        "max",
        "sqrt",
        "map",
        "filter",
        "Some",
        "None",
        "Ok",
        "Err",
    }

    tokens = {
        "root": [
            (r"\s+", Whitespace),
            # Comments
            (r"//.*?$", Comment.Single),
            (r"/\*.*?\*/", Comment.Multiline),
            (r"//@.*?$", Comment.Special),
            # String Literals
            (r'"(?:[^"\\]|\\.)*"', String.Double),
            (r"'(?:[^'\\]|\\.)'", String.Single),
            (r'r"[^"]*"', String),  # Raw string
            (r"r'[^']*'", String),  # Raw string
            # Character Literal
            (r"'(?:[^'\\]|\\.)''", String.Char),
            # Numeric Literal
            (r"0[xX][0-9a-fA-F]+[ulUL]*", Number.Hex),
            (r"0[oO][0-7]+[ulUL]*", Number.Oct),
            (r"0[bB][01]+[ulUL]*", Number.Bin),
            (r"\d+\.\d*([eE][+-]?\d+)?[fFlL]*", Number.Float),
            (r"\d+[eE][+-]?\d+[fFlL]*", Number.Float),
            (r"\d+[ulUL]*", Number.Integer),
            # Attribute
            (r"#\[.*?\]", Name.Attribute),
            # Macro Call
            (r"\w+#", Name.Function.Magic),
            # Function Definition
            (
                r"(fn)(\s+)([a-zA-Z_][a-zA-Z0-9_]*)",
                bygroups(Keyword, Whitespace, Name.Function),
            ),
            # Keywords
            (words(keywords, suffix=r"\b"), Keyword),
            (words(types, suffix=r"\b"), Keyword.Type),
            (words(builtins, suffix=r"\b"), Name.Builtin),
            # Function Call
            (
                r"([a-zA-Z_][a-zA-Z0-9_]*)(\s*)(\()",
                bygroups(Name.Function, Whitespace, Punctuation),
            ),
            # Operators
            (r"->", Operator),
            (r"=>", Operator),
            (r"<=>", Operator),
            (r"::", Operator),
            (r"\.\.\.|\.\.=?", Operator),
            (r"[+\-*/%=!<>&|^~]", Operator),
            (r"[+\-*/%]?=", Operator),
            (r"<<|>>", Operator),
            (r"&&|\|\|", Operator),
            (r"[+\-]?[+\-]", Operator),
            # Delimiters
            (r"[{}()\[\];,.]", Punctuation),
            (r":", Punctuation),
            (r"\?", Punctuation),
            # Type Name (PascalCase)
            (r"\b[A-Z][a-zA-Z0-9_]*\b", Name.Class),
            # Identifier
            (r"[a-zA-Z_][a-zA-Z0-9_]*", Name),
            # Other
            (r".", Text),
        ],
    }


def setup_lexer():
    from pygments.lexers import register

    register(RedyLexer)


if __name__ == "__main__":
    # for test
    code = """
fn main() {
    x := 42;
    println#("Hello, World!");

    if x > 0 {
        println#("Positive number: {}", x);
    } else {
        println#("Non-positive number");
    }

    // inline comment
    /* multi
       line comment
       testing */

    result := calculate(x, "test");
    ret result;
}

struct Point {
    x: f32,
    y: f32,
}

fn calculate(n: i32, s: &str) -> i32 {
    n * 2
}
"""

    from pygments import highlight
    from pygments.formatters import TerminalFormatter

    lexer = RedyLexer()
    formatter = TerminalFormatter()

    result = highlight(code, lexer, formatter)
    print(result)
