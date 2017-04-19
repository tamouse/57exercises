defmodule Ex02CountingCharacters do
  @moduledoc """
  Documentation for Ex02CountingCharacters.
  """

  @doc """
  Counting characters

  ## Examples

      iex> Ex02CountingCharacters.count("aeiou")
      5

  """
  def count(str) do
    String.length(str)
  end

end
