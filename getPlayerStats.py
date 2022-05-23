def stat_get(bungieName, b_num):
    import requests
    # the first area is just to get bungie ID and platform from bungie name
    # dictionary to hold extra headers
    HEADERS = {"X-API-Key": "898ee44d41714955909f5b4929cfd45a"}

    bungieNum = b_num.strip("#")

    names = requests.post("https://www.bungie.net/platform/User/Search/GlobalName/0", "",
                          {"displayNamePrefix": bungieName}, headers=HEADERS)

    response = names.json()

    for user in response["Response"]["searchResults"]:
        if user["bungieGlobalDisplayNameCode"] == int(bungieNum):
            membershipType = str(user["destinyMemberships"][0]["crossSaveOverride"])
            membershipId = user["destinyMemberships"][0]["membershipId"]
            if membershipType == "0":
                str(user["destinyMemberships"][0]["membershipType"])

    # --------------------------------------------------------------------------------------------------
    stats = requests.get(
        "https://www.bungie.net/platform/Destiny2/" + membershipType + "/Account/" + membershipId + "/Character/0/Stats/?groups=General&modes=10,12,37,84",
        headers=HEADERS)
    statsJson = stats.json()
    characterStats = statsJson["Response"]

    controlKD = characterStats["control"]["allTime"]["killsDeathsRatio"]["basic"]["value"]
    controlKillVolume = characterStats["control"]["allTime"]["kills"]["pga"]["value"]
    controlEfficiency = characterStats["control"]["allTime"]["efficiency"]["basic"]["value"]
    controCR = characterStats["control"]["allTime"]["combatRating"]["basic"]["value"]

    clashKD = characterStats["clash"]["allTime"]["killsDeathsRatio"]["basic"]["value"]
    clashKillVolume = characterStats["control"]["allTime"]["kills"]["pga"]["value"]
    clashEfficiency = characterStats["clash"]["allTime"]["efficiency"]["basic"]["value"]
    clashCR = characterStats["clash"]["allTime"]["combatRating"]["basic"]["value"]

    trialsKD = characterStats["trials_of_osiris"]["allTime"]["killsDeathsRatio"]["basic"]["value"]
    trialsEfficiency = characterStats["trials_of_osiris"]["allTime"]["efficiency"]["basic"]["value"]
    trialsCR = characterStats["trials_of_osiris"]["allTime"]["combatRating"]["basic"]["value"]

    averageKD = (controlKD + clashKD + trialsKD) / 3
    averageEfficiency = (controlEfficiency + clashEfficiency + trialsEfficiency) / 3
    averageCR = (controCR + clashCR + trialsCR) / 3

    print("Average KD:", averageKD)
    # print("Average Efficiency:", averageEfficiency)
    # print("Average CR:", averageCR)
    return averageKD
