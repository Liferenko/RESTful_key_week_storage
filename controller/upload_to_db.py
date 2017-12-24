# coding: utf8
# источник - https://github.com/admiralobvious/flask-mysqldb , http://snakeproject.ru/rubric/article.php?art=python_mysql
from filestorage import app
from flask import request
from flask_mysqldb import MySQL
from werkzeug import secure_filename


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))

    
# как пользователь может загрузить файл в облако?
# class test_file_uploading_form():
        # не пустая ли форма отправки? Если ли файл?
        # (опционально) возможно ли загрузить сразу 2-3 файла?
        # есть ли кнопка "Выбрать файл" в форме загрузки
        # есть ли кнопка "загрузить файл"?
        #
        #




#успешна ли загрузка нового файла?
# .test_does_new_file_uploading_successful()



# загрузка файла успешно завершена. 
    # Success-страница с ключом и кнопками "Удалить файл" и "Переименовать файл"
    # Крупными буквами показывается ключ доступа к файлу
    # (опционально) Отправить ключ на почту
    # (опционально) Предупреждение что файл будет удалён через 7 дней


