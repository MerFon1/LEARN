def spel(list1, list2):
    slis2 = set(list2)
    for i in slis2:
        if i not in list1:
            print(i)

def query_str(list, x):
    for i in range(x):
        str = input().lower().split()
        list.extend(str)

lines = int(input())
correct_words = []
query_str(correct_words, lines)

lines1 = int(input())
received_words = []
query_str(received_words, lines1)

spel(correct_words, received_words)










