import requests
import json
import utilities as utl

# r = requests.get('https://thedivisiontab.com/api/search.php?name=Targgus&platform=uplay')

# data = json.loads(r.text)

# pid = data['results'][0]['pid']

# print(pid)

# r2 = requests.get('https://thedivisiontab.com/api/player.php?pid='+pid)

# playerData = json.loads(r2.text)

# killCount = playerData['kills_total']

# print(killCount)

name = 'Targgus'
baseInfo = utl.getBaseInfo(name)
print(baseInfo)
