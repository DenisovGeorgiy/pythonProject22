import requests

TOKEN = ''

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def upload_file_to_disk(self, disk_file_path, filename):
        href_json = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_json["href"]
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Успех")

if __name__ == "__main__":
    YandexDisk(token=TOKEN)
    YandexDisk.upload_file_to_disk('disk.txt', 'book.txt')