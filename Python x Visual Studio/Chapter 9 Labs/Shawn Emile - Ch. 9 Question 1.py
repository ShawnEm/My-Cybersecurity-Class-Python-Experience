IPs = {
    "IPhone": "192.168.1.2",
    "MacBook": "192.168.1.3",
    "Smart TV": "192.168.1.4",
    "BT Speaker": "192.168.1.5",
    "Xbox Series X": "192.168.1.6"
}
x = input("Is this device in the dictionary?: ")
if (x) in IPs:
    print(f"Yes, heres the IP address: {IPs[x]}")
else:
    print("Not in dictionary.")
print("Proccess Complete")