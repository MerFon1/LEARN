"""
Подарок на новый год
Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и оценка разделены пробелом). Оценка - целое число от 00 до 100100 включительно.

Напишите программу для добавления 55 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в файл new_scores.txt.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Если бы файл class_scores.txt содержал строки:

Washington 83
Adams 86
Kingsman 100
MacDonald 95
Thomson 98
то файл new_scores.txt имел бы вид:

Washington 88
Adams 91
Kingsman 100
MacDonald 100
Thomson 100
Примечание 3. Указанный файл можно скачать по ссылке.
"""

with open('class_scores.txt', encoding='utf-8') as csf, open('new_scores.txt','w',encoding='utf-8') as nsf:
    l_l = len(csf.readlines())
    csf.seek(0)
    for i in range(l_l):
        name,score = csf.readline().strip().split()
        if int(score)<95:
            score = int(score)+5
        else:
            score = 100
        print(f"{name} {score}",file=nsf)







