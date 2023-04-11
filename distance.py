import csv
import datetime
from hashingTable import HashTable

# Read CSV files and add to a list
with open('./data/distance.csv') as csvfile_1:
    distance_data_csv = csv.reader(csvfile_1,delimiter=',')
with open('./data/addressData.csv') as csvfile_2:
    address_data_csv = csv.reader(csvfile_2,delimiter=',')

    # Now to get pacakge address data 
    def get_address_data():
        return address_data_csv

    # Now to calculate the total distance from each row and column in the distance csv
    def getDistance(row, col, total):
        distance = distance_data_csv[row][col]
        # incase the row is blank but distance can be found from the column
        if distance =='':
            distance = distance_data_csv[col][row]

        return total + float(distance)
    
    # Now we need to calculate the distance from the current location
    def currentlyTravelled(row, col):
        distance = distance_data_csv[row][col]
        if distance =='':
            distance = distance_data_csv[col][row]
        
        return distance

    #Calculate the total distance a truck has travelled
    def get_truck_Distance(distance,truckData):
        new_time = distance / 18
        dist_min = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = dist_min +':00'
        truckData.append(final_time)
        total = datetime.timedelta()
        for i in truckData:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        return total
    
    # These lists represent the tructs that bave been sorted and are put in order
    first_truck = []
    first_truck_indexs = []
    second_truck = []
    second_truck_indexs = []
    third_truck = []
    third_truck_indexs = []

    # Next we shall be utilizing the 'Greedy approach' algorithm. 
    # Greedy Algorithm usies the vertex distances and predecessors pointers 
    # it also pushes all vertices to a queue of unvisted verices and computes the shortest distance
    # and by utilizing recursive process to determine the best location to visit based on current location

    # The following algorith utilizes 3 parameter:
    # 1. Packages lists
    # 2. Trucks identification or truck number
    # 3. Current location of the truck

    # There are 2 loops being utilized in this algorithm
    # The first loop is to identify the shortest distance to the next location. The lower value will continously change until the minimum value is found
    # Second loop is where the lowerst value has been determined. Using conditional statements the value is then assorted to the appropriate truck.The current package is taken out of the list
    # and the current location moves to the next optimal location
    # determined from the first loop. Lastly, a recursive call is made
    # for the next location and shortened list. Recursive calls will
    # continually be made until the base case is called, which will
    # end the function and return the now empty list. 

    def shortest_route(dataList, num, cur_location):
        if not len(dataList):
            return dataList
        lowest_distance = 50.0
        location = 0

        for i in dataList:
            value = int(i[1])
            if currentlyTravelled(cur_location, int(i[1]) <= lowest_distance):
                lowest_distance = currentlyTravelled(cur_location, value)
                location = value
        
        for i in dataList:
            if currentlyTravelled(cur_location, int(i[1]) == lowest_distance):
                if num ==1:
                    first_truck.append(i)
                    first_truck_indexs.append(i[1])
                    dataList.pop(dataList.index(1))
                    cur_location = location
                    shortest_route(dataList, 1, cur_location)
                elif num ==2:
                    second_truck.append(i)
                    second_truck_indexs.append(i[1])
                    dataList.pop(dataList.index(1))
                    cur_location = location
                    shortest_route(dataList, 2, cur_location)
                elif num ==3:
                    third_truck.append(i)
                    third_truck_indexs.append(i[1])
                    dataList.pop(dataList.index[i])
                    cur_location = location
                    shortest_route(dataList, 3, cur_location)
            
        # inserting 0 for the first index of each index list
        first_truck_indexs.insert(0,'0')
        second_truck_indexs.insert(0,'0')
        third_truck_indexs.insert(0,'0')

        # The following are helpers functions to return the required truck lists above
        def first_truck_index():
            return first_truck_indexs
        
        def first_truck_lists():
            return first_truck
        
        def second_truck_index():
            return second_truck_indexs
        
        def second_truck_lists():
            return second_truck
        
        def third_truck_index():
            return third_truck_indexs
        
        def third_truck_lists():
            return third_truck