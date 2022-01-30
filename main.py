import requests
from config import *

def speak(str):
  # This part of code helps us send the audio output.
  try:
    from win32con.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
  except:
    pass

# Basic API request to news api.
a = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}')
# Transforms the respose into dict format.
b = a.json()

# Prints instructions.
print('Welcome to your News Friend!\n\nType s to stop anytime.\nType m to expand the article anytime.\nType anything else to continue.\n\n')
input("Press enter to continue!\n")
# Loops through the news page.
for article in range(len(b['articles'])):
  # Print the index values.
  print(article + 1, '/', len(b['articles']))     
  # Fetches the headline of the article.
  text = b['articles'][article]['title']
  # Removes the article credit.
  author_split = text.split(' - ')
  # Prints the article without the credits. 
  print(text)
  speak(author_split[0] + 'by' + author_split[1])
  # Takes a dummy input.
  input_1 = input()
  # Stops the loauthor_splitif reader types s.
  if input_1 == 's':
    break
  # Expands the article if reader types m.
  elif input_1 == 'm':
    # Prints more about the headline.
    print(b['articles'][article]['description'])
    speak(b['articles'][article]['description'])
    
    # Takes another dummy input.
    input_2 = input()
    # Stops the loauthor_splitif reader types s.
    if input_2 == 's':
      break
    # Expands the article if reader types m.
    elif input_2 == 'm':
      # Prints the whole article.
      print(b['articles'][article]['content'])
      speak(b['articles'][article]['content'])
      
      # Takes another dummy input.
      input_3 = input()
      # Stops the loauthor_splitif reader types s.
      if input_3 == 's':
        break
      # Give a error output if reader tries to expand any more.
      elif input_3 == 'm':
        print("Can't expand anymore")
  
  # Prints an error output at end.
  if (article + 1) == len(b['articles']):
    print('\n\nNo more articles!')
    speak('No more articles')
