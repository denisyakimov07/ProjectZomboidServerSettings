mods_id = []
mods_name = []
maps_name = []
with open('Yanis07.ini', 'r') as file:
    data = file.readlines()

with open('mods.txt', 'r') as file:
    mode_data = file.readlines()
for mod in mode_data:
    if 'Workshop ID' in mod:
        mods_id.append(mod.replace('Workshop ID:', '').replace(' ', '').replace('\n', ''))
    if 'Mod ID:' in mod:
        mods_name.append(mod.replace('Mod ID:', '').replace(' ', '').replace('\n', ''))
    if 'Map Folder:' in mod:
        maps_name.append(mod.replace('Map Folder:', '').replace(' ', '').replace('\n', ''))

for i, x in enumerate(data):
    if 'WorkshopItems' in x and 'Example' not in x:
        data[i] = f'WorkshopItems={";".join(set(mods_id))}\n'

    if 'Mods=' in x and 'Example' not in x:
        data[i] = f'Mods={";".join(set(mods_name))}\n'

    if 'Map=' in x and 'Example' not in x:
        data[i] = f'Map={";".join(set(maps_name))};Muldraugh, KY\n'

with open('Yanis07.ini', 'w') as file:
    file.writelines(data)
