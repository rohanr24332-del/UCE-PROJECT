from .context_compressor import compress
from utils.logger import log_line
def make_knowledge_chunk(task, plan, results):
    text = f'Task: {task}\nPlan: {plan}\n'
    for s,r in results:
        text += f'Step: {s}\nOutput: {str(r)[:300]}\n'
    chunk = compress(text, max_chars=800)
    log_line('Knowledge chunk created len=' + str(len(chunk)))
    return chunk
