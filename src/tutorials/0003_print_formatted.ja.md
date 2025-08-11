# フォーマット

フォーマットされた文字列を表示してみましょう:

```redy
fn main() {
  n := 5
  println#("3足す2の和は{}", n)
}
```

```bash
redy main.ry
# Compiling... : main.ry
# Completed!   : main.ry

./out/main
# 3足す2の和は5
```

数字が表示できましたね
見ての通り、`n`という変数に格納された値がフォーマットされて表示できました。<br/>
このように、`println#()`には複数の引数を渡すことができます<br/>
最初の引数は`format string`と呼ばれ、それ以外の引数は全て`format args`と呼ばれます。
`format string`の内部にあるすべてのブラケット(`{}`)は、出てきた順番に`format args`の値に置き換えられていきます
