
from ex04_mad_libs.madlib import MadLib

prompts = input("Enter a space-separated list of one-word prompts: ").split()
template = input("Enter a madlib template: ")
madlib = MadLib(prompts, template)

words = {}
for prompt in madlib.prompts_iter:
    words[prompt] = input("Enter a {prompt}: ".format(prompt=prompt))

print(madlib.render(words))
