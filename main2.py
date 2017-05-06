import os
hostname1="8.8.8.8"
hostname2="8.8.8.4"
hostname3="192.168.1.1"
hostname4="192.168.1.2"

response1 = os.system("ping {} -q -c1 > /dev/null".format(hostname1))
response2 = os.system("ping {} -q -c1 > /dev/null".format(hostname2))
response3 = os.system("ping {} -q -c1 > /dev/null".format(hostname3))
response4 = os.system("ping {} -q -c1 > /dev/null".format(hostname4))

if response1 == 0:
    print("{}: Reachable".format(hostname1))
else:
    print("{}: Unreachable".format(hostname1))

if response2 == 0:
    print("{}: Reachable".format(hostname2))
else:
    print("{}: Unreachable".format(hostname2))

if response3 == 0:
    print("{}: Reachable".format(hostname3))
else:
    print("{}: Unreachable".format(hostname3))

if response4 == 0:
    print("{}: Reachable".format(hostname4))
else:
    print("{}: Unreachable".format(hostname4))