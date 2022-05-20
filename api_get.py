import requests
import os
import pprint
key = os.environ['BNG_KEY']
# dictionary to hold extra headers
HEADERS = {"X-API-Key": key}

def stat_get(ID, platform):
	usr = requests.get("https://bungie.net/platform/" + f"/Destiny2/{platform}/Account/{ID}/Character/0/Stats/", headers=HEADERS)
	usr = usr.json()
	pprint.pprint(dir(usr.values))
	
	r = requests.get("https://www.bungie.net/platform/Destiny2/" + platform + "/Account/" + ID + "/Stats/?mode=84", headers=HEADERS)
	response = r.json()
	characterStats = response["Response"]["mergedAllCharacters"]
	#activity numbers: trials - 84, comp - 69 (eyyy), valor - 70, alllllll pvp - 5 (only seasonal stat used)
	#for stat in response['Response']['mergedAllCharacters']['results']:
	#	print(stat)
	lifetimeKD = characterStats["results"]["allPvP"]["allTime"]["killsDeathsRatio"]["basic"]["value"]
	#print(characterStats["results"]["trials"].keys())
	print("Lifetime kd:", lifetimeKD)
	
