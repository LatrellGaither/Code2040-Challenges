import requests
import json
from dateutil.parser import parse
from datetime import timedelta

myToken = '075b5de9348beb07fe8fd1c52d59f15c'
myGit = 'https://github.com/LatrellGaither/Code2040-Challenges'
data = {'token': myToken}

#Registration
def register():
    data = {'token': myToken, 'github': myGit}
    #post request to code2040.org
    request = requests.post("http://challenge.code2040.org/api/register", json=data)

#reverse slicing for reverse_string method
def reversed(word):
    return word[::-1]

#Stage 1 challenge
def reverse_string():
    
    request = requests.post("http://challenge.code2040.org/api/reverse", json=data)
    word = request.text
    return_data = {'token': myToken, 'string': reversed(word)}
    return_request = requests.post('http://challenge.code2040.org/api/reverse/validate', json=return_data)

def find_needle(needle, haystack):
    pos = 0
    for x in haystack:
        if x == needle:
            return pos
        else:
            pos += 1

def haystack():
    request = requests.post('http://challenge.code2040.org/api/haystack', json=data)
    r_data = request.json()
    needle = r_data['needle']
    haystack = r_data['haystack']
    result = find_needle(needle, haystack)
    return_data = {'token': myToken, 'needle': result}
    return_request = requests.post('http://challenge.code2040.org/api/haystack/prefix', json=return_data)

def remove_strings(prefix, strings):
    crucial_info = len(prefix)
    result = []
    for x in strings:
        if not x[:crucial_info] == prefix:
            result.append(x)
    return result

def prefix():
    request = requests.post('http://challenge.code2040.org/api/prefix', json=data)
    r_data = request.json()
    prefix = r_data['prefix']
    strings = r_data['array']
    new_strings = remove_strings(prefix, strings)
    return_data = {'token': myToken, 'array': new_strings}
    request = requests.post('http://challenge.code2040.org/api/prefix/validate', json=return_data)

def dating_incriment(datestamp, interval):
    date_info = parse(datestamp)
    time_to_add = timedelta(seconds = interval)
    val = date_info + time_to_add
    val = val.isoformat()
    val = val[:len(val) - 4]
    return val

def dating():
    request = requests.post('http://challenge.code2040.org/api/dating', json=data)
    r_data = request.json()
    datestamp = r_data['datestamp']
    interval = r_data['interval']
    return_datestamp = dating_incriment(datestamp, interval)
    data['datestamp'] = return_datestamp
    request = requests.post('http://challenge.code2040.org/api/dating/validate', json=data)
