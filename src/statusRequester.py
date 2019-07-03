import requests, settings

def FetchLeagueStatusData():
    response = requests.get('https://euw1.api.riotgames.com/lol/status/v3/shard-data?api_key=' + settings.API_KEY)
    data = response.json()
    return data

def DataFormatterStore(data):
    CheckServerStatusClient(data)    
    print("Server name: " + data['name'])
    print("Platform: " + data['services'][0]['name'])
    print("Status: " + data['services'][0]['status'])
    # print("Updated: " + data['services'][0]['incidents'][0]['updates'][0]['updated_at'])
    for probs in data['services'][0]:
        print("Problems: ", len(probs))
    print("\t")

def DataFormatterClient(data):
    CheckServerStatusClient(data)  
    print("Server name: " + data['name'])
    print("Platform: " + data['services'][3]['name'])
    print("Status: " + data['services'][3]['status'])
    print("Updated: " + data['services'][3]['incidents'][0]['updates'][0]['updated_at'])
    for probs in data['services'][0]:
        print("Problems: ", len(probs))
    print("\t")

def CheckServerStatusStore(data):
    if data['services'][0]['status'] == "offline":
        while data['services'][0]['status'] == "offline":
            print("EUW CURRENTLY DOWN")                
    else:pass

def CheckServerStatusClient(data):
    if data['services'][3]['status'] == "offline":
        while data['services'][3]['status'] == "offline":
            print("EUW CURRENTLY DOWN")                
    else:pass

data = FetchLeagueStatusData()
DataFormatterStore(data)
DataFormatterClient(data)

