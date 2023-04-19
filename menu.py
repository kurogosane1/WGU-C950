# # Syed Khurshid, SID:010081191

from data_reading import getAllPackages
from packages import total_distance, truckOne_distance, truckTwo_distance, truckThree_distance
import datetime

# # This is the user menu


def userMenu():
    # This is the display message that is shown when the user runs the program. The interface is accessible from here
    print('------------------------------')
    print('WGUPS Package Delivery Planning tool')
    print('------------------------------\n')
    print(f'Total Distance Truck 1 drove {truckOne_distance():.2f} miles.\n')
    print(f'Total Distance Truck 2 drove {truckTwo_distance():.2f} miles.\n')
    print(f'Total Distance Truck 3 drove {truckThree_distance():.2f} miles.\n')
    print(f'Route was completed in {total_distance():.2f} miles.\n')

    userInput = input("""
    Please select an option below to begin or type 'quit' or 'q to quit:
    1. Get info for all packages at a particular time
    2. Get info for a single package at a particular time
    3. Get package status between a particular time range
    4. Get package by address
    5. Get package by City
    6. Get packages by Zipcode
    7. Get by package weight
    8. Get by Deadline
    """)

    # Switch statements based on User Feedback
    match userInput:
        case "1":
            get_inTime()
        case "2":
            get_Package_at_time()
        case "3":
            get_within_range()
        case "4":
            get_address()
        case "5":
            get_by_city()
        case "6":
            get_by_zipcode()
        case "7":
            get_by_weight()
        case "8":
            get_by_deadline()
        case "Quit":
            exit()
        case "q":
            exit()
        case "quit":
            exit()


# First Menu option
def get_inTime():
    try:
        inputTime = input(
            'Enter a time to get all packages till that time\n and enter as (HH:MM:SS): ')
        if inputTime != "Quit" or inputTime != "q" or inputTime != "exit":
            (hrs, mins, secs) = inputTime.split(":")
            convert_user_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            for count in range(1, 41):
                try:
                    first_time = getAllPackages().get_value(str(count))[9]
                    second_time = getAllPackages().get_value(str(count))[10]
                    (hrs, mins, secs) = first_time.split(":")
                    converted_first_time = datetime.timedelta(
                        hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    (hrs, mins, secs) = second_time.split(':')
                    converted_second_time = datetime.timedelta(
                        hours=int(hrs), minutes=int(mins), seconds=int(secs))
                except ValueError:
                    pass

                # Determine which packages have left the hub
                if converted_first_time >= convert_user_time:
                    getAllPackages().get_value(str(count))[10] = 'At Hub'
                    getAllPackages().get_value(str(count))[
                        9] = "Leaves at "+first_time

                    # Print packages current info
                    print(
                        f'Package ID: {getAllPackages().get_value(str(count))[0]}, ' f'Delivery status: {getAllPackages().get_value(str(count))[10]}')

                # Determine which packages have left left but have not been delivered
                elif converted_first_time < convert_user_time:
                    if convert_user_time < converted_second_time:
                        getAllPackages().get_value(str(count))[
                            10] = "In transit"
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}, ' f'Delivery status: {getAllPackages().get_value(str(count))[10]}')
                    else:
                        getAllPackages().get_value(str(count))[
                            10] = "Delievered at " + second_time
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}, ' f'Delivery status: {getAllPackages().get_value(str(count))[10]}')

    except ValueError:
        print('Invalid Entry')
        exit()
    except IndexError:
        print(IndexError)
        exit()

    exit()

# Packages at a time
def get_Package_at_time():
    try:
        count = input("Enter a valid package ID: ")
        first_time = getAllPackages().get_value(str(count))[9]
        (hrs, mins, secs) = first_time.split(':')
        converted_first_time = datetime.timedelta(
            hours=int(hrs), minutes=int(mins), seconds=int(secs))
        second_time = getAllPackages().get_value(str(count))[10]
        (hrs, mins, secs) = second_time.split(':')
        converted_second_time = datetime.timedelta(
            hours=int(hrs), minutes=int(mins), seconds=int(secs))
        input_time = input('Enter a time (HH:MM:SS): ')
        (hrs, mins, secs) = input_time.split(':')
        convert_user_time = datetime.timedelta(
            hours=int(hrs), minutes=int(mins), seconds=int(secs))

        # Determine which packages have left the hub
        if converted_first_time >= convert_user_time:
            getAllPackages().get_value(str(count))[10] = "At Hub"
            getAllPackages().get_value(str(count))[
                9] = "Leaves at " + first_time

            # Print packages current info
            print(
                f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
            )
        elif converted_first_time < convert_user_time:
            if convert_user_time < converted_second_time:
                getAllPackages().get_value(str(count))[10] = "In Transit"
                getAllPackages().get_value(str(count))[
                    9] = "Left at " + first_time

                # Print packages current info
                print(
                    f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                    f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                    f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                    f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                    f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                    f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                )

            else:
                getAllPackages().get_value(str(count))[
                    10] = 'Delivered at ' + second_time
                getAllPackages().get_value(str(count))[
                    9] = "Left at " + first_time

                # Print packages current info
                print(
                    f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                    f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                    f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                    f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                    f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                    f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                )

    except ValueError:
        print("Invalid Entry")
        exit()

