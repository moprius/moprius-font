# Contributing

Bug reports and improvements are welcome.

When reporting a glyph issue, include:

1. Family and style.
2. Character or Unicode code point.
3. Application, operating system and rendering size.
4. Screenshot and a short explanation of the expected result.

Before submitting changes, run:

```bash
python tools/build.py
python tools/audit.py
```

All font modifications must remain compatible with the SIL Open Font License 1.1 and must not introduce a Reserved Font Name as a public family name.
