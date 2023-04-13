# Syed Khurshid, SID:010081191

from data_reading import getAllData
from packages import total_distance
import datetime

class Main:
       # This is the display message that is shown when the user runs the program. The interface is accessible from here
    print('------------------------------')
    print('WGUPS Routing Program!')
    print('------------------------------\n')
    print(f'Route was completed in {total_distance():.2f} miles.\n')   

    userInput = input("""
    Please select an option below to begin or type 'quit' to quit:
    1. Get info for all packages at a particular time
    2. Get info for a single package at a particular time
    """)

    while userInput is not 'quit':
       # Case if user selects Option # 1 which is to get all packages at a particular time
       if userInput == '1':
           try:
               inputTime = input('Enter a time (HH:MM:SS): ')
               (hrs,mins, secs) = inputTime.split(':')
               converted_input_time = datetime.timedelta(hours =int(hrs), minutes=int(mins), seconds=int(secs))

               # Complexity 0(n^2)
               for count in range(1, 41):
                   try:
                       firstTime = getAllData().get_value(str(count))[9]
                       secondTime = getAllData().get_value(str(count))[10]
                       (hrs,mins, secs) = firstTime.split(':')
                       converted_first_time = datetime.timedelta(hours =int(hrs), minutes=int(mins), seconds=int(secs))
                       (hrs,mins, secs) = secondTime.split(':')
                       converted_second_time = datetime.timedelta(hours =int(hrs), minutes=int(mins), seconds=int(secs))
                   except ImportError:
                     pass
                     
                   # Determine which packages have left the hub
                   if converted_first_time >= converted_input_time:
                       getAllData().get_value(str(count))[10] = 'At Hub'
                       getAllData().get_value(str(count))[9] = 'Leaves at ' + firstTime

                       # Print the packages current info
                       print( f'Package ID: {getAllData().get_value(str(count))[0]}, ')
                       print( f'Delivery Status: {getAllData().get_value(str(count))[10]},')

                   # Determine which pacakges that have left the Hub but are pending delivery
                   elif converted_first_time <= converted_input_time:
                       if converted_input_time < converted_second_time:
                           getAllData().get_value(str(count))[10] = 'In transit'
                           getAllData().get_value(str(count))[9] = ' Left at ' + firstTime

                           # Print the pacakges current info
                           print( f'Package ID: {getAllData().get_value(str(count))[0]}, ')
                           print( f'Delivery Status: {getAllData().get_value(str(count))[10]},')
                        
                       # Determine which packages have already been delivered
                       else:
                            getAllData().get_value(str(count))[10] = 'Delivered at ' + secondTime
                            getAllData().get_value(str(count))[0] = ' Left at '+ firstTime

                           # Print packages current info
                            print( f'Package ID: {getAllData().get_value(str(count))[0]}, ')
                            print( f'Delivery Status: {getAllData().get_value(str(count))[10]},')
                          
                           
           except IndexError:
               print(IndexError)
               exit()
           except ValueError:
               print('Invalid entry')
               exit()
      
          
                         