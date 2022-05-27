mport base64                  
import requests
from PIL import Image
#######################################################################
#########################Getting and saving image data ################
#######################################################################

response = requests.get('https://api.codepannu.com/disney/')
x = [i['_id'] for i in response.json()]
print(x)
filename = input("Enter the filename with extention: ")
for n,i in enumerate(x):
  with open(f'{i}.jpg','wb') as f:
    f.write(base64.b64decode(response.json()[n]['img']))
    print('wrote')

#####################################################################
###################### posting data #################################
#####################################################################

character = {
  'name':'minniemouse',
  'designedby':'Walt Disney,',
  'img':'',
  'firstAppeared': 'Steamboat Willie',
  'gender':'female'
  }  

with open('Minnie_Mouse.png','rb') as f:
  character['img'] = base64.b64encode(f.read()).decode("utf8")


response = requests.post('https://api.codepannu.com/disney/',
   params={'apiKey':'codepannustudent'},
  data={
  'name':character['name'],
  'designedby':character['designedby'],
  'img':character['img'],
  'firstAppeared':character['firstAppeared'],
  'gender':character['gender'],})
print(response.json())


#####################################################################
######################## Getting by name ############################
#####################################################################

mickey = requests.get(f'https://api.codepannu.com/disney/name/mIcKeyMoUse',params={'apiKey':'codepannustudent'})
print(mickey.json())
with open('miakeyy123.png','wb') as f:
  f.write(base64.b64decode(mickey.json()[0]['img']))

im = Image.open('./miakeyy123.png')
im.show()


mini = requests.get(f'https://api.codepannu.com/disney/gender/female',params={'apiKey':'codepannustudent'})
print(mini.json())
with open('mini2.png','wb') as f:
  f.write(base64.b64decode(mini.json()[0]['img']))
  print('wrote')
