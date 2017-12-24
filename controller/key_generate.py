from itsdangerous import URLSafeSerializer
s = URLSafeSerializer('secret-key')
s.dumps([1, 2, 3, 4])

s.loads('WzEsMiwzLDRd.wSPHqC0gR7VUqivlSukJ0IeTDgo')
[1, 1]

        #генерируется уникальный ключ доступа к файлу
        # .generate_new_file_identification_key()