defmodule Ex04MadLibs do
  @moduledoc """
  Given a madlib template, ask for the list of words to fill in,
  then print out the result with the template filled out.
  """




  @doc ~S"""
  Extract the words from the template.

  Template words are enclosed in braces, like:

      Now is the {noun} for all {adjective} {pluralnoun} to {verb}
      to the {noun} of their {noun}

  This would generate a list of atoms for the substitutions:

      [:noun, :adjective, :pluralnoun, :verb, :noun, :noun]

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




  @doc ~S"""
  Shoot the list of word-pairs from the Regex.scan in extract_words, and return the second part of the pair.

      iex> Ex04MadLibs.words([["a", "b"],["c", "d"], ["e", "f"]])
      ["b", "d", "f"]

      iex> Ex04MadLibs.words([])
      []
  """
  def words([]), do: []
  def words([head| tail]) do
    [second_part(head) | words(tail) ]
  end




  @doc ~S"""
  Returns the second part of a paired list

      iex> Ex04MadLibs.second_part(["first", "second"])
      "second"
  """
  def second_part(pair), do: hd(tl(pair))




  @doc ~S"""
  Convert a list of strings to atoms (symbols).

  ## Examples

      iex> Ex04MadLibs.atomize(["a", "b", "c"])
      [:a, :b, :c]

      iex> Ex04MadLibs.atomize([])
      []
  """
  def atomize([]), do: []
  def atomize([head | tail]) do
    [String.to_atom(head) | atomize(tail) ]
  end



  @doc ~S"""
  Given the template and a list of words, fill in the corresponding word slots in the template with the words in the same order.


  ## Examples

      iex> Ex04MadLibs.solver("Now {pronoun} have a {food}", ["we", "pizza"])
      "Now we have a pizza"


  """
  def solver('', []), do: ''
  def solver(template, words) do
    String.split(template)
    |> replacer(words)
    |> Enum.join(" ")
  end




  @doc ~S"""
  Given a list of words from the template and a list of replacement words,
  shoot the template list, substituting the first word in the list and pop
  it off the replacement words list.

  ## Examples

      iex> Ex04MadLibs.replacer(["Now", "{pronoun}", "have", "a", "{food}"], ["we", "pizza"])
      ["Now", "we", "have", "a", "pizza"]

      iex> Ex04MadLibs.replacer(["Now", "{pronoun}", "have", "a", "{food}"], ["we"])
      ["Now", "we", "have", "a", "pizza"]

      iex> Ex04MadLibs.replacer(["Now", "{pronoun}", "have", "a", "{food}"], [])
      ["Now", "we", "have", "a", "pizza"]


  """
  def replacer([], []), do: []
  def replacer([head | tail], words) do
    if Regex.match?(~r/\{(.*?)\}/, head) do
      [ hd(words) | replacer(tail, tl(words)) ]
    else
      [ head | replacer(tail, words)]
    end
  end

end
