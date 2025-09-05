hljs.registerLanguage('redy', function (hljs) {
  return {
    name: 'Redy',
    keywords: {
      keyword:
        'fn struct enum union match if else loop while for break continue ret mut const pub extern unsafe impl trait',
      literal:
        'true false null',
      type:
        'i8 i16 i32 i64 u8 u16 u32 u64 f32 f64 bool char str void',
    },
    contains: [
      hljs.C_LINE_COMMENT_MODE,
      hljs.C_BLOCK_COMMENT_MODE,
      hljs.QUOTE_STRING_MODE,
      hljs.NUMBER_MODE,
      {
        className: 'function',
        begin: /[a-zA-Z_][a-zA-Z0-9_]*#/,
      },
    ],
  };
});
