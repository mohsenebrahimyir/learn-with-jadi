class Device:
    count = 0
    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac_address = mac
        self.name = name
        Device.count += 1
        #TODO: result = ping the device
        if result:
            self.status = "active"
        else:
            self.status = "unknown"
        def get_status(self):
            """
            TODO: return result based on 
            ping results for self
            """
            pass

class TV(Device):
    def turn_on(self):
        #TODO: connect to self.ip and turn on
        pass
    def turn_off(self):
        #TODO: connect to self.ip and turn off
        pass

class Thermo(Device):
    def get_temp(self):
        """
        TODO: connect to self.ip and read 
        temperature and return the result
        """
        pass

class SmartTV(TV):
    def turn_on(self):
        # turn on the smart tv from self.ip
        pass
