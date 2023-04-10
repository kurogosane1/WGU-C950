#Hashing table
class HashingTable:
    #Constructor with optional intial capacity parameter
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        self.table =[]
        for i in range(initial_capacity):
            self.table.append([])
   # Create hash key -> 0(1)
    def create_hash_key(self, key):
        return int(key) % len(self.table)
    
    # Inser package into hash table -> 0(n)
    def insert(self, key, item):
        key_hash = self.create_hash_key(key)
        values = [key_hash,item]

        if self.table[key_hash] == None:
            self.table[key_hash] = list([values])
            return True
        else: 
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1]== values
                    return True
            self.table[key_hash].append(values)
            return True
            
    # Updating packages in table to match 0(1)
    def update(self, key, item):
        key_hash = self.create_hash_key(key)
        if self.table[key_hash] != None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1]= item
                    print(pair[1])
                    return True
            else:
                print('There was an error in update with Key value: '+ key)
    
    #Searches for an item with matching key in the hash table.
    #Returns the item if found, or none if not found
    def search(self, key):
        #get the buck list where this key would be.
        key_hash = self.create_hash_key(key)
        if self.table[key_hash] != None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
                  
    #Removes an item with matching key from the hash table
    def remove(self, key):
        #get the bucket list where this item will be removed from.
        key_hash = self.create_hash_key(key)
        if self.table[key_hash] != None:
            for i in range(0, len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    self.table[key_hash].pop(i)
                    return True
            return False
        
       

# myHash = HashingTable();
# myHash.insert("John")
# print(myHash.table)

# myHash.insert("Jane Doe")
# print(myHash.table)

# myHash.insert("Saad Doe")
# print(myHash.table)

# print(myHash.search("Saad Doe"))

# myHash.remove("John")
# print(myHash.table)
