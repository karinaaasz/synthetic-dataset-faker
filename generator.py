import random
def fake_records(n=10): return [{'id': i, 'val': round(random.random(), 4)} for i in range(n)]
