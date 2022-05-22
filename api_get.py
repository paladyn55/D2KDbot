import requests
import os
import pprint
key = os.environ['BNG_KEY']
# dictionary to hold extra headers
HEADERS = {"X-API-Key": key}

def stat_get(ID, platform):
	r = requests.get("https://www.bungie.net/platform/Destiny2/" + platform + "/Account/" + ID + "/Stats/?groups=General&modes=10,12,37,84", headers=HEADERS)
	response = r.json()
	characterStats = response["Response"]["mergedAllCharacters"]

	lifetimeKD = characterStats["results"]["allPvP"]["allTime"]["killsDeathsRatio"]["basic"]["value"]
	print("Lifetime kd:", lifetimeKD)

	
	
