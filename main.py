# все начинаю с тестов


# новый файл загружен в базу данных
    #генерируется уникальный ключ доступа к файлу
    #является ли ключ уникальным и отличным от всех ключей в базе данных?

    #успешна ли загрузка нового файла?

# загрузка файла успешно завершена. 
    # Success-страница с ключом и кнопками "Удалить файл" и "Переименовать файл"
    # Крупными буквами показывается ключ доступа к файлу
    # (опционально) Отправить ключ на почту
    # (опционально) Предупреждение что файл будет удалён через 7 дней


#самый старый файл удалился автоматически по истечению 7 дней с момента загрузки
    #между датой загрузки и сегодняшней датой более 7 дней? Удалить файл


#старый файл успешно удалён пользователем

#новый заруженный файл успешно переименован
    #содержит ли новое имя файла недопустимые символы?

#новый файл успешно найден по введённому ключу пользователя
    #есть ли такой ключ в базе данных?

    #привязан ли такой ключ к какому-то файлу?
        #нет ли на один такой ключ двух и более файлов? Уникален ли ключ (это лучше на этапе присвоения ключа)

    #привязан ли такой ключ к уже удалённому файлу?

    

#новый файл успешно скачивается пользователю на телефон (mobile-first)
