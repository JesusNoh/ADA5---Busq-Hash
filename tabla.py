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

# Crear una tabla hash de tamaño 10
hash_table = HashTable(10)

# Agregar elementos a la tabla
hash_table.add("manzana")
hash_table.add("banana")
hash_table.add("naranja")

# Buscar elementos en la tabla
print("Buscar 'manzana':", hash_table.search("manzana"))  # Debería devolver True
print("Buscar 'pera':", hash_table.search("pera"))        # Debería devolver False