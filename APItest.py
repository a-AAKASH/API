import requests
import json

url = "https://api.uptimerobot.com/v2/getMonitors"
          
## start of 'last week' i.e. 19 June 2022, 0000 hours IS 1655679600
## end of 'last week' i.e. 26 June 2022, 2400 hours IS 1656284400

payload = {"api_key" : "ur828173-4544bcf8143509466865be09",
            "monitors" : "790608131-784355743-784355767-784355758-784355759",
            "log_types" : "1-99-98", 
            #"logs_start_date" : "1655679600",
            #"logs_end_date" : "1656284400",
            #"custom_uptime_ratios" : "7",
            #"custom_uptime_ranges" : "1655679600_1656284400",
            "logs_limit" : "1",
            "logs" : "1"
            #"statuses" : "2"
            } 
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)
          
#prettyjson = json.loads(response.text)
#print(json.dumps(prettyjson, indent=1))

#print(response.json())

#jsonFile = open("data.json", "w")
#jsonFile.write(json.dumps(prettyjson, indent=1))
#jsonFile.close()

jsonString = json.dumps(response.json(), indent=1)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()