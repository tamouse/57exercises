import re

class MadLib:
    def __init__(self, template):
        self.template = template
        self._prompts = None

    def prompts(self):
        return re.findall('\{(.*?)\}', self.template)

    def prompts_iter(self):
        if self._prompts == None:
            self._prompts = iter(self.prompts())

        return self._prompts

    def render(self, words):
        return self.template.format(**words)
