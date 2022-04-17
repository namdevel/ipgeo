import requests
import json

API_URL = "https://api.namdevel.rest"

class IPGeoLoc(object):

    def __init__(self):
        self.ip = ""
        self.res = ""

    def setIp(self, ip):
        self.ip = ip

    def getIp(self):
        return self.ip

    def getResult(self):
        try:
            res = requests.get(API_URL + "/v1/ip_address/" + self.ip)
            self.response = res.text
        except Exception:
            print("Unknown error")
            
        return self

    def continent(self):
        return self.parse()["continent"]

    def continentCode(self):
        return self.parse()["continentCode"]

    def country(self):
        return self.parse()["country"]

    def countryCode(self):
        return self.parse()["countryCode"]

    def region(self):
        return self.parse()["region"]

    def regionName(self):
        return self.parse()["regionName"]

    def city(self):
        return self.parse()["city"]

    def district(self):
        return self.parse()["district"]

    def zip(self):
        return self.parse()["zip"]

    def lat(self):
        return self.parse()["lat"]

    def lon(self):
        return self.parse()["lon"]

    def timezone(self):
        return self.parse()["timezone"]

    def offset(self):
        return self.parse()["offset"]

    def currency(self):
        return self.parse()["currency"]

    def isp(self):
        return self.parse()["isp"]

    def org(self):
        return self.parse()["org"]

    def asn(self):
        return self.parse()["as"]

    def asname(self):
        return self.parse()["asname"]

    def isMobile(self):
        return self.parse()["mobile"]

    def isProxy(self):
        return self.parse()["proxy"]

    def isHosting(self):
        return self.parse()["hosting"]

    def parse(self):
        return json.loads(self.response)
