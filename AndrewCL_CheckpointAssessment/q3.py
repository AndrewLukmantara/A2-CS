class Device():
    def __init__(self, device_name : str, brand : str, battery_life : int, price : float): 
        self.__device_name = device_name
        self.__brand = brand
        self.__battery_life = battery_life
        self.__price = price
    
    def get_device_name(self):
        return self.__device_name

    def get_brand(self):
        return self.__brand

    def get_battery_life(self):
        return self.__battery_life
    
    def get_price(self):
        return self.__price
    
    def print_details(self):
        print(f"Device name : {self.__device_name}")
        print(f"Brand : {self.__brand}")
        print(f"Battery Life : {self.__battery_life}")
        print(f"Price : {self.__price}")

class Phone(Device):
    
    def __init__(self, device_name : str, brand : str, battery_life : int, price : float, storage : float):
        super().__init__(device_name, brand, battery_life, price)
        self.__storage = storage
    
    def get_storage(self):
        return self.__storage
    
    def print_details(self):
        print(f"Device name :{Device.get_device_name(self)}")
        print(f"Brand : {Device.get_brand(self)}")
        print(f"Battery Life : {Device.get_battery_life(self)}")
        print(f"Price : {Device.get_price(self)}")
        print(f"Storage : {self.__storage}")


class Laptop(Device):
    
    def __init__(self, device_name : str, brand : str, battery_life : int, price : float, ram : int):
        super().__init__(device_name, brand, battery_life, price)
        self.__ram = ram
    
    def get_storage(self):
        return self.__ram
    
    def print_details(self):
        print(f"Device name :{Device.get_device_name(self)}")
        print(f"Brand : {Device.get_brand(self)}")
        print(f"Battery Life : {Device.get_battery_life(self)}")
        print(f"Price : {Device.get_price(self)}")
        print(f"RAM : {self.__ram}")



class Tablet(Device):
    
    def __init__(self, device_name, brand, battery_life, price, screen_size):
        super().__init__(device_name, brand, battery_life, price)
        self.__screen_size = screen_size
    
    def get_storage(self):
        return self.__screen_size
    
    def print_details(self):
        print(f"Device name :{Device.get_device_name(self)}")
        print(f"Brand : {Device.get_brand(self)}")
        print(f"Battery Life : {Device.get_battery_life(self)}")
        print(f"Price : {Device.get_price(self)}")
        print(f"Screen Size : {self.__screen_size}")


def ReadDeviceData():
    DeviceArr = [] # ARRAY OF Device
    file = open("C:/Users/62818/OneDrive/A Level CS/AndrewCL_CheckpointAssessment/Devices.txt", "r") # STRING
    line = file.readline().strip() # STRING
    store = line.split(",") # ARRAY OF STRING
    while line != "":
        match store[0]:

            case "Phone":
                DeviceArr.append(Phone(store[1], store[2], int(store[3]), float(store[4]), float(store[5])))
            case "Laptop":
                DeviceArr.append(Laptop(store[1], store[2], int(store[3]), float(store[4]), int(store[5])))
            case "Tablet":
                DeviceArr.append(Tablet(store[1], store[2], int(store[3]), float(store[4]), float(store[5])))

        line = file.readline().strip()
        store = line.split(",")

    file.close()

    return DeviceArr



def PrintDevices(arr):
    for i in range(len(arr)): # i : INTEGER
        arr[i].print_details()


ret_value = ReadDeviceData() # ARRAY OF Device
PrintDevices(ret_value)



def ChooseDevice(arr, budget, brand, minBatteryLife):

    newArr = [] # ARRAY OF Device
    Found = False # BOOLEAN
    for i in range(len(arr)):
        if arr[i].get_price() <= budget and arr[i].get_brand() == brand and arr[i].get_battery_life() >= minBatteryLife:
            newArr.append(arr[i])
            Found = True
    
    if Found == False:
        print("No devices found that match the criteria")
        return -1
    else:
        return newArr


PrintDevices(ChooseDevice(ret_value,500, "TechNova", 10))

