# IPGEO
 Free IP Geolocation API and IP Location Lookup

### Install
---------
```python
pip install ipgeo-namdevel
```

Usage (Install from PIP)
---------
```python
from namdevel.ipgeo import IPGeoLoc

if __name__ == "__main__":
    app = IPGeoLoc()
    app.setIp("8.8.8.8")
    isProxy = app.getResult().isProxy()
    print(isProxy)

```

### Usage (Download Source)
---------
```python
from src.namdevel.ipgeo import IPGeoLoc

if __name__ == "__main__":
    app = IPGeoLoc()
    app.setIp("8.8.8.8")
    isProxy = app.getResult().isProxy()
    print(isProxy)

```
