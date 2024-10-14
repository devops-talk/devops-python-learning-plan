# 2. Class Inheritance
# Problem: Create a base class Device with attributes name and status. Derive a class Smartphone that adds the attribute apps. Add methods to:
# Display the device details.
# Install apps on the smartphone.
# Objective: Learn about inheritance and method overriding.



class Device:
    def __init__(self, name, status):
        self.name = name  
        self.status = status  
    def display_details(self):
        print(f"Device Name: {self.name}")
        print(f"Device Status: {self.status}")

class Smartphone(Device):
    def __init__(self, name, status):
        super().__init__(name, status) 
        self.apps = []
    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"App '{app_name}' installed.")
    def display_details(self):
        super().display_details() 
        print(f"Installed Apps: {', '.join(self.apps) if self.apps else 'No apps installed'}")

my_phone = Smartphone("iPhone", "On")
my_phone.display_details()
my_phone.install_app("WhatsApp")
my_phone.install_app("Instagram")
my_phone.display_details()