# coding: utf8
# источник: https://www.palletsprojects.com/p/itsdangerous/
from datetime import datetime
from itsdangerous import URLSafeSerializer
s = URLSafeSerializer('secret-key')
time_stamp_for_key = datetime.now()
s.dumps(time_stamp_for_key)

print(time_stamp_for_key)
print(s.dumps)

        #генерируется уникальный ключ доступа к файлу
        # .generate_new_file_identification_key()
        # уникальность ключа можно достичь при помощи помещения в s.dumps() серверное время загрузки файла.
        # даже если будет дубль файла - его ключ будет уникален из-за разницы во времени
        