from agents.base import AgentBase
from utils.logger import log_line

class CriticAgent(AgentBase):
    def handle(self, task):
        log_line('CriticAgent: critiquing...')
        if isinstance(task, tuple):
            step, draft = task
            prompt = f'Review draft for step: {step}\nDraft:\n{draft}\nProvide one-line issues if any.'
        else:
            prompt = f'Review: {task}\nOne-line issues if any.'
        return self.reasoner.solve(prompt, context=self.memory.search_related(task if not isinstance(task, tuple) else task[0]))
