from ex07_area_of_rectangular_room.area_calc import *

if __name__ == '__main__':
    length = input("Length of room: ")
    width = input("Width of room: ")
    try:
        area = calc(length, width)
    except CalcArgumentError as err:
        print("An error occured:")
        print(err.message, err.argument)
    else:
        print("Area of room: {} square feet, or {} square meters".format(*area))
