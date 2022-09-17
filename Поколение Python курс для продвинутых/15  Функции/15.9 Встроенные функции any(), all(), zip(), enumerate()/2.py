"""
Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о стране в формате:

<capital> is the capital of <country>, population equal <population> people.


Moscow is the capital of Russia, population equal 145934462 people.
Washington is the capital of USA, population equal 331002651 people.
...
Для каждой страны информацию выводить на отдельной строке.
"""

countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [str(i).replace('_','',str(i).count('_')) for i in [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]]

[print(f"{cap} is the capital of {cou}, population equal {pop} people.") for cap,cou,pop in zip(capitals,countries,population)]