# Packages by address at a particular time
def get_address():
    user_input = input("Please input by Delivery Address: ")
    user_time = input("Please input the time in HH:MM:SS: ")

    if user_input is not "Quit" or not "q" or not "quit":
        for count in range(1, 41):
            first_time = getAllPackages().get_value(str(count))[9]
            (hrs, mins, secs) = first_time.split(':')
            converted_first_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            second_time = getAllPackages().get_value(str(count))[10]
            (hrs, mins, secs) = second_time.split(':')
            converted_second_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            (hrs, mins, secs) = user_time.split(':')
            convert_user_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            # print(f'this is line {count} and its {getAllPackages().get_value(str(count))[2]}')
            if user_input == getAllPackages().get_value(str(count))[2]:
                if converted_first_time >= convert_user_time:
                    getAllPackages().get_value(str(count))[10] = "At Hub"
                    getAllPackages().get_value(str(count))[
                        9] = "Leaves at " + first_time

                    # Print packages current info
                    print(
                        f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                        f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                        f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                        f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                        f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                        f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                    )
                elif converted_first_time < convert_user_time:
                    if convert_user_time < converted_second_time:
                        getAllPackages().get_value(str(count))[
                            10] = "In Transit"
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                            f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                        )
                    else:
                        getAllPackages().get_value(str(count))[
                            10] = "Delivered at " + second_time
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                            f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                        )
                else:
                    print("Please enter valid address")
                    exit()

# Get info for packages by city at a particular time
def get_by_city():
    user_input = input("Please input by city: ")
    user_time = input("Please input the time in HH:MM:SS: ")

    if user_input is not "Quit" or not "q" or not "quit":
        for count in range(1, 41):
            first_time = getAllPackages().get_value(str(count))[9]
            (hrs, mins, secs) = first_time.split(':')
            converted_first_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            second_time = getAllPackages().get_value(str(count))[10]
            (hrs, mins, secs) = second_time.split(':')
            converted_second_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            (hrs, mins, secs) = user_time.split(':')
            convert_user_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            print(
                f' this is count {count} and line for {getAllPackages().get_value(str(count))[6]}')
            if user_input == getAllPackages().get_value(str(count))[3]:
                if converted_first_time >= convert_user_time:
                    getAllPackages().get_value(str(count))[10] = "At Hub"
                    getAllPackages().get_value(str(count))[
                        9] = "Leaves at " + first_time

                    # Print packages current info
                    print(
                        f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                        f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                        f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                        f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                        f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                        f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                    )
                elif converted_first_time < convert_user_time:
                    if convert_user_time < converted_second_time:
                        getAllPackages().get_value(str(count))[
                            10] = "In Transit"
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                            f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                        )
                    else:
                        getAllPackages().get_value(str(count))[
                            10] = "Delivered at " + second_time
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                            f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                        )
                else:
                    print("Invalid city")
                    exit()

# Packages by zipcode
def get_by_zipcode():
    user_input = input("Please input zipcode: ")
    user_time = input("Please input the time in HH:MM:SS: ")

    if user_input is not "Quit" or not "q" or not "quit":
        for count in range(1, 41):
            first_time = getAllPackages().get_value(str(count))[9]
            (hrs, mins, secs) = first_time.split(':')
            converted_first_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            second_time = getAllPackages().get_value(str(count))[10]
            (hrs, mins, secs) = second_time.split(':')
            converted_second_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            (hrs, mins, secs) = user_time.split(':')
            convert_user_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))

            # print(f'this is line {count} and its {getAllPackages().get_value(str(count))[5]}')
            if user_input == getAllPackages().get_value(str(count))[5]:
                if converted_first_time >= convert_user_time:
                    getAllPackages().get_value(str(count))[10] = "At Hub"
                    getAllPackages().get_value(str(count))[
                        9] = "Leaves at " + first_time

                    # Print packages current info
                    print(
                        f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                        f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                        f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                        f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                        f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                        f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                    )
                elif converted_first_time < convert_user_time:
                    if convert_user_time < converted_second_time:
                        getAllPackages().get_value(str(count))[
                            10] = "In Transit"
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                            f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                        )
                    else:
                        getAllPackages().get_value(str(count))[
                            10] = "Delivered at " + second_time
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                            f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                        )
                else:
                    print("Invalid zipcode")
                    exit()

