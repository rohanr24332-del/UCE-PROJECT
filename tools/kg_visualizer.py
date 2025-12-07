import os
from utils.logger import log_line
def export_dot(nodes, path=None):
    if path is None:
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'kg_graph.dot'))
    try:
        with open(path, 'w') as f:
            f.write('digraph UCE_KG {\n')
            for k in nodes.keys():
                lab = k.replace('"','\\"')[:40]
                f.write(f'  "{lab}" [shape=box];\n')
            f.write('}\n')
        log_line('Exported DOT to ' + path)
        return path
    except Exception as e:
        log_line('Export failed: ' + str(e))
        return None
