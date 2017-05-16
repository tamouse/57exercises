defmodule Mix.Tasks.Quoter do

  @moduledoc """

  Ask the user for a quotation and the author, and print
  the formatted quote.

  Run with `mix quoter`

  Set the default task to 'quoter' in ./mix.exs

  """

  use Mix.Task

  def run(_) do
    quotation = String.trim(IO.gets("What is the quote? "))
    author = String.trim(IO.gets("Who said it? "))
    # call the module method
    IO.puts(Quoting.format(quotation, author))
  end

end
