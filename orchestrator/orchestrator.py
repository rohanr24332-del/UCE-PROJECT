from planner.planner_v2 import PlannerV2
from reasoner.reasoner import Reasoner
from verifier.iterative_verifier import IterativeVerifier
from memory.knowledge_graph import KnowledgeGraphMemory
from agents.manager import AgentManager
from tools.tool_executor import ToolExecutor
from utils.logger import log_section, log_line

class Orchestrator:
    def __init__(self, full_mode=False):
        self.full_mode = full_mode
        self.planner = PlannerV2()
        self.memory = KnowledgeGraphMemory()
        self.reasoner = Reasoner(memory=self.memory)
        self.verifier = IterativeVerifier(self.reasoner)
        self.tools = ToolExecutor()
        self.agents = AgentManager(self.reasoner, self.tools, self.memory) if full_mode else None

    def run(self, task: str) -> str:
        log_section('ORCHESTRATOR')
        log_line('Received task: ' + task)
        plan = self.planner.create_plan(task)
        step_results = []
        if self.full_mode and self.agents:
            for i, step in enumerate(plan, 1):
                res = self.agents.handle_step(step)
                step_results.append((step, res))
        else:
            for i, step in enumerate(plan, 1):
                log_section(f'REASONER - Step {i}')
                res = self.reasoner.solve(step, context=self.memory.search_related(step))
                step_results.append((step, res))
        log_section('VERIFIER')
        verified, patched = self.verifier.verify_and_fix(step_results)
        self.memory.store_task(task, plan, patched, verified)
        final = '\n\n'.join([f'[STEP] {s}\n{r}' for s,r in patched])
        final += '\n\n[VERIFIED] ' + ('YES' if verified else 'NO')
        return final
