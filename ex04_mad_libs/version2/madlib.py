import re

class MadLib:
    def __init__(self, template):
        self.template = template

    def prompts(self):
        return list(set(re.findall('\{(.*?)\}', self.template)))

    def render(self, words):
        return self.template.format(**words)

    def next_prompt(self):
        for prompt in self.prompts():
            yield prompt
