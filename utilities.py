import requests
import json

class baseInfo():
    def __init__(self, name, level, pid):
        self.name = name
        self.level = level
        self.pid = pid

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

    def array(self):
        return [self.killsTotal, self.killsBleeding, self.killsShocked,
                self.killsBurning, self.killsEnsnare, self.killsHeadshots, self.killsSkill,
                self.killsTurret]

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
    return data['results'][0]

def getAdvancedStats(pid):
    r2 = requests.get('https://thedivisiontab.com/api/player.php?pid='+pid)
    data = json.loads(r2.text)
    return data