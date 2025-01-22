import requests
import os



class Vk:
    def __init__(self, token, version='5.131'):
        self.params = {
            'access_token': token,
            'v': version
        }
        self.base = 'https://api.vk.com/method/'

    def get_photos(self, user_id, album_id, count=5):
        url = f'{self.base}photos.get'
        params = {
            'owner_id': user_id,
            'album_id': album_id,
            'extended': 1,
            'count': count
        }
        params.update(self.params)
        response = requests.get(url, params=params)
        return response.json()


class Yd:
    def __init__(self, token):
        self.headers = {
            'Authorization': token
        } 

    def creating_a_folder(self, name_path):
        try:
            print('Создание папки для фотографий')
            url = 'https://cloud-api.yandex.net/v1/disk/resources?'
            self.params = {
                'path': name_path
            }
            response = requests.put(url, params=self.params, headers=self.headers)
            print('Папка успешно создана')
        except:
            print('Отсутсвует интернет соединение')

    def file_upload_url(self, list_likes, name_path):
        print(f'Производится отправка фотографий на Яндекс Диск')
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        number_of_photos_sent = 0
        for file_name in list_likes:
            params = {
                'path': f'{name_path}/{file_name}'
            }
            response = requests.get(url, params=params, headers=self.headers)
            url_upload_yd = response.json()['href']
            with open(file_name, 'rb') as f:
                requests.put(url_upload_yd, files={'file': f})
            os.remove(file_name)
            number_of_photos_sent += 1
        print(f'Отправлено фотографий {number_of_photos_sent} из {len(list_likes)}')