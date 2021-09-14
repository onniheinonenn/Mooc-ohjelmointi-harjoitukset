
import requests


class Target:
    
    def __init__(self, siteName, address):
        self.name = siteName
        self.address = address
        self.server = ""
        self.ip = ""

    def setServer(self):
        result = requests.get(self.address)
        
        self.server = result.headers["Server"]

    def setAddress(self, address):
        self.ip = address

    def printData(self):
        print("\nWebsite info:")
        print("Site name: " + self.name)
        print("Server: " + self.server) 
        print("Site IP: " + self.ip)

        print("\n")


zerobank = Target("Zerobank", "http://zero.webappsecurity.com/")
zerobank.setServer()
zerobank.setAddress("54.82.22.214")
zerobank.printData()

canvas = Target("Canvas", "https://canvas.academy.se/")
canvas.setServer()
canvas.setAddress("52.51.210.96")
canvas.printData()

git = Target("GitHub", "https://github.com/")
git.setServer()
git.setAddress("140.82.121.4")
git.printData()
