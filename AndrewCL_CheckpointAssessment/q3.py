class Device():
    def __init__(self, device_name : str, brand : str, battery_life : int, price : float): 
        self._device_name = device_name
        self._brand = brand
        self._battery_life = battery_life
        self._price = price
    
    def get_device_name(self):
        return self._device_name

    def get_brand(self):
        return self._brand

    def get_battery_life(self):
        return self._battery_life
    
    def get_price(self):
        return self._price
    
    def print_details(self):
        print(f"Device name : {self._device_name}")
        print(f"Brand : {self._brand}")
        print(f"Battery Life : {self._battery_life}")
        print(f"Price : {self._price}")

class Phone(Device):
    
    def __init__(self, device_name : str, brand : str, battery_life : int, price : float, storage : float):
        super().__init__(device_name, brand, battery_life, price)
        self._storage = storage

    def get_storage(self):
        return self._storage
    
    def print_details(self):
        print(f"Device name :{self._device_name}")
        print(f"Brand : {self._brand}")
        print(f"Battery Life : {self._battery_life}")
        print(f"Price : {self._price}")
        print(f"Storage : {self._storage}")


class Laptop(Device):
    
    def __init__(self, device_name : str, brand : str, battery_life : int, price : float, ram : int):
        super().__init__(device_name, brand, battery_life, price)
        self._ram = ram
    
    def get_storage(self):
        return self._ram
    
    def print_details(self):
        print(f"Device name :{self._device_name}")
        print(f"Brand : {self._brand}")
        print(f"Battery Life : {self._battery_life}")
        print(f"Price : {self._battery_life}")
        print(f"RAM : {self._ram}")



class Tablet(Device):
    
    def __init__(self, device_name, brand, battery_life, price, screen_size):
        super().__init__(device_name, brand, battery_life, price)
        self._screen_size = screen_size
    
    def get_storage(self):
        return self._screen_size
    
    def print_details(self):
        print(f"Device name :{self._device_name}")
        print(f"Brand : {self._brand}")
        print(f"Battery Life : {self._battery_life}")
        print(f"Price : {self._battery_life}")
        print(f"Screen Size : {self._screen_size}")


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

