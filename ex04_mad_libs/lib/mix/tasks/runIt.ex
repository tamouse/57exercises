defmodule Mix.Tasks.RunIt do

  @moduledoc """
  Run the program
  """

  use Mix.Task

  def run(_) do
    template = "Enter the template with keywords in braces: "
    |> IO.gets

    answers = Ex04MadLibs.extract_words(template)
    |> responses

    Ex04MadLibs.solver(template, answers)
    |> IO.puts
  end

  def responses(words) do
    Enum.map(words, fn(word) -> "Give me a #{word}: " |> IO.gets |> String.trim end)
  end
end
