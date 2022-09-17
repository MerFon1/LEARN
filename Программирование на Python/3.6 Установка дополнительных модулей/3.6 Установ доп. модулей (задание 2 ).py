import  requests
with open ('dataset_3378_2.txt') as inf:
    #Читаем строку обрабатываем её
    url = (inf.readline().strip())
    #Переходим по сылке и качаем файл благодаря библиотеке requests
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
    #Записываем в переменую nxf текст внутри скачаного файла
    nxf = r.text
    # Создаём цикл в котором будут проверять первые 2 буквы  текста в переменной nxf
    while nxf[0:2]!='We':
        #Переходим по сылке конец которой меняеться с изменением переменой nxf и качаем файл
        cr = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + nxf)
        #Записываем в переменую текст нового открытого файла
        nxf = cr.text
        print(nxf)














