defmodule Quoting do
  @moduledoc """
  Documentation for Quoting.
  """

  @doc """
  Formatting quotes

  ## Examples

      iex> Quoting.format("These aren't the droids you're looking for.", "Obi Wan Kenobi")
      "Obi Wan Kenobi said: \\"These aren't the droids you're looking for.\\""


  """
  def format(quote, author) do
    author <> " said: " <> "\"" <> quote <> "\""
  end
end
