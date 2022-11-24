from random_word import RandomWords
import requests, json
from flask import Flask
app = Flask(__name__)

r = RandomWords()

def find_word_meaning(word):
  meaning = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}")
  meaning_list = json.loads(meaning.text)
  try:
    return meaning_list['list'][0]['definition']
  except Exception as ex:
    return False
  
def find_word():
  word = r.get_random_word()
  meaning = find_word_meaning(word)
  if not meaning:
    return find_word()
  return word, meaning

@app.route('/')
def index():
   return jsonify(find_word())

if __name__=="__main__":
  app.run()