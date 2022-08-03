import json
import wget
import os


def get_data(fileurl, filename):
    if os.path.exists(filename):
        os.remove(filename)
        wget.download(url, out=filename)
    else: 
        wget.download(url, out=filename)


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

url = "https://ghproxy.com/https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/enemy_handbook_table.json"

#get_data(url, "data.json")

with open("data.json", encoding='utf-8') as fr:
    enemy_data = json.load(fr)

for enemy in enemy_data.values():
    if enemy['enemyLevel'] == 'NORMAL':
        if not enemy['hideInHandbook']:
            normal.append(enemy['name'])
    elif enemy['enemyLevel'] == 'ELITE':
        if not enemy['hideInHandbook']:
            elite.append(enemy['name'])
    elif enemy['enemyLevel'] == 'BOSS':
        if not enemy['hideInHandbook']:
            boss.append(enemy['name'])

#download_png(normal, 'normal')
#download_png(elite, 'elite')
#download_png(boss, 'boss')


f = open("normal.md", "w", encoding='utf-8')
f.write('---\ntitle: 普通敌人\npermalink: /normal\n---\n')
for line in normal:
    f.write(f'![{line}](http://124.223.3.107:8088/normal/{line}.png "{line}")\n')


f = open("elite.md", "w", encoding='utf-8')
f.write('---\ntitle: 精英敌人\npermalink: /elite\n---\n')
for line in elite:
    f.write(f'![{line}](http://124.223.3.107:8088/elite/{line}.png "{line}")\n')

i = 0
l = len(boss)
f = open("boss.md", "w", encoding='utf-8')
f.write('---\ntitle: 领袖\npermalink: /boss\n---\n')
for line in boss:
    f.write( '| !['+line+']' +'('+'http://124.223.3.107:8088/boss/'+line+'.png) ')
    i += 1
    if i == l:
        f.write('|\n')
        for n in range (1, l+1):
            f.write('| - ')
        f.write('|\n')
for line in boss:
    f.write('| '+line+' ')
f.write('|')
    
    

        