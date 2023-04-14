import datetime
import distance
import data_reading

# first we create the Empty truck lists
first_delivery = []
second_delivery = []
third_delivery = []
first_truck_distance = []
second_truck_distance = []
third_truck_distance = []

# Times the trucks leave the Hub
first_truck_leave_time = ['8:00:00']
second_truck_leave_time = ['9:10:00']
third_truck_leave_time = ['11:00:00']

# Setting the delivery start time for the first truck for all packages
for index, value in enumerate(data_reading.get_firstDeliver()):
    data_reading.get_firstDeliver()[index][9] = first_truck_leave_time[0]
    first_delivery.append(data_reading.get_firstDeliver()[index])


# Now we will compare the truck address to the address lists 
for index, outer in enumerate(first_delivery):
    for inner in distance.get_address_data():
        if outer[2] == inner[2]:
            first_truck_distance.append(outer[0])
            first_delivery[index][1] = inner[0]
    
# Calling algorithm to sort packages for the first truck
# print(f'this is the first deliver row 33 {first_delivery}')
distance.shortest_route(first_delivery, 1, 0)
total_distance_T1 = 0

# Calculating the total distance of the first truck and distance of each package
for index in range(len(distance.first_truck_index())):
   try:
       total_distance_T1 = distance.getDistance(int(distance.get_truck_index()[index]), int(distance.get_truck_index()[index+1]), total_distance_T1)

       del_package = distance.get_truck_time(distance.currentlyTravelled(int(distance.first_truck_index()[index]), int(distance.first_truck_index()[index+1])))
       data_reading.getAllPackages().update(distance.first_truck_list()[index][0],first_delivery)
   except IndexError:
       pass

# Set delivery_start to second_truck_leave_time for all truck 2 packages
for index, value in enumerate(data_reading.get_secondDeliver()):
    # print(f'This is the secondDeliver {data_reading.get_secondDeliver()[index]}')
    # print(f'This is the second truck leave time {second_truck_leave_time[0]}')
    data_reading.get_secondDeliver()[index][9] = second_truck_leave_time[0]
    second_delivery.append(data_reading.get_secondDeliver()[index])

 # Compare truck twos address to the address list in the address list
for index, outer in enumerate(second_delivery):
    for inner in distance.get_address_data():
        if outer[2] == inner[2]:
            print(f'this is line 57 {outer[0]}')
            second_truck_distance.append(outer[0])
            second_delivery[index][1] = inner[0]

# Calling function to sort packages for the second truck
# print(f'this is the second delivery {second_delivery}')
distance.shortest_route(second_delivery,2,0)
total_distance_T2 = 0

# Calculate the total distance of the second truck and the distance of each package
for index in range(len(distance.second_truck_index())):
    try:
        pointA = int(distance.second_truck_index()[index])
        pointB = int(distance.second_truck_index()[index+1])
        # distance.get_time(distance.get_current_distance(int(distance.second_truck_index()[index]), int(distance.second_truck_index()[index + 1])), second_leave_times)
        total_distance_T2 = distance.getDistance(pointA,pointB, total_distance_T2)

        deliver_package = distance.get_truck_time(distance.currentlyTravelled(pointA,pointB), second_truck_leave_time)
        distance.second_truck_lists()[index][10] = (str(deliver_package))
        data_reading.getAllPackages().update(int(distance.second_truck_index()[index][0]),second_delivery)
            
    except IndexError:
        pass
    
 # Set delivery_start to third truck_leave_time for all truck 3 packages
for index, value in enumerate(data_reading.get_thirdDeliver()):
    data_reading.get_thirdDeliver()[index][9] = third_truck_leave_time[0]
    third_delivery.append(data_reading.get_thirdDeliver()[index])

# Compare truck three address to the address list in the address data
for index, outer in enumerate(second_delivery):
    for inner in distance.get_address_data():
        if outer[2] == inner[2]:
            third_truck_distance.append(outer[0])
            third_delivery[index][1] = inner[0]

# Calling function to sort packages for the third truck
distance.shortest_route(third_delivery,3,0)
total_distance_T3 = 0

# Calculate the total distance of the third truck and the distance of each package
for index in range(len(distance.third_truck_index())):
    try: 
        pointA = int(distance.third_truck_index()[index])
        pointB = int(distance.third_truck_index()[index+1])

        total_distance_T3 = distance.getDistance(pointA,pointB,total_distance_T3)

        deliver_package =  distance.get_truck_time(distance.currentlyTravelled(pointA, pointB), third_truck_leave_time)
        distance.third_truck_lists()[index][10] = (str(deliver_package))
        data_reading.getAllPackages().update(int(distance.third_truck_index()[index][0]), third_delivery)
    except IndexError:
        pass

def total_distance():
    return total_distance_T1 + total_distance_T2 + total_distance_T3

