import requests
import json

book = ''
verse = ''
url = 'http://getbible.net/json?passage='
# add for app python
end = '&raw=true'


def specific_bible():
    global book
    try:
        book = input('What book do you want to look ? :  ')
        chapter = input('What chapter ? : ')
        verse = input('What verse ? : ')
        response = url + book + chapter + ":" + verse + end + "&version=asv"
        rep = requests.get(response).json()
        verse_upper = rep["book"][0]["chapter"]
        verse_lower = verse_upper[verse]['verse']
        print(verse_lower)
    except KeyError:
        print('No book ')
    except json.decoder.JSONDecodeError:
        print('no chapter in this ' + book + '.')


def search_bible():
    global book, verse
    try:
        book = input('What book do you want to look ? : ')
        chapter = input('What chapter  ? : ')
        verse_int = 1
        while True:
            verse = str(verse_int)
            response = url + book + chapter + ':' + verse + end + '&version=asv'
            rep = requests.get(response).json()
            verse_upper = rep["book"][0]["chapter"]
            verse_lower = verse_upper[verse]['verse']
            print('Verse ' + ''+  verse + ': ' + verse_lower)
            verse_int += 1
    except KeyError:
        print('END')
    except  json.decoder.JSONDecodeError:
        print('ThatS all versus in ' + book)
        

