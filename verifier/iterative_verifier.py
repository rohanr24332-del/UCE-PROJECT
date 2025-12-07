from models.config import get_responder
from utils.logger import log_line, log_section
import re

class IterativeVerifier:
    def __init__(self, reasoner, max_rounds=2):
        self.reasoner = reasoner
        self.responder = get_responder()
        self.max_rounds = max_rounds

    def verify_and_fix(self, step_results):
        combined = '\n\n'.join([f'STEP: {s}\nOUTPUT:\n{r}' for s,r in step_results])
        prompt = 'You are a verifier. If everything is correct reply VERIFIED. Otherwise reply ISSUE and mention step numbers needing fixes.'
        resp = self.responder(prompt + '\n\n' + combined)
        log_line('Verifier reply: ' + resp.split('\n')[0][:200])
        if 'VERIFIED' in resp.upper():
            return True, step_results
        # find step indices
        fixes = [int(m.group(1))-1 for m in re.finditer(r'step\s*(\d+)', resp.lower())]
        patched = list(step_results)
        rounds = 0
        while fixes and rounds < self.max_rounds:
            for idx in fixes:
                s, old = step_results[idx]
                log_section(f'Iterative fix: re-solving step {idx+1}')
                new = self.reasoner.solve(s, context=None)
                patched[idx] = (s, new)
            rounds += 1
            combined = '\n\n'.join([f'STEP: {s}\nOUTPUT:\n{r}' for s,r in patched])
            resp = self.responder('Verify after fixes:\n' + combined)
            if 'VERIFIED' in resp.upper():
                return True, patched
            fixes = [int(m.group(1))-1 for m in re.finditer(r'step\s*(\d+)', resp.lower())]
        return ('VERIFIED' in resp.upper()), patched
