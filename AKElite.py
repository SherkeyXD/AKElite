import json
import wget
import os


def download_png(listname, catename):
    for line in listname:
        url = "https://prts.wiki/w/Special:Filepath/头像_敌人_" + line + ".png"
        filename = line + ".png"
        filepath = "./assets/" + catename + "/"
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        if filename not in os.listdir(filepath):
            wget.download(url, out=os.path.join(filepath, filename))



normal = []
elite = []
boss = []

url = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/enemy_handbook_table.json"

#if os.path.exists("data.json"):
#    os.remove("data.json")
#    wget.download(url, out='data.json')
#else: 
#    wget.download(url, out='data.json')

with open('data.json', encoding='utf-8') as fr:
    enemy_data = json.load(fr)

for enemy in enemy_data.values():
    if enemy['enemyLevel'] == 'NORMAL':
        if enemy['hideInHandbook'] != 'true':
            normal.append(enemy['name'])
    elif enemy['enemyLevel'] == 'ELITE':
        if enemy['hideInHandbook'] != 'true':
            elite.append(enemy['name'])
    elif enemy['enemyLevel'] == 'BOSS':
        if enemy['hideInHandbook'] != 'true':
            boss.append(enemy['name'])

download_png(normal, 'normal')
#download_png(elite, 'elite')
#download_png(boss, 'boss')

#f = open("normal.md", "w", encoding='utf-8')
#for line in normal:
#    f.write( '!['+line+']' +'('+'assets/normal/'+line+'.png)' + '\n')

#f = open("elite.md", "w", encoding='utf-8')
#for line in elite:
#    f.write( '!['+line+']' +'('+'assets/elite/'+line+'.png)' + '\n')

#f = open("boss.md", "w", encoding='utf-8')
#for line in boss:
#    f.write( '!['+line+']' +'('+'assets/boss/'+line+'.png)' + '\n')