# coding: utf8
# источник: https://www.palletsprojects.com/p/itsdangerous/
from datetime import datetime
from itsdangerous import Signer.TimestampSigner

secret_key = datetime.now()


s = TimestampSigner()

print(secret_key)
print(s)

        #генерируется уникальный ключ доступа к файлу
        # .generate_new_file_identification_key()
        # уникальность ключа можно достичь при помощи помещения в s.dumps() серверное время загрузки файла.
        # даже если будет дубль файла - его ключ будет уникален из-за разницы во времени
        