from litemapy import Schematic
import pandas as pd
import json, pickle, os



FOLDER = "LitematicaSchematics\\"
FILENAME = input('Filename: ') #"test"

SAVEFOLDER = 'Generated Files'

DEFAULTFILENAME = FILENAME

# Load the schematic and get its first region
schem = Schematic.load(FOLDER + FILENAME + ".litematic")

reg = list(schem.regions.values())[0]


# Print out the basic shape
sections = {}

section = []
i = 0
for y in reg.yrange():
    for x in reg.xrange():
        for z in reg.zrange():
            b = reg.getblock(x, y, z)
            if b.blockid == "minecraft:air":
                print(" ", end="")
            else:
                print("#", end='')

                section.append([(x, y, z), b.blockid])
        print()
    
    print('\n\n')
    sections[i] = section
    i += 1
    section = []






i = 0
while 1:
    if not os.path.exists(f'{SAVEFOLDER}\\{FILENAME}'):
        os.mkdir(f'{SAVEFOLDER}\\{FILENAME}')
        break
    else:
        if input('Folder already exists! Would you like to overide with new processed data? (Y/n)') == 'y':
            FILENAME = f'{DEFAULTFILENAME}_{i}'
            print('Trying new name:', FILENAME)
        else:
            print('Overiding...')
            break
    i += 1
        

# My very janky way of saving it as a json
with open(f'{SAVEFOLDER}\\{FILENAME}\\{FILENAME}.pickle', 'wb') as f:
    pickle.dump(sections, f, protocol=pickle.HIGHEST_PROTOCOL) ##@##R$%^&*(*REW#$%^&*&^%$#$%^&**&) sections or json_sections???? From testing it would seem to be sections lol

with open(f'{SAVEFOLDER}\\{FILENAME}\\{FILENAME}.pickle', 'rb') as f:
    data = pd.read_pickle(f)

with open(f'{SAVEFOLDER}\\{FILENAME}\\{FILENAME}.json', 'w') as f:
    json.dump(data, f)

with open(f'{SAVEFOLDER}\\{FILENAME}\\{FILENAME}-readable.json', 'w') as f:
    json.dump(data, f, indent=4)