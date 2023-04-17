import csv
from hashingTable import HashingTable

# Read the CSV files
with open('./data/package.csv') as csvFile:
        read_csv= csv.reader(csvFile, delimiter=",")

        #Creating an instance of the hash table
        myHash = HashingTable()
        # first truck delivery
        firstTruckDelivery = []
        # second truck delivery
        secondTruckDelivery = []
        # third truck delivery
        finalTruckDelivery = []

        # insert values from the csv file into key/value pairs of the hash table . Utilizing the 0(n)
        for row in read_csv:
            id = row[0]
            address=row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            delivery = row[5]
            size = row[6]
            note = row[7]
            delivery_start = ''
            address_location = ''
            delivery_status = 'At hub'

            value= [id, address_location,address,city,state,zip,delivery,size,note,delivery_start,delivery_status]

            # Categorization of packages status that can then placed in nested lists for quick indexing
            
            # To correct package details that were listed incorrectly
            if "84104" in value[5] and"10:30" not in value[6]:
                finalTruckDelivery.append(value)
            
            # First Trucks delivery
            if value[6] != 'EOD':
                 if 'Must' in value[8] or 'None' in value[8]:
                      firstTruckDelivery.append(value)

            # Second truck delivery
            if 'Can only be' in value[8] or 'Delayed' in value[8]:
                 secondTruckDelivery.append(value)
            
            # Check remaining packages
            if value not in firstTruckDelivery and value not in secondTruckDelivery and value not in finalTruckDelivery:
                 secondTruckDelivery.append(value) if len(secondTruckDelivery) < len(finalTruckDelivery) else finalTruckDelivery.append(value)
          
            # Insert value into the hash table
            myHash.insert(id, value)

        # Get the list of all packages¬
        def getAllPackages():
             return myHash  

        # Get packages on the first delivery 
        def get_firstDeliver():
             return firstTruckDelivery
        
        # Get packages on the second truck on deliver
        def get_secondDeliver():
             return secondTruckDelivery
        
        # Get packages on the final truck delivery
        def get_thirdDeliver():
             return finalTruckDelivery
        