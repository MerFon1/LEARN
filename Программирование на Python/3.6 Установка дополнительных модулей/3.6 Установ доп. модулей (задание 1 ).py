import requests
with open ('dataset_3378_1.txt') as inf:
    #Читаем и записываем строки файла в переменую
    url = (inf.readline().strip())
    #Переходим по сылке качаем файл и записываем в переменую данные нового файла
    text_url =  requests.get(url).text
    #Выводим подсчитаное количество строк в переменной
    print(text_url.count('\n'))
