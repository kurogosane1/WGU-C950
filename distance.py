# Syed Khurshid, SID:010081191

import csv
import datetime

# Read CSV files
with open('./data/distance.csv') as csvfile_1:
    distance_csv = list(csv.reader(csvfile_1, delimiter=','))
with open('./data/addressData.csv') as csvfile_2:
    distance_name_csv = list(csv.reader(csvfile_2, delimiter=','))

    # Get package address data -> O(n)
    def get_address():
        return distance_name_csv

    # Calculate the total distance from row/column values -> O(1)
    def getDistance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return total + float(distance)

    # Calculate the current distance from row/column values -> O(1)

    def currentlyTravelled(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return float(distance)

    # Calculate total distance for a given truck -> O(n)
    # get_time
    def get_truck_time(distance, truck_list):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs),
                                        minutes=int(mins), seconds=int(secs))
            print(total)
        return total

    # these lists represent the sorted trucks that are put in order of efficiency in the function below
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
     # Base Case: Length of the list is False, or zero. 

     # Space-Time Complexity -> O(n^2)

    def get_shortest_route(_list, num, curr_location):
        if not len(_list):
            return _list

        lowest_value = 50.0
        location = 0
        # print(_list[1][1])
        for i in _list:

            value = int(i[1])
            if currentlyTravelled(curr_location, value) <= lowest_value:
                lowest_value = currentlyTravelled(
                    curr_location, value)
                location = value

        for i in _list:

            if currentlyTravelled(curr_location, int(i[1])) == lowest_value:
                if num == 1:
                    first_truck.append(i)
                    first_truck_indexs.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 1, curr_location)
                elif num == 2:
                    second_truck.append(i)
                    second_truck_indexs.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 2, curr_location)
                elif num == 3:
                    third_truck.append(i)
                    third_truck_indexs.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    get_shortest_route(_list, 3, curr_location)

    # Insert 0 for the first index of each index list
    first_truck_indexs.insert(0, '0')
    second_truck_indexs.insert(0, '0')
    third_truck_indexs.insert(0, '0')

    # The following are all helper functions to return a desired value -> O(1)
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
