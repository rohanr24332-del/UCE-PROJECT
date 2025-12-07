import subprocess, tempfile, os, sys
from utils.logger import log_line

class ToolExecutor:
    def __init__(self): pass
    def run_python(self, code: str, timeout=5):
        try:
            with tempfile.TemporaryDirectory() as d:
                path = os.path.join(d, 'ucetemp.py')
                with open(path, 'w') as f:
                    f.write(code)
                proc = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=timeout)
                out = proc.stdout or proc.stderr
                return True, out
        except Exception as e:
            return False, str(e)
