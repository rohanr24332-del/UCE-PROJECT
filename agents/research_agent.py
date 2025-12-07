from agents.base import AgentBase
from utils.logger import log_line

class ResearchAgent(AgentBase):
    def handle(self, task):
        log_line('ResearchAgent: research...')
        prompt = f'Explain concisely: {task}.'
        return self.reasoner.solve(prompt, context=self.memory.search_related(task))
