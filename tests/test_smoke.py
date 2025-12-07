from orchestrator.orchestrator import Orchestrator
def test_smoke():
    eng = Orchestrator(full_mode=False)
    out = eng.run('Find the longest word in this sentence: Artificial intelligence will change everything.')
    assert 'intelligence' in out.lower()
if __name__ == '__main__':
    test_smoke(); print('SMOKE OK')
