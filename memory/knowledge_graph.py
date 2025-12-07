import json, os
from utils.logger import log_line
BASE = os.path.dirname(__file__)
MEM = os.path.abspath(os.path.join(BASE, '..', 'data', 'kg_memory.json'))

class KnowledgeGraphMemory:
    def __init__(self):
        os.makedirs(os.path.dirname(MEM), exist_ok=True)
        if not os.path.exists(MEM):
            with open(MEM, 'w') as f:
                json.dump({'nodes':{}, 'tasks':{}}, f)
        self._load()

    def _load(self):
        try:
            with open(MEM, 'r') as f:
                data = json.load(f)
        except:
            data = {'nodes':{}, 'tasks':{}}
        self.nodes = data.get('nodes', {})
        self.tasks = data.get('tasks', {})

    def _save(self):
        with open(MEM, 'w') as f:
            json.dump({'nodes': self.nodes, 'tasks': self.tasks}, f, indent=2)

    def store_task(self, task, plan, results, verified):
        self.tasks[task] = {'plan': plan, 'results': results, 'verified': verified}
        for step, res in results:
            key = step[:60]
            self.nodes.setdefault(key, {})['example'] = str(res)[:400]
        self._save()
        log_line('KGMemory: stored task.')

    def search_related(self, query):
        q = set(query.lower().split())
        related = {}
        for k,v in self.nodes.items():
            if any(tok in k.lower() for tok in q):
                related[k] = v
        return related
