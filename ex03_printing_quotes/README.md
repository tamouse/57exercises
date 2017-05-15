# QUOTING

Quotation marks are often used to denote the start and end of a
string. But sometimes we need to print out the quotation marks
themselves by using escape characters. Create a program that prompts
for a quote and an author. Display the quotation and author as shown
in the example output.

> Excerpt From: Brian P. Hogan. “Exercises for Programmers (for Tamara Temple).” iBooks.

## Installation

If [available in Hex](https://hex.pm/docs/publish), the package can be installed
by adding `ex03_printing_quotes` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [{:ex03_printing_quotes, "~> 0.1.0"}]
end
```

Documentation can be generated with [ExDoc](https://github.com/elixir-lang/ex_doc)
and published on [HexDocs](https://hexdocs.pm). Once published, the docs can
be found at [https://hexdocs.pm/ex03_printing_quotes](https://hexdocs.pm/ex03_printing_quotes).

## Startup

    mix new ex03_printing_quotes --module QUOTING
    cd ex03_printing_quotes
    mix test

## Cleanup

Remove the sample test.
