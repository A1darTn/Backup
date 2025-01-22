import configparser
import requests
import json
import os
from models import Vk, Yd
from functions import getting_an_ID, receiving_the_album, getting_the_number_of_photos, list_likes, upload_images_comp



def main():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    vk_token = config['Tokens']['vk_token']

    token_yd = str(input('Введите ваш токен ЯндексДиск: '))
    vk = Vk(vk_token)
    yd = Yd(token_yd)

    try:
        photos_vk = vk.get_photos(getting_an_ID(), receiving_the_album(), getting_the_number_of_photos())
        folder_name = input(f'Придумайте название для папки: ')
        yd.creating_a_folder(folder_name)

        list_likes_save_photo = list_likes(photos_vk)

        upload_images_comp(photos_vk)

        yd.file_upload_url(list_likes_save_photo, folder_name)
    except:
        print(f'Отсутсвует соединие, пожалуйста, подключитесь к сети')

if __name__ == '__main__':
    main()