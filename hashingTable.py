# Syed Khurshid, SID:010081191

class HashingTable:
    def __init__(self, capacity=10):
        self.table = []
        for _ in range(capacity):
            self.table.append([])

    # Create hash key -> O(1)
    def create_hash_key(self, key):
        return int(key) % len(self.table)

    # Insert package into hash table -> O(n)
    def insert(self, key, value):
        hashKey = self.create_hash_key(key)
        values = [key, value]

        if self.table[hashKey] == None:
            self.table[hashKey] = list([values])
            return True
        else:
            for pair in self.table[hashKey]:
                if pair[0] == key:
                    pair[1] = values
                    return True
            self.table[hashKey].append(values)
            return True

    # Update package in hash table -> O(n)
    def update(self, key, value):
        hashKey = self.create_hash_key(key)
        if self.table[hashKey] != None:
            for pair in self.table[hashKey]:
                if pair[0] == key:
                    pair[1] = value
                    return True
        else:
            print('Unsuccessful Key Updation: ' + key)

    # Get a value from hash table -> O(n)
    def get_value(self, key):
        hashKey = self.create_hash_key(key)
        if self.table[hashKey] != None:
            for pair in self.table[hashKey]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Delete a value from hash table -> O(n)
    def remove(self, key):
        hashKey = self.create_hash_key(key)

        if self.table[hashKey] == None:
            return False
        for i in range(0, len(self.table[hashKey])):
            if self.table[hashKey][i][0] == key:
                self.table[hashKey].pop(i)
                return True
        return False

class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item
