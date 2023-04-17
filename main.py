# Syed Khurshid, SID:010081191

from data_reading import getAllPackages
from packages import total_distance, truckOne_distance, truckTwo_distance, truckThree_distance
import datetime
from menu import userMenu

class Main:

    userMenu()
       # This is the display message that is shown when the user runs the program. The interface is accessible from here
    # print('------------------------------')
    # print('WGUPS Routing Program!')
    # print('------------------------------\n')
    # print(f'Total Distance Truck 1 drove {truckOne_distance():.2f} miles.\n')   
    # print(f'Total Distance Truck 2 drove {truckTwo_distance():.2f} miles.\n')   
    # print(f'Total Distance Truck 3 drove {truckThree_distance():.2f} miles.\n')   
    # print(f'Route was completed in {total_distance():.2f} miles.\n')   

    # userInput = input("""
    # Please select an option below to begin or type 'quit' or 'q to quit:
    # 1. Get info for all packages at a particular time
    # 2. Get info for a single package at a particular time
    # 3. Get packages between a particular range
    # """)

    # while userInput != 'quit' or userInput != 'q':
       # Case if user selects Option # 1 which is to get all packages at a particular time
    #    if userInput == '1':
    #        try:
    #            inputTime = input('Enter a time (HH:MM:SS): ')
    #            if inputTime == "Quit" or inputTime == "q":
    #                exit()
               

               # Complexity 0(n^2)
            #    else:
            #         (hrs,mins, secs) = inputTime.split(':')
            #         converted_input_time = datetime.timedelta(hours =int(hrs), minutes=int(mins), seconds=int(secs))
            #         for count in range(1, 41):
            #             try:
            #                 firstTime = getAllPackages().get_value(str(count))[9]
            #                 secondTime = getAllPackages().get_value(str(count))[10]
            #                 print(f'This is the first time {firstTime} and {secondTime}')
            #                 (hrs,mins, secs) = firstTime.split(':')
            #                 converted_first_time = datetime.timedelta(hours =int(hrs), minutes=int(mins), seconds=int(secs))
            #                 (hrs,mins, secs) = secondTime.split(':')
            #                 converted_second_time = datetime.timedelta(hours =int(hrs), minutes=int(mins), seconds=int(secs))
            #             except ImportError:
            #                 pass
                            
                        # Determine which packages have left the hub
                        # if converted_first_time >= converted_input_time:
                        #     getAllPackages().get_value(str(count))[10] = 'At Hub'
                        #     getAllPackages().get_value(str(count))[9] = 'Leaves at ' + firstTime

                        #     # Print the packages current info
                        #     print( f'Package ID: {getAllPackages().get_value(str(count))[0]}, ')
                        #     print( f'Delivery Status: {getAllPackages().get_value(str(count))[10]},')
                            

                        # Determine which pacakges that have left the Hub but are pending delivery
                        # elif converted_first_time <= converted_input_time:
                        #     if converted_input_time < converted_second_time:
                        #         getAllPackages().get_value(str(count))[10] = 'In transit'
                        #         getAllPackages().get_value(str(count))[9] = ' Left at ' + firstTime

                        #         # Print the pacakges current info
                        #         print( f'Package ID: {getAllPackages().get_value(str(count))[0]}, ')
                        #         print( f'Delivery Status: {getAllPackages().get_value(str(count))[10]},')
                                
                                
                            # Determine which packages have already been delivered
                            # else:
                            #         getAllPackages().get_value(str(count))[10] = 'Delivered at ' + secondTime
                            #         getAllPackages().get_value(str(count))[0] = ' Left at '+ firstTime

                            #     # Print packages current info
                            #         print( f'Package ID: {getAllPackages().get_value(str(count))[0]}, ')
                            #         print( f'Delivery Status: {getAllPackages().get_value(str(count))[10]},')
                                    
                          
                           
        #    except IndexError:
        #        print(IndexError)
        #        exit()
        #    except ValueError:
        #        print('Invalid entry')
        #        exit()
      
          
    #    elif userInput == '2':
    #        try:
    #            count = input(' Enter package ID number : ')
    #            firstTime = getAllPackages().get_value(str(count))[9]
    #            secondTime = getAllPackages().get_value(str(count))[10]
    #            inputTime = input('Enter a time (HH:MM:SS): ')
    #            (hrs, mins, secs) = inputTime.split(":")
    #            converted_input_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
    #            (hrs, mins, secs) = firstTime.split(":")
    #            converted_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs)) 
    #            (hrs, mins, secs) = secondTime.split(":")
    #            converted_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

               # Determine which pacakges have left the hub
            #    if converted_first_time >= converted_input_time:
            #        getAllPackages().get_value(str(count))[10] = 'At hub'
            #        getAllPackages().get_value(str(count))[9] = 'Leaves at '+ firstTime

                   # Print all the information related to the packages based on current
                   # info provided
            #        print(f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
            #               f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
            #               f'Required delivery time: {getAllPackages().get_value(str(count))[6]} \n'
            #               f'Package weight: {getAllPackages().get_value(str(count))[7]} \n'
            #               f'Truck status: {getAllPackages().get_value(str(count))[9]} \n'
            #               f'Delivery status: {getAllPackages().get_value(str(count))[10]} \n'
            #               )
                   
            #    elif converted_first_time<= converted_input_time:
            #        if converted_input_time < converted_second_time:
            #            getAllPackages().get_value(str(count))[10] = 'In transit'
            #            getAllPackages().get_value(str(count))[9] = 'Left at '+ firstTime

            #            print(f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
            #               f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
            #               f'Required delivery time: {getAllPackages().get_value(str(count))[6]} \n'
            #               f'Package weight: {getAllPackages().get_value(str(count))[7]} \n'
            #               f'Truck status: {getAllPackages().get_value(str(count))[9]} \n'
            #               f'Delivery status: {getAllPackages().get_value(str(count))[10]} \n'
            #               )
                       
               # Determining which packages have already been delivered
            #    else:
            #        getAllPackages().get_value(str(count))[10] = 'Delivered at '+ secondTime
            #        getAllPackages().get_value(str(count))[9] = 'Left at '+ firstTime

                   # Print packages current info
        #            print(f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
        #                   f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
        #                   f'Required delivery time: {getAllPackages().get_value(str(count))[6]} \n'
        #                   f'Package weight: {getAllPackages().get_value(str(count))[7]} \n'
        #                   f'Truck status: {getAllPackages().get_value(str(count))[9]} \n'
        #                   f'Delivery status: {getAllPackages().get_value(str(count))[10]} \n'
        #                   )
                   
        #    except ValueError:
        #        print('Invalid entry')
        #        exit()
        # Incase option 3 is selected
    #    elif userInput == "3":
    #        try:
    #            input_Start_Time = input('Enter starting time as HH:MM:SS: ')
    #            input_End_Time = input('Enter ending time as HH:MM:SS: ')
    #            (hrs, mins, secs) = input_Start_Time.split(':')
    #            converted_input_start = datetime.timedelta(hours =int(hrs), minutes=int(mins), seconds=int(secs))
    #            (hrs, mins, secs) = input_End_Time.split(':')
    #            converted_input_end = datetime.timedelta(hours =int(hrs), minutes=int(mins), seconds=int(secs))
               
    #            for count in range(1,41):
    #                try:
    #                    firstTime = getAllPackages().get_value(str(count))[9]
    #                    secondTime = getAllPackages().get_value(str(count))[10]
    #                    status = getAllPackages().get_value(str(count))[6]
    #                    (hrs,mins, secs) = firstTime.split(':')
    #                    converted_first_time = datetime.timedelta(hours =int(hrs), minutes=int(mins), seconds=int(secs))
    #                    (hrs,mins, secs) = secondTime.split(':')
    #                    converted_second_time = datetime.timedelta(hours =int(hrs), minutes=int(mins), seconds=int(secs))

    #                    if converted_first_time>=converted_input_start or converted_second_time>=converted_input_start:
                           # If the start time is after the delivery start time
                        #    if converted_first_time >= converted_input_start:
                        #        getAllPackages().get_value(str(count))[10] = 'At hub'
                        #        getAllPackages().get_value(str(count))[9] = 'Leaves at '+ firstTime
                               # Print all the information related to the packages based on current
                               # info provided
                        #        print(f'Package ID: {getAllPackages().get_value(str(count))[0]} '
                        #                 f'Street address: {getAllPackages().get_value(str(count))[2]} '
                        #                 f'Required delivery time: {getAllPackages().get_value(str(count))[6]} '
                        #                 f'Package weight: {getAllPackages().get_value(str(count))[7]} '
                        #                 f'Truck status: {getAllPackages().get_value(str(count))[9]} '
                        #                 f'Delivery status: {getAllPackages().get_value(str(count))[10]} '
                        #                 )
                        #    elif converted_first_time < converted_input_start and converted_second_time > converted_input_end:
                        #         getAllPackages().get_value(str(count))[10] = 'In transit'
                        #         getAllPackages().get_value(str(count))[9] = 'Left at '+ firstTime 
                                # Print all the information related to the packages based on current
                                # info provided
                        #         print(f'Package ID: {getAllPackages().get_value(str(count))[0]} '
                        #                 f'Street address: {getAllPackages().get_value(str(count))[2]} '
                        #                 f'Required delivery time: {getAllPackages().get_value(str(count))[6]} '
                        #                 f'Package weight: {getAllPackages().get_value(str(count))[7]} '
                        #                 f'Truck status: {getAllPackages().get_value(str(count))[9]} '
                        #                 f'Delivery status: {getAllPackages().get_value(str(count))[10]} '
                        #                 )
                        #    else:
                        #        getAllPackages().get_value(str(count))[10] = 'Delivered at '+ secondTime
                        #        getAllPackages().get_value(str(count))[9] = 'Left at '+ firstTime
                               # Print all the information related to the packages based on current
                               # info provided
                    #            print(f'Package ID: {getAllPackages().get_value(str(count))[0]} '
                    #                     f'Street address: {getAllPackages().get_value(str(count))[2]} '
                    #                     f'Required delivery time: {getAllPackages().get_value(str(count))[6]} '
                    #                     f'Package weight: {getAllPackages().get_value(str(count))[7]} '
                    #                     f'Truck status: {getAllPackages().get_value(str(count))[9]} '
                    #                     f'Delivery status: {getAllPackages().get_value(str(count))[10]} '
                    #                     )
                    #    else:
                    #        pass
                           
                           
                               
                #    except ValueError:
                #        print('Invalid entry')
                #        exit()
                   


        #    except ValueError:
        #        print('Invalid entry')
        #        exit()   
        # Case 'exit 
        # This exists the program
    #    elif userInput == 'quit':
    #        exit()
        # Case Error
        # Print Invalid Entry and quit the program
    #    else:
    #        print('Invalid input')
    #        exit()    
        