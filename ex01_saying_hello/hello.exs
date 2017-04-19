# Write a program to ask the user their name, and then print a greeting.

defmodule HelloWorld do
  def hello(name) do

    # "String concatenation is done with <>" from http://elixir-lang.org/getting-started/basic-operators.html

    # Additionally, the String.trim/1 method removes the whitespace
    # surrounding the string, *MOST NOTABLY* the newline that is
    # included in the IO.gets/1 method

    "Hello, " <> String.trim(name) <> "!"

    # There is another way to concatenate strings as well, using
    # Enum.join():
    #
    #     Enum.join(["Hello, ", String.trim(name), "!"])
    #
    # does the same as above

  end
end

# Basic read from user and print on stdout
name = IO.gets(" enter your name: ")
IO.puts(HelloWorld.hello(name))
