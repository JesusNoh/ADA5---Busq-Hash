class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        index = self._hash(key)
        return key in self.table[index]

hash_table = HashTable(10)

hash_table.add("manzana")
hash_table.add("banana")
hash_table.add("naranja")

print("Buscar 'manzana':", hash_table.search("manzana"))  
print("Buscar 'pera':", hash_table.search("pera"))       
