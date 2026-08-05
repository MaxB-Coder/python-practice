# python-practice

Building Python fluency deliberately, coming from a Java and JavaScript background.

I work mostly in Java, Spring and React. Rather than picking Python up by osmosis,
I'm working through it week by week — small, self-contained exercises and tools,
written by hand.

## Structure

- `week-1/` — fundamentals: syntax, data structures, and finding my way around the standard library
- `week-2/todo-cli/` — a command-line todo application

## Tooling

Pre-commit hooks run black and ruff on every commit, so formatting and linting are
enforced rather than remembered.

## Coming from Java

Notes on what's actually different, rather than what the tutorials say:

- **Type hints aren't a compiler.** They look like static typing but nothing enforces
  them at runtime. The safety net I'd taken for granted is a linting step here, not a
  guarantee.
- **Duck typing instead of interfaces.** You never declare what you implement, so the
  contract lives in tests and documentation rather than in the type system.

## Where this is going

Being able to write, test and deploy a small service in Python with the same confidence
I'd have doing it in Spring Boot.
