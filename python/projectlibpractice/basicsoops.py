# class creature:
#     def __init__(self, type:str, mmlornot:str):
#         self.c_type = type
#         self.c_mmlornot = mmlornot

# c1 = creature("dog", "mammal")
# c2 = creature("bird", "not mammal")
# print(c1.c_type)




# class ThermoStat:
#     def __init__(self, room_name:str, current_temp:int, target_temp:int):
#         self.rn = room_name
#         self.ct = current_temp
#         self.tt = target_temp

# thermostat1 = ThermoStat("living_room", 25, 20)
# thermostat2 = ThermoStat("bed_room", 22, 30)
# print(thermostat1.tt)
# print(thermostat2.tt)



"methods in a class"
# class ThermoStat:
#     def __init__(self, room_name:str, current_temp:int, target_temp:int):
#         self.room_name = room_name
#         self.current_temp = current_temp
#         self.target_temp = target_temp

#     def check_status(self):
#         if self.current_temp>self.target_temp:
#             print(f"too hot, decrease to {self.target_temp}")
#         elif self.current_temp<self.target_temp:
#             print(f"too cold, increase to {self.target_temp}")
#         else:
#             print("the temperature is perfect")

# thermostat1 = ThermoStat("living_room", 25, 20)
# thermostat2 = ThermoStat("bed_room", 22, 30)
# thermostat1.check_status()




# class ThermoStat:
#     def __init__(self, room_name:str, current_temp:int, target_temp:int):
#         self.room_name = room_name
#         self.current_temp = current_temp
#         self.target_temp = target_temp

#     def check_status(self):
#         if self.current_temp>self.target_temp:
#             print(f"turning on the AC")
#         elif self.current_temp<self.target_temp:
#             print(f"turning on the heater")
#         else:
#             print("the temperature is perfect")
    
#     def change_target(self, new_target:int):
#         self.target_temp = new_target

# thermostat1 = ThermoStat("living_room", 25, 20)
# thermostat1.check_status()
# thermostat1.change_target(28)
# thermostat1.check_status()




""" Encapsulation: hiding or protecting data from the outside world
and validating it first."""
# class ThermoStat:
#     def __init__(self, room_name:str, current_temp:int, target_temp:int):
#         self.room_name = room_name
#         self.current_temp = current_temp
#         self.target_temp = target_temp

#     def check_status(self):
#         if self.current_temp>self.target_temp:
#             print(f"turning on the AC")
#         elif self.current_temp<self.target_temp:
#             print(f"turning on the heater")
#         else:
#             print("the temperature is perfect")
    
#     def change_target(self, new_target:int):
#         #incapsulating/protecting from bad data
#         if 15<=new_target<=30:
#             self.target_temp = new_target
#         else:
#             print(f"safety hazard! cannot change temperature to {new_target}")

# thermostat1 = ThermoStat("living_room", 25, 20)
# thermostat1.check_status()
# thermostat1.change_target(99)




"inheritance"
# class ThermoStat:
#     def __init__(self, room_name:str, current_temp:int, target_temp:int):
#         self.room_name = room_name
#         self.current_temp = current_temp
#         self.target_temp = target_temp

#     def check_status(self):
#         if self.current_temp>self.target_temp:
#             print(f"turning on the AC")
#         elif self.current_temp<self.target_temp:
#             print(f"turning on the heater")
#         else:
#             print("the temperature is perfect")
    
#     def change_target(self, new_target:int):
#         #incapsulating/protecting from bad data
#         if 15<=new_target<=30:
#             self.target_temp = new_target
#         else:
#             print(f"safety hazard! cannot change temperature to {new_target}")

# class SmartThermoStat(ThermoStat):
#     def __init__(self, room_name:str, current_temp:int, target_temp:int, initial_wifi_status:bool):
#         super().__init__(room_name, current_temp, target_temp)
#         self.is_wifi_connected = initial_wifi_status

#     def toggle_wifi(self):
#         self.is_wifi_connected = not self.is_wifi_connected
#         print(f"the wifi connection is now {self.is_wifi_connected}")
#         if self.is_wifi_connected == True:
#             print(f"sending notification phone...the wifi connection to {self.room_name} is {self.is_wifi_connected}")
#         else:
#             print(f"sending notification phone...the wifi connection to {self.room_name} is {self.is_wifi_connected}")

# thermostat1 = SmartThermoStat("living_room", 20, 20, False)
# thermostat1.check_status()
# thermostat1.toggle_wifi()




"method - overriding"
# class ThermoStat:
#     def __init__(self, room_name:str, current_temp:int, target_temp:int):
#         self.room_name = room_name
#         self.current_temp = current_temp
#         self.target_temp = target_temp

#     def check_status(self):
#         if self.current_temp>self.target_temp:
#             print(f"turning on the AC")
#         elif self.current_temp<self.target_temp:
#             print(f"turning on the heater")
#         else:
#             print("the temperature is perfect")
    
#     def change_target(self, new_target:int):
#         #incapsulating/protecting from bad data
#         if 15<=new_target<=30:
#             self.target_temp = new_target
#         else:
#             print(f"safety hazard! cannot change temperature to {new_target}")

# class SmartThermoStat(ThermoStat):
#     def __init__(self, room_name:str, current_temp:int, target_temp:int, initial_wifi_status:bool):
#         super().__init__(room_name, current_temp, target_temp)
#         self.is_wifi_connected = initial_wifi_status

#     def toggle_wifi(self):
#         self.is_wifi_connected = not self.is_wifi_connected
#         print(f"the wifi connection is now {self.is_wifi_connected}")
#         if self.is_wifi_connected == True:
#             print(f"sending notification phone...the wifi connection to {self.room_name} is {self.is_wifi_connected}")
#         else:
#             print(f"sending notification phone...the wifi connection to {self.room_name} is {self.is_wifi_connected}")
    
#     def check_status(self):
#         super().check_status()
#         if self.is_wifi_connected:
#             print("[SMART ALERT]: the device is now connected to the cloud server")
#         else:
#             print("[OFFLINE]: the state is not synced")

# thermostat1 = SmartThermoStat("living_room", 20, 20, False)
# thermostat1.change_target(999)
