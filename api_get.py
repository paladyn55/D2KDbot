import requests

# dictionary to hold extra headers
HEADERS = {"X-API-Key": "898ee44d41714955909f5b4929cfd45a"}

miniId = "4611686018431617573"
platform = "2"

r = requests.get("https://www.bungie.net/platform/Destiny2/" + platform + "/Account/" + miniId + "/Stats/?modes=5",
                 headers=HEADERS)
response = r.json()
characterStats = response["Response"]["mergedAllCharacters"]

lifetimeKD = characterStats["results"]["allPvP"]["allTime"]["killsDeathsRatio"]["basic"]["value"]

print("Lifetime kd:", lifetimeKD)
