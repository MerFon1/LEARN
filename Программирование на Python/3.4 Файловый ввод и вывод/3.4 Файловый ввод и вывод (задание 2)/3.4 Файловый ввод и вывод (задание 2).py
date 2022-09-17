import collections
slv = []
#открывем файл
with open('text1.txt') as inf:
    for gbggg in inf:
        #обьеденяем все строки в одну
        gbggg = (" ".join(line.strip() for line in inf))
        # делаем ве буквы маленькими
        gbggg = gbggg.lower()
        #создаём список
        gbggg = gbggg.split()
        #переносим созданый список в постояную переменую
        slv.extend(gbggg)

print(slv)

# C помощью импортированой функции Counter из библиотеки collections
# cоздаём словарь в котором пишеться
# сколько раз повторялось каждое слово из списка nslv
nslv = collections.Counter(slv)

print(nslv)







