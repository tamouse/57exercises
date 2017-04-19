
# It's imporant that this is located where it is!


defmodule Mix.Tasks.Counter do
  use Mix.Task

  def run(_) do
    string = String.trim(IO.gets("Enter a string: "))
    num_chars = Ex02CountingCharacters.count(string)
    IO.puts("There were #{num_chars} characters in #{string}")
  end
end
