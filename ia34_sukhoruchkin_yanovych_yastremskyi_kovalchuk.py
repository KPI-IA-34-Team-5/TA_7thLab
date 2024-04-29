class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def fnv_hash(self, key):
        FNV_prime = 0x01000193
        hash = 0x811c9dc5
        for byte in key.encode('utf-8'):
            hash ^= byte
            hash = (hash * FNV_prime) % (2 ** 32)
        return hash % self.size
    
    def insert(self, key, value):
        index = self.fnv_hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])
    
    def search(self, key):
        index = self.fnv_hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

ht = HashTable()
ht.insert("exampleKey", "exampleValue")
print("Inserted ('exampleKey', 'exampleValue')")
result = ht.search("exampleKey")
print("Searched for 'exampleKey':", result)