class AgentBase:
    def __init__(self, reasoner, tools, memory):
        self.reasoner = reasoner
        self.tools = tools
        self.memory = memory
    def handle(self, task):
        raise NotImplementedError
