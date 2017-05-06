y=1
z=2
x="Michael"
print("Hello my World")
print(8)
print(12+12)
print(x)
print(y+z)
hostname1="192.168.1.1"
hostname2="172.16.1.1"
hostname3="10.0.0.1"
print("The main hostname is: {}".format(hostname1))
print(" Hostname 1: {} \n Hostname 2: {} \n Hostname 3: {}".format(hostname1, hostname2, hostname3))
import os
os.system("ping -c 1 8.8.8.8")
response = os.system("ping -c 1 8.8.8.8")
print("Ito ang output:")
print(response)
var = 0
if var == 0:
    print("Var is equal to zero")
elif var == 1:
    print("Var is equal to one")
else:
    print("Var is not zero or one")
