# Ex04MadLibs

Mad libs are a simple game where you create a story template with
blanks for words. You, or another player, then construct a list of
words and place them into the story, creating an often silly or funny
story as a result.

Create a simple mad-lib program that prompts for a noun, a verb, an
adverb, and an adjective and injects those into a story that you
create.

Excerpt From: Brian P. Hogan. "Exercises for Programmers (for Tamara
Temple)." iBooks.


## Learning:

### Taking the head of the tail of a list:

```elixir
hd(tl(list))
```

- `hd` and `tl` are part of the standard List Functions in Elixir

### Mapping functions to work on a list:

Need two methods, one to match the empty list, and one to match the
head and tail (car and cdr).

```elixir
  def mthd([]), do: []
  def mthd([head|tail]), do: [process(head) | mthd(tail)]
```

### Convert a string to an atom, aka symbol:

```elixir
iex> String.to_atom("s")
:s
```

### Regexes

Regex expressions start with `~r` : "tilde - arr"
