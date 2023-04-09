import csv

#importing data from csv data Package


#HashTables class using Chaining
class ChainingHashTable:
    #Constructor with optional initial capacity parameter
    def __init__(self, initial_capacity=10):
        #intialize the hash table with empty bucket list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])


#Creating a class for Packages
class Package:
    def __init__(self, ID, address,city,state, zipCode, del_deadline, mass_kil, note):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.del_deadline = del_deadline
        self.mass_kil = mass_kil
        self.note = note
    
    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.del_deadline, self.mass_kil, self.note)


#Hashing table
class HashingTable:
    #Constructor with optional intial capacity parameter
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        self.table =[]
        for i in range(initial_capacity):
            self.table.append([])
    
    
    def insert(self, item):
        #get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        #inset the item to the end of the bucket list.
        bucket_list.append(item)
    
    #Searches for an item with matching key in the hash table.
    #Returns the item if found, or none if not found
    def search(self, key):
        #get the buck list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #search for the key in the bucket list
        if key in bucket_list:
            # find the items index and return the item that is in the bucket list.
            item_index= bucket_list.index(key)
            return bucket_list[item_index]
        else:
            # the key is not found. 
            return None
    #Removes an item with matching key from the hash table
    def remove(self, key):
        #get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #remove the item from the bucket list if it is present. 
        if key in bucket_list:
            bucket_list.remove(key)
    


myHash = HashingTable();
myHash.insert("John")
print(myHash.table)

myHash.insert("Jane Doe")
print(myHash.table)

myHash.insert("Saad Doe")
print(myHash.table)

print(myHash.search("Saad Doe"))

