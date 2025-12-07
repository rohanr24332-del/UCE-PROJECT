# UCE — Full Final Build
This is the final polished Unified Cognitive Engine starter.
Run demo: python main.py --demo
Run tests: python tests/test_smoke.py
Export KG dot: python -c "from tools.kg_visualizer import export_dot; import json; print(export_dot(json.load(open('data/kg_memory.json'))['nodes']))"
