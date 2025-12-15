import requests
from bs4 import BeautifulSoup
import json

r = requests.get('https://news.ycombinator.com/')

html = r.text
soup = BeautifulSoup(html, 'html.parser')

news_data = []
titles = soup.find_all('span', class_='titleline')

for title in titles:
    link_tag = title.find('a')
    if link_tag:
        news_item = {
            'title': link_tag.text,
            'url': link_tag['href']
        }
        news_data.append(news_item)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(news_data, f, ensure_ascii=False, indent=2)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=`, initial-scale=1.0">
    <title>Срочные новости в криминальном мире хакинга</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1a1a2e;
            color: white;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: #16213e;
            padding: 20px;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        }
        
        h1 {
            text-align: center;
            color: #ffcc00;
            text-shadow: 0 0 10px rgba(255,204,0,0.5);
            border-bottom: 3px solid #ffcc00;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }
        
        .stats {
            background: #0f3460;
            padding: 10px;
            margin-bottom: 20px;
            text-align: center;
            font-size: 18px;
            border: 2px solid #ffcc00;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #dc51f5;
            overflow: hidden;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
        }
        
        th {
            background: linear-gradient(#55fa89);
            color: white;
            padding: 15px;
            text-align: left;
            font-size: 18px;
            border-right: 2px solid #1a1a2e;
        }
        
        td {
            padding: 15px;
            border-bottom: 2px solid #1a1a2e;
            border-right: 2px solid #1a1a2e;
            font-size: 16px;
        }


        .title {
            color: #ffffff;
            font-weight: bold;
        }
        
        .url {
            color: #72efdd;
            font-size: 14px;
            word-break: break-all;
        }
        
    </style>
</head>
<body bgcolor="#c0c0c0">
<table>
    <thead>
        <tr>
            <th width="50">#</th>
            <th>ЗАГОЛОВОК НОВОСТИ</th>
            <th width="300">ССЫЛКА НА ИСТОЧНИК</th>
        </tr>
    </thead>
<tbody>''')
    for i, news in enumerate(news_data, 1):
        
        f.write(f'''
            <tr class>
                <td class="number">{i}</td>
                <td class="title">{news['title']}</td>
                <td class="url"><a href="{news['url']}" target="_blank">{news['url']}</a></td>
            </tr>
''')
    f.write('''</body>
        </html>''')