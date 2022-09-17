data = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': []}

with open('dataset_3380_5.txt') as f:
    file = f.read().split()
    f.seek(0)

    for i in range(0, len(file), 3):
        data.get(file[i]).append(int(file[i + 2]))

for i in data.keys():
    if len(data[i]) > 0:
        print(f"{i} - {sum(data[i]) / len(data[i])}")
    else:
        print(f"{i} -")


