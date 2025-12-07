from agents.base import AgentBase
from utils.logger import log_line

class CodeAgent(AgentBase):
    def handle(self, task):
        log_line('CodeAgent: generating code...')
        prompt = f'Write production-ready Python code for: {task}\nInclude simple tests.'
        return self.reasoner.solve(prompt, context=self.memory.search_related(task))
