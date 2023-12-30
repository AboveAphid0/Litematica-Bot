import json, pickle, os, pandas as pd

FILENAME = input('Filename: ') #"test"
FILEPATH = f'Generated Files\\{FILENAME}\\{FILENAME}'

try:
    with open(f'{FILEPATH}.json', 'r') as f:
        data = dict(json.loads(f.read()))
except json.JSONDecodeError:
    print('ERROR: Not a valid json formatted file.')



commandFormat = '/setblock ~{x} ~{y} ~{z} {block}'


jsonFormat = {}

l = 0
for i, blocks in data.items():
    blocks = data[i]

    for b in blocks:
        x,y,z = b[0][0], b[0][1], b[0][2]

        command = commandFormat.format(x=x, y=y, z=z, block=b[1])

        jsonFormat[l] = command
        l += 1


    print('Completed Row:', i)

with open('temp.pickle', 'wb') as f:
    pickle.dump(jsonFormat, f, protocol=pickle.HIGHEST_PROTOCOL) ##@##R$%^&*(*REW#$%^&*&^%$#$%^&**&) sections or json_sections????

with open('temp.pickle', 'rb') as f:
    data = pd.read_pickle(f)

os.remove('temp.pickle')

with open(f'{FILEPATH}-commands.json', 'w') as f:
    json.dump(data, f)