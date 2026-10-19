import hashlib, json, time
class Block:
    def __init__(self, index, prev_hash, data):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = time.time()
        self.data = data
        self.hash = self.compute_hash()

    def compute_hash(self):
        s = f"{self.index}:{self.prev_hash}:{self.timestamp}{json.dumps(self.data)}"
        return hashlib.sha256(s.encode()).hexdigest()

class Chain:
    def __init__(self):
        self.blocks = [Block(0, "0", {"msg": "genesis"})]

    def add(self, data):
        b = Block(len(self.blocks), self.blocks[-1].hash, data)
        self.blocks.append(b)

if __name__ == "__main__":
    c = Chain()
    c.add({"from": "Alice", "to": "Bob", "amount": 5})
    for b in c.blocks:
        print(b.index, b.hash[:10])