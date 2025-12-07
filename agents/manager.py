from agents.code_agent import CodeAgent
from agents.research_agent import ResearchAgent
from agents.critic_agent import CriticAgent
from utils.logger import log_line

class AgentManager:
    def __init__(self, reasoner, tools, memory):
        self.code = CodeAgent(reasoner, tools, memory)
        self.research = ResearchAgent(reasoner, tools, memory)
        self.critic = CriticAgent(reasoner, tools, memory)

    def handle_step(self, step: str):
        s = step.lower()
        if any(k in s for k in ('code','function','python','implement','script')):
            return self.code.handle(step)
        if any(k in s for k in ('explain','describe','why','how','summarize')):
            return self.research.handle(step)
        draft = self.research.handle(step)
        critique = self.critic.handle((step, draft))
        if 'issue' in critique.lower() or 'error' in critique.lower():
            improved = self.code.handle(step)
            return improved
        return draft