# Packages by weight
def get_by_weight():
    user_input = input("Please input valid weight: ")
    user_time = input("Please input the time in HH:MM:SS: ")

    if user_input is not "Quit" or not "q" or not "quit":
        for count in range(1, 41):
            first_time = getAllPackages().get_value(str(count))[9]
            (hrs, mins, secs) = first_time.split(':')
            converted_first_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            second_time = getAllPackages().get_value(str(count))[10]
            (hrs, mins, secs) = second_time.split(':')
            converted_second_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            (hrs, mins, secs) = user_time.split(':')
            convert_user_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))

            # print(f'this is line {count} and its {getAllPackages().get_value(str(count))[5]}')
            if user_input == getAllPackages().get_value(str(count))[7]:
                if converted_first_time >= convert_user_time:
                    getAllPackages().get_value(str(count))[10] = "At Hub"
                    getAllPackages().get_value(str(count))[
                        9] = "Leaves at " + first_time

                    # Print packages current info
                    print(
                        f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                        f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                        f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                        f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                        f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                        f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                    )
                elif converted_first_time < convert_user_time:
                    if convert_user_time < converted_second_time:
                        getAllPackages().get_value(str(count))[
                            10] = "In Transit"
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                            f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                        )
                    else:
                        getAllPackages().get_value(str(count))[
                            10] = "Delivered at " + second_time
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                            f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                        )
                else:
                    print("Invalid weight")
                    exit()


# Getting the weight by deadline
def get_by_deadline():

    user_time = input("Please input deadline of the package in HH:MM:SS: ")

    if user_time is not "Quit" or not "q" or not "quit":
        for count in range(1, 41):
            first_time = getAllPackages().get_value(str(count))[9]
            (hrs, mins, secs) = first_time.split(':')
            converted_first_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            second_time = getAllPackages().get_value(str(count))[10]
            (hrs, mins, secs) = second_time.split(':')
            converted_second_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            (hrs, mins, secs) = user_time.split(':')
            convert_user_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))

            # print(f'this is line {count} and its {getAllPackages().get_value(str(count))[5]}')
            if user_time <= getAllPackages().get_value(str(count))[6] and getAllPackages().get_value(str(count))[6] != 'EOD':
                if converted_first_time >= convert_user_time:
                    getAllPackages().get_value(str(count))[10] = "At Hub"
                    getAllPackages().get_value(str(count))[
                        9] = "Leaves at " + first_time

                    # Print packages current info
                    print(
                        f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                        f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                        f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                        f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                        f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                        f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                    )
                elif converted_first_time < convert_user_time:
                    if convert_user_time < converted_second_time:
                        getAllPackages().get_value(str(count))[
                            10] = "In Transit"
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                            f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                        )
                    else:
                        getAllPackages().get_value(str(count))[
                            10] = "Delivered at " + second_time
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}\n'
                            f'Street address: {getAllPackages().get_value(str(count))[2]}\n'
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}\n'
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}\n'
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}\n'
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}\n'
                        )
            else:
                print("Invalid deadline time")
                exit()

# Geting the package within a range
def get_within_range():
    print("Please input the starting and ending time range below")
    user_first_range = input("Input the starting time range in HH:MM:SS: ")
    user_end_range = input("Input the end time range in HH:MM:SS: ")

    if user_first_range and user_end_range != "Quit" or not "q" or not "quit" or not "exit":
        for count in range(1, 41):
            first_time = getAllPackages().get_value(str(count))[9]
            (hrs, mins, secs) = first_time.split(':')
            converted_first_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            second_time = getAllPackages().get_value(str(count))[10]
            (hrs, mins, secs) = second_time.split(':')
            converted_second_time = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            (hrs, mins, secs) = user_first_range.split(':')
            con_first_range = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))
            (hrs, mins, secs) = user_end_range.split(':')
            con_end_range = datetime.timedelta(
                hours=int(hrs), minutes=int(mins), seconds=int(secs))

            # print(converted_first_time<con_first_range)

            if converted_first_time > con_first_range:
                # Print Packages current info
                if converted_first_time > con_first_range and converted_second_time > con_end_range:
                    getAllPackages().get_value(str(count))[10] = "At Hub"
                    getAllPackages().get_value(str(count))[
                        9] = "Leaves at " + first_time
                    print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}. '
                            f'Street address: {getAllPackages().get_value(str(count))[2]}. '
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}. '
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}. '
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}. '
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}. '
                        )
                elif converted_first_time > con_first_range and converted_second_time > con_end_range:
                        getAllPackages().get_value(str(count))[
                            10] = "Delivered at " + second_time
                        getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                        print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}. '
                            f'Street address: {getAllPackages().get_value(str(count))[2]}. '
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}. '
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}. '
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}. '
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}. '
                        )

            elif converted_first_time < con_first_range:
                if converted_second_time < con_end_range:
                    getAllPackages().get_value(str(count))[
                            10] = "Delivered at " + second_time
                    getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                    print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}. '
                            f'Street address: {getAllPackages().get_value(str(count))[2]}. '
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}. '
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}. '
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}. '
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}. '
                        )
                else:
                      getAllPackages().get_value(str(count))[
                            10] = "In Transit"
                      getAllPackages().get_value(str(count))[
                            9] = "Left at " + first_time

                        # Print Packages current info
                      print(
                            f'Package ID: {getAllPackages().get_value(str(count))[0]}. '
                            f'Street address: {getAllPackages().get_value(str(count))[2]}. '
                            f'Required delivery time: {getAllPackages().get_value(str(count))[6]}. '
                            f'Package weight: {getAllPackages().get_value(str(count))[7]}. '
                            f'Truck status: {getAllPackages().get_value(str(count))[9]}. '
                            f'Delivery status: {getAllPackages().get_value(str(count))[10]}. '
                        )
