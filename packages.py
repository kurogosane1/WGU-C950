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
    print("This is to see the outer")
    print(outer)
    print("This is to see the inner")
    print(inner)
    for inner in distance.get_address_data():
        if outer[2] == inner[2]:
            first_truck_distance.append[outer[0]]
            first_delivery[index][1] = inner[0]
    
# Calling algorithm to sort packages for the first truck
distance.shortest_route(first_delivery,1,0)
first_truck_total_distance =0

# Calculating the total distance of the first truck and distance of each package
for index in range(len(distance.first_truck_index())):
   try:
       first_truck_total_distance = distance.getDistance(int(distance.get_truck_index()[index]), int(distance.get_truck_index()[index+1]), first_truck_total_distance)

       del_package = distance.get_truck_time(distance.currentlyTravelled(int(distance.first_truck_index()[index]), int(distance.first_truck_index()[index+1])))
       data_reading.getAllPackages().update(distance.first_truck_list()[index][0],first_delivery)
   except IndexError:
       pass

 # Calculating the total distance of the 2nd Truck and the distance of each package
 
    
   