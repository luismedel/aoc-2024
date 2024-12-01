
import os
from pathlib import Path
import sys
import requests
import markdownify
from bs4 import BeautifulSoup
from datetime import datetime


# Quick .env management
env = dict(line.strip().split('=', maxsplit=1) for line in open('.env', 'r').readlines())

SESSION = env.get('AOC_SESSION', os.environ.get('AOC_SESSION', None))
if not SESSION:
    raise Exception('Missing AOC_SESSION environment variable')

auto_part = False

if len(sys.argv) < 2:
    now = datetime.now()
    year, day = now.year, now.day
else:
    year, day = sys.argv[1].split('/', maxsplit=1)

if len(sys.argv) < 3:
    part = 1
    auto_part = True
else:
    part = int(sys.argv[2])

dir_name = f'{day:02d}/{part:02d}'

if int(part) == 1 and auto_part and os.path.isdir(dir_name):
    part = 2
    dir_name = f'{day:02d}/{part:02d}'

if Path.is_dir(Path(dir_name)):
    raise Exception(f'Directory {dir_name} already exists')

headers = { 'cookie': f'session={SESSION}' }
page = requests.get(f"https://adventofcode.com/{year}/day/{day}", headers=headers)
input = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
text = soup.find_all('article')[int(part) - 1]
md = markdownify.markdownify(str(text), heading_style="ATX")

os.makedirs(dir_name, exist_ok=True)

with open(f'{dir_name}/input.txt', 'w') as f:
    f.write(input.content.decode())

with open(f'{dir_name}/README.md', 'w') as f:
    f.write(md)
