from pprint import pprint
import requests

TOKEN = '2619421814940190'
urls = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
]

def requests_get(urls): #Функция получения http запроса
    # принимает список адресов
    r = (requests.get(url) for url in urls)
    return r

def superheros_intelligence(): #Функция Получения супер интелекта
    superhero = []
    for item in requests_get(urls): #проходим по списку
        intelligence = item.json() # и получаем информацию с запросов
        for results in intelligence['results']: #Получаем значения из results
            superhero.append({'name': results['name'],
                                      'intelligence': results['powerstats']['intelligence']})#Создаем список из словарей
    # return superhero

    superheros_intelligence = 0 #для послдеюющего сравнения
    name = '' #для имен
    for intelligence in superhero: #Цикл для получения интелекта герооев
        if superheros_intelligence < int(intelligence['intelligence']): #Условие на сравнение интелекта
            superheros_intelligence = int(intelligence['intelligence']) #каждый проход цикла получаем нове значение и сравнием со старым
            name = intelligence['name'] #Получаем имена
    print(f"Самый интелектуальный {name}, интелект: {superheros_intelligence}")

# if __name__ == '__main__':
#     superheros_intelligence()


class YaUploader: #Как сделал вообще не поёму
    def __init__(self, token: str):
        self.token = token

    def get_headers(self): #Получить авторизацию
        return{
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, path_to_file): #Получить ссылку на загрузку
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = self.get_headers() #Получить авторизацию
        params = {'path': path_to_file, 'overwrite': 'true'} # Некое условие
        response = requests.get(url, headers=headers, params=params) #
        pprint(response.json())
        return response.json()

    def upload(self, path_to_file: str): #Загрузка файла "Тупо переписал с лекции"
        href = self.get_upload_link(path_to_file=path_to_file).get('href', '')
        response = requests.put(href, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Успех')


if __name__ == '__main__':
    print('Задание 1')
    superheros_intelligence()

    print()
    print('Задание 2')
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '1.txt'
    token = 'klopAAAAgtGc88EAADLqqqqRXY11111EaXl075kpppzGOzzzA'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)