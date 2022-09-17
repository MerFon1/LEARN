from requests import get
from sys import stdin
import json

for number in stdin:
    number = number.rstrip()
    string = f"http://numbersapi.com/{number}/math?json=true"
    result = get(string).json()
    if result["found"]:
        print('Interesting')
    else:
        print('Boring')
