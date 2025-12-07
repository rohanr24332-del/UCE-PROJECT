from models.config import get_responder
from utils.logger import log_line

class Reasoner:
    def __init__(self, memory=None):
        self.responder = get_responder()
        self.memory = memory

    def _build_prompt(self, step, context):
        ctx = ''
        if context:
            ctx = '\n\nRelevant memory:\n' + str(context)
        return f"You are an expert assistant. Solve the step: {step}.{ctx}\nAnswer concisely and include code where relevant."

    def solve(self, step: str, context=None):
        log_line('Reasoner: solving => ' + step[:120])
        prompt = self._build_prompt(step, context)
        return self.responder(prompt)
