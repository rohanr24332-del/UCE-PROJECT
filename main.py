from orchestrator.orchestrator import Orchestrator
from utils.logger import log_header
import argparse, os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--api", action="store_true")
    args = parser.parse_args()
    if args.api:
        os.environ['USE_OPENAI'] = '1'
    log_header("UCE — Full Final Build")
    engine = Orchestrator(full_mode=True)
    if args.demo:
        demo = [
            "Write a python function to check prime numbers and include simple tests.",
            "Explain how airplanes fly in 4 steps."
        ]
        for t in demo:
            print("\n>>> DEMO TASK:", t)
            print(engine.run(t))
        return
    while True:
        try:
            task = input("\nEnter task: ").strip()
        except (KeyboardInterrupt, EOFError):
            print('\nGoodbye!'); break
        if not task: continue
        if task.lower() in ('exit','quit'): break
        out = engine.run(task)
        print("\n=== FINAL OUTPUT ===\n", out)

if __name__ == '__main__':
    main()
