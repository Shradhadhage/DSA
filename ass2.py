# Class for HashTable Implementation with Linear and Quadratic Probing
class HashTable:
    def __init__(self):
        # Initialize the hash table with a user-defined size
        self.m = int(input("Enter size of hash table: "))  # Table size
        self.hashTable = [None] * self.m                  # Empty hash table
        self.elecount = 0                                  # Number of elements in the table
        self.comparisons = 0                              # Track number of comparisons

    # Hash function to map keys to their index
    def hashFunction(self, key):
        return key % self.m

    # Check if the hash table is full
    def isFull(self):
        return self.elecount == self.m

    # Linear probing to handle collisions
    def linearProbe(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        # Find the next available slot
        while self.hashTable[index] is not None:
            index = (index + 1) % self.m  # Move to the next index (wrap around if needed)
            compare += 1
        self.hashTable[index] = [key, data]
        self.elecount += 1
        print(f"Data inserted at index {index}")
        print(self.hashTable)
        print(f"Number of comparisons: {compare}")

    # Search for a key using linear probing
    def getLinear(self, key, data):
        index = self.hashFunction(key)
        while self.hashTable[index] is not None:
            if self.hashTable[index] == [key, data]:
                return index  # Key found
            index = (index + 1) % self.m
        return None  # Key not found

    # Quadratic probing to handle collisions
    def quadraticProbe(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        i = 0
        # Apply quadratic probing for collision resolution
        while self.hashTable[index] is not None:
            index = (index + i * i) % self.m  # Quadratic formula
            compare += 1
            i += 1
        self.hashTable[index] = [key, data]
        self.elecount += 1
        print(f"Data inserted at index {index}")
        print(self.hashTable)
        print(f"Number of comparisons: {compare}")

    # Search for a key using quadratic probing
    def getQuadratic(self, key, data):
        index = self.hashFunction(key)
        i = 0
        while self.hashTable[index] is not None:
            if self.hashTable
