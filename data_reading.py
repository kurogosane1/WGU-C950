# Syed Khurshid, SID:010081191
import csv
from hashingTable import HashingTable

# Read CSV files
with open('./data/package.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')

    myHash = HashingTable()  # Create an instance of HashMap class
    firstTruckDelivery = []  # first truck delivery
    secondTruckDelivery = [] # second truck delivery
    finalTruckDelivery = [] # final truck delivery

    # Insert values from csv file into key/value pairs of the hash table -> O(n)
    for row in read_csv:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'

        value = [id, address_location, address, city, state, zip, delivery, size, 
            note, delivery_start, delivery_status]

        # Conditional statements to determine which truck a package should be located and 
        # put these packages into a nested list for quick indexing

        # Correct incorrect package details
        if '84104' in value[5] and '10:30' not in value[6]:
            finalTruckDelivery.append(value)

        # First truck's first delivery
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                firstTruckDelivery.append(value)

        # Second truck's delivery
        if 'Can only be' in value[8] or 'Delayed' in value[8]:
            secondTruckDelivery.append(value)
        
        # Check remaining packages
        if value not in firstTruckDelivery and value not in secondTruckDelivery and value not in finalTruckDelivery:
            secondTruckDelivery.append(value) if len(secondTruckDelivery) < len(finalTruckDelivery) else finalTruckDelivery.append(value)

        # Insert value into the hash table
        myHash.insert(id, value)
       

    # Get packages on the first delivery -> O(1)
    def get_first_delivery():
        return firstTruckDelivery

    # Get packages on the second delivery -> O(1)
    def get_second_delivery():
        return secondTruckDelivery

    # Get packages on the final delivery -> O(1)
    def get_final_delivery():
        return finalTruckDelivery

    # Get full list of packages -> O(1)
    def getAllPackages():
        return myHash