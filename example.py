from src.namdevel.ipgeo import IPGeoLoc

if __name__ == "__main__":
    app = IPGeoLoc()
    app.setIp("8.8.8.8")
    isProxy = app.getResult().isProxy()
    print(isProxy)
