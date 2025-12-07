from models.config import get_responder
from utils.logger import log_line

class PlannerV2:
    def __init__(self):
        self.responder = get_responder()

    def create_plan(self, task: str):
        log_line('PlannerV2: creating plan...')
        if len(task.split()) < 10:
            return [task.strip()]
        prompt = f"Split the task into 3-5 concise ordered steps:\nTask: {task}\nPlan:"
        resp = self.responder(prompt)
        lines = [l.strip() for l in resp.splitlines() if l.strip()]
        plan = []
        import re
        for line in lines:
            s = re.sub(r'^[0-9]+[.)\-\s]*', '', line)
            if len(s) > 3:
                plan.append(s)
        if not plan:
            parts = [p.strip() for p in task.replace(';','.|').split('.') if p.strip()]
            plan = parts if parts else [task]
        log_line('Plan produced: ' + str(plan))
        return plan
