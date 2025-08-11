from collections import defaultdict

# Sample data
data = ["hello world", "hello big data", "hello map reduce"]

# --- MAP PHASE ---
mapped = []
for line in data:
    for word in line.strip().split():
        mapped.append((word, 1))  # emit (key, value)

# --- SHUFFLE PHASE ---
shuffle = defaultdict(list)
for key, value in mapped:
    shuffle[key].append(value)

# --- REDUCE PHASE ---
reduced = {}
for key in shuffle:
    reduced[key] = sum(shuffle[key])

print(reduced)
