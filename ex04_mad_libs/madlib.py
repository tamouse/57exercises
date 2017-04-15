
class MadLib:
    def __init__(self, prompts, template):
        self.prompts = prompts
        self.template = template
        self.prompts_iter=iter(prompts)

    def next_prompt(self):
        return next(self.prompts_iter)

    def render(self, words):
        return self.template.format(**words)
