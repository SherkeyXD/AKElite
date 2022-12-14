import json
import wget
import os


def get_data(fileurl, filename):
    if os.path.exists(filename):
        os.remove(filename)
        wget.download(url, out=filename)
    else: 
        wget.download(url, out=filename)
    print("\nData updated.")


def download_png(listname, catename):
    for line in listname:
        url = "https://prts.wiki/w/Special:Filepath/头像_敌人_" + line + ".png"
        if '"' in line:
            line = '“' + line.strip('"') + '”'  # 将英文引号转换为中文，避免引起markdown混乱
        filename = line + ".png"
        filepath = "./assets/" + catename + "/"
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        if filename not in os.listdir(filepath):
            wget.download(url, out=os.path.join(filepath, filename))
    print(f"\033[32m\n {catename.title()} pictures updated.\033[0m")


normal = []
elite = []
boss = []

url = "https://ghproxy.com/https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/enemy_handbook_table.json"

get_data(url, "data.json")

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

download_png(normal, 'normal')
download_png(elite, 'elite')
download_png(boss, 'boss')


f = open("./docs/src/enemy/normal.md", "w", encoding='utf-8')
f.write('---\ntitle: 普通敌人\npermalink: /normal\n---\n')
for line in normal:
    if '"' in line:
        line = '“' + line.strip('"') + '”'
    f.write(f'![{line}](https://img.sherkey.ml:8088/normal/{line}.png "{line}")\n')

f = open("./docs/src/enemy/elite.md", "w", encoding='utf-8')
f.write('---\ntitle: 精英敌人\npermalink: /elite\n---\n')
for line in elite:
    if '"' in line:
        line = '“' + line.strip('"') + '”'
    f.write(f'![{line}](https://img.sherkey.ml:8088/elite/{line}.png "{line}")\n')

f = open("./docs/src/enemy/boss.md", "w", encoding='utf-8')
f.write('---\ntitle: 领袖敌人\npermalink: /boss\n---\n')
for line in boss:
    if '"' in line:
        line = '“' + line.strip('"') + '”'
    f.write(f'![{line}](https://img.sherkey.ml:8088/boss/{line}.png "{line}")\n')

print("\nMarkdown files generated.")

os.system("cd docs && git add .")
os.system('git commit -m "Site update on $(TZ=UTC-8 date +%Y-%m-%d" "%H:%M:%S)"')
os.system("git push -f")