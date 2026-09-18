import subprocess
import os

def check(var):
    global x
    print("\033[H\033[2J", end="")
    print(globals().get(var))
    x = input("is this correct [Y,n]: ")
    if x == "n" or x == "N":
       globals()[var] = input(f"Type your {var}: ")

print("\033[H\033[2J", end="")
print("An simple python application for adding networks in wpa_supplicant")
print()

rooti = subprocess.run(["whoami"], capture_output=True, text=True) 
root = rooti.stdout.strip()

if root == "root":
    ssid = input("Type your ssid: ")
    x = "dummy"
    while x == "dummy" or x == "n" or x == "N":
        check("ssid")

    paswd = input("Type your password: ")
    x = "dummy"
    while x == "dummy" or x == "n" or x == "N":
        check("paswd")

    result = subprocess.run(["wpa_passphrase", f"{ssid}", f"{paswd}"], capture_output=True, text=True)
    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a") as f:
        f.write(result.stdout)
    print("Added network", ssid, "to wpa_supplicant.conf")

else :
    print("You arent running as root")
