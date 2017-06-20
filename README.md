Working through Brian Hogan's _Exercises for Programmers: 57
Challenges to Develop Your Coding Skills_

Branches are for working in a different language, for example, the
`python3` branch for working with Python 3.x.


**This** branch is for Elixir.


## Elixir stuff

### Making a new project

Creating a new elixir project:

    mix new PROJECT_NAME

Write your code in the `lib/PROJECT_NAME.ex` file.

Embed your unit tests into the code itself with `@doc` tests:

```elixir
defmodule MyModule do
  @moduledoc """
  Documentation for MyModule.
  """

  @doc """
  MyModule does stuff...

  ## Examples

      iex> MyModule.do_something("hi", "there")
      "hi there"
  """
  def do_something(s1, s2) do
    s1 <> " " <> s2
  end
end

```

### Testing

USE DOCTESTS OMGOMGOMGWTFBBQ!!!!

In `./test/` create a file to match your code file(s) that contains:

```elixir
defModule MyModuleTest do
  use ExUnit.Case
  doctest MyModule
end
```

Also, create a file called `./test/test_helper.exs` that contains:

```elixir
ExUnit.start()
```

When you want to run the tests, from the root of the project:

    $ mix test

should do it.

### Making a runner

Make a mix task to make running the program easier:

    touch lib/mix/tasks/task_name.ex

A task looks something like this:

```elixir
defmodule Mix.Tasks.TaskName do

  @moduledoc """
  Run MyModule's do_something method
  """

  use Mix.Task

  def run(_) do
    s1 = String.trim(IO.gets("enter the first string: "))
    s2 = String.trim(IO.gets("enter the second string: "))
    IO.puts(MyModule.do_something(s1, s2))
  end
end
```

Then run with:

    $ mix task_name

See `ex03_printing_quotes/lib/mix/tasks/quoter.ex` for a neat example
with IO to the console.
