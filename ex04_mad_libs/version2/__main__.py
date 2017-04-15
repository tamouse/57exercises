
from ex04_mad_libs.version2.madlib import MadLib

template = input("Give me a template: ")
madlib = MadLib(template)

words = {}
for prompt in madlib.prompts():
    words[prompt] = input("Give me a {prompt}: ".format(prompt=prompt))

print(madlib.render(words))
