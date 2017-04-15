"""
“Quotation marks are often used to denote the start and end of a string. But sometimes we need to print out the quotation marks themselves by using escape characters.

Create a program that prompts for a quote and an author. Display the quotation and author as shown in the example output.”

Excerpt From: Brian P. Hogan. “Exercises for Programmers (for Tamara Temple).” iBooks.
"""


def format_quote(quote, cite):
    return '{cite} said: "{quote}"'.format(cite=cite, quote=quote)
