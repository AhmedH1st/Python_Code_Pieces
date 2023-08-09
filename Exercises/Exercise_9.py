#script to print All System Info 
import platform
import psutil

#print OS running type
print("Platform :"+platform.platform())
#print processor type
print("Processor :"+platform.processor())
#print architectural detail
print("architecture :",platform.architecture(),"\n")
#print Memory Size & Usage
print("Memory :",psutil.virtual_memory(),"\n")
#print PC IPv4, IPv6, Mac Address
print("Network info :",psutil.net_if_addrs(),"\n")
#print PC Internal Temperature
print("Temp :",psutil.sensors_temperatures(),"\n")



#for more APIs visit https://pypi.org/project/psutil/ 
