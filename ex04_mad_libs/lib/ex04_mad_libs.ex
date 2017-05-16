defmodule Ex04MadLibs do
  @moduledoc """
  Given a madlib template, ask for the list of words to fill in,
  then print out the result with the template filled out.
  """

  @doc """
  Extract the words from the template.

  Template words are enclosed in braces, like:

      Now is the {noun} for all {adjective} {pluralnoun} to {verb}
      to the {noun} of their {noun}

  This would generate a list:

      [noun, adjective, pluralnoun, verb, noun, noun]

  ## Examples

      iex> Ex04MadLibs.extract_words("Now is the {noun} for all {adjective} {pluralnoun} to {verb}  to the {noun} of their {noun}")
      [:noun, :adjective, :pluralnoun, :verb, :noun, :noun]

  """
  def extract_words(template) do
    ~r/\{(.*?)\}/
    |> Regex.scan(template)
    |> words
    |> atomize
  end

  @doc """
      iex> Ex04MadLibs.words([["a", "b"],["c", "d"], ["e", "f"]])
      ["b", "d", "f"]

      iex> Ex04MadLibs.words([])
      []
  """
  def words([]), do: []
  def words([head| tail]) do
    [second_part(head) | words(tail) ]
  end

  @doc """
      iex> Ex04MadLibs.second_part(["first", "second"])
      "second"
  """
  def second_part(pair), do: hd(tl(pair))

  @doc """
      iex> Ex04MadLibs.atomize(["a", "b", "c"])
      [:a, :b, :c]

      iex> Ex04MadLibs.atomize([])
      []
  """
  def atomize([]), do: []
  def atomize([head | tail]) do
    [String.to_atom(head) | atomize(tail) ]
  end

end
