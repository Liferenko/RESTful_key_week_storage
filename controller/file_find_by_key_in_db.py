# источник - Объект запросаhttps://ru.wikibooks.org/wiki/Flask#%D0%97%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B0_%D1%84%D0%B0%D0%B9%D0%BB%D0%B0

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # this is executed if the request method was GET or the
    # credentials were invalid

# как пользователь может найти уже ранее загруженный файл по ключу?
class test_finding_file_by_key_form():
    def __init__(self, file_identification_key):
        pass



#новый файл успешно найден по введённому ключу пользователя
    #есть ли такой ключ в базе данных?
    ,find_file_by_key()
    #привязан ли такой ключ к какому-то файлу?
        #нет ли на один такой ключ двух и более файлов? Уникален ли ключ (это лучше на этапе присвоения ключа)
    .test_check_multyple_key_usage()
    #привязан ли такой ключ к уже удалённому файлу?
    .test_check_if_key_was_removed_file_using()
    