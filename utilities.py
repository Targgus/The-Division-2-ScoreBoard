import requests
import json

class stats():
    def __init__(self, name, level, time):
        self.name = name
        self.level = level
        self.time = time

class kills():
    def __init__(self, killsTotal,
    killsBleeding, killsShocked,
    killsBurning, killsEnsnare,
    killsHeadshots, killsSkill,
    killsTurret):
        self.killsTotal = killsTotal
        self.killsBleeding = killsBleeding
        self.killsShocked = killsShocked
        self.killsBurning = killsBurning
        self.killsEnsnare = killsEnsnare
        self.killsHeadshots = killsHeadshots
        self.killsSkill = killsSkill
        self.killsTurret = killsTurret

class weaponKills():
    def __init__(self, pistolKills,
    grenadeKills, smgKills,
    shotgunKills, rifleKills, specKills):
        self.pistolKills = pistolKills
        self.grenadeKills = grenadeKills
        self.smgKills = smgKills
        self.shotgunKills = shotgunKills
        self.rifleKills = rifleKills
        self.specKills = specKills


def getBaseInfo(userName):
    r1 = requests.get('https://thedivisiontab.com/api/search.php?name='+userName+'&platform=uplay')
    data = json.loads(r1.text)
    return data

def getAdvancedStates(pid):
    r2 = requests.get('https://thedivisiontab.com/api/player.php?pid='+pid)
    data = json.loads(r2.text)
    return data