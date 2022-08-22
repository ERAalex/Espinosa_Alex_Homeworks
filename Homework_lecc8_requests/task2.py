import requests
from pprint import pprint
import json

URL1 = 'https://cloud-api.yandex.net/v1/disk/resources'   # url для создания папок

class YaUploader:

    def __init__(self, token: str):
        self.token = yandex_acc_token

    def create_folder(self, name_path):
        """Создание папки. \n path: Путь к создаваемой папке."""
        response = requests.put(f'{URL1}?path={name_path}', headers=headers)
        # добавляем описание ошибки, если вдруг не создаться + выведем из json конкретику
        if response:
            print('все успешно создано')
        else:
            print('создание каталога не прошло, причина: ')
            x = response.json()
            print(x['message'])



    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }


    def get_list_of_files(self):
        files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        pprint(response)
        return response.json()



    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()


# disk_file_name  - место на яндекс диске, куда кладем. например в папку test  получается 'test/2.txt' причем название
# файла прописываем тоже, то как он будет назваться (можно любое, сохранить только расширение)!

# filename - название документа и путь до него внутри локального диска(то есть то, октуда мы его открываем через open)

    def upload_file_to_disk(self, disk_file_path, direction):
        href = self._get_upload_link(disk_file_path= disk_file_path).get("href", "")
        response = requests.put(href, data=open(direction, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    direction = input(str('Введите путь до файла на компьютере: '))
    yandex_acc_token = input('Введите Ваш токен Yandex.Disk: ')
# достаем навзание из адреса введенного пользователем (чтобы использовать то же название и расширение документа)
    disk_file_path = direction.split('/')[-1]
# создаем объект класса для выозва функций
    yan = YaUploader(yandex_acc_token)

    yan.upload_file_to_disk(disk_file_path, direction)

