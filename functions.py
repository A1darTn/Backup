import requests
import json




def getting_an_ID():
    while True:
        user_id = input(f'Для загрузки фотографий необоходимо ввести ID пользователя: ')
        if user_id.isdigit():
            return user_id
        else:
            print(f'Вы неправильно ввели ID пользователя(ID должно содержать только числа)')


def receiving_the_album():
    while True:
        album_id = None
        album_int = input(f'Выберите альбом из которого хотите совершить загрузку:\n1 - фотографии со стены\n2 - фотографии профиля\n')
        if album_int == '1':
            album_id = 'wall'
            return album_id
        elif album_int == '2':
            album_id = 'profile'
            return album_id
        else:
            print(f'Выберите 1 или 2')


def getting_the_number_of_photos():
    while True:
        count = input(f'Введите количество желаемых фотографий(по умолчанию количество равно 5): ')
        if count.isdigit():
            count = int(count)
            return count
        else:
            print(f'Вы ввели не число, пожалуйста, введите число желаемых фотографий')


def list_likes(photos):
    list_likes_photo = []
    for dict_info_photo in photos['response']['items']:
        for i in dict_info_photo:
            list_likes_photo.append(str(dict_info_photo['likes']['count']))
            break
    return list_likes_photo


def upload_images_comp(photos):
    list_json_info_photo = []
    for dict_info_photo in photos['response']['items']:
            photo_info_dict = {}
            name = dict_info_photo['sizes']
            name_file = str(dict_info_photo['likes']['count'])
            for index in range(len(name)):
                if name[index]['type'] == 'w':
                    response = requests.get(name[index]['url'])
                    with open(name_file, 'wb') as f:
                        f.write(response.content)
                    photo_info_dict['file_name'] = f'{name_file}.jpg'
                    photo_info_dict['size'] = name[index]['type']
            list_json_info_photo.append(photo_info_dict)
    with open ('photo.json', 'w') as f:
        json.dump(list_json_info_photo, f, indent=4)
                    
