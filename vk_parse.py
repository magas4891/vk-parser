import csv
import requests
import time

def get_1000_posts():
    token = 'ENTER_API_KEY'
    version = 5.103
    domain = 'rammsteinrepublik'
    count = 100
    offset = 0
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )

        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        time.sleep(0.5)
        return all_posts


def file_writer(data):
    with open('rammsteinrepublik.csv', 'w', errors='ignore') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            a_pen.writerow((post['likes']['count'],
                            post['text'],
                            img_url
                            ))

all_posts = get_1000_posts()
file_writer(all_posts)