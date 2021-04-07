import os
import IP2Location

#---------------------------------
database = IP2Location.IP2Location(os.path.join("data", "IPV6-COUNTRY.BIN"))
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#rec = database.get_all(IP_ADDRESS)
#//////////////////////////////////////
ipaddress = input("ip address")
ws = IP2Location.IP2LocationWebService("demo","WS24",True)
rec = ws.lookup(ipaddress, ["continent", "country", "region", "city", "geotargeting", "country_groupings", "time_zone_info"], "en")
print (rec)
#------------------------------------------












