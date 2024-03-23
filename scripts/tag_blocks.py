from os.path import join, dirname
from json import loads, dumps
from os import listdir

root_dir = dirname(dirname(__file__))
blocks_dir = join(root_dir, 'blocks')
meta_id = 4

for file in listdir(blocks_dir):
    if not file.endswith('.json'):
        continue

    path = join(blocks_dir, file)
    with open(path) as f:
        data = loads(f.read())
        data["meta.id"] = meta_id
    with open(path, 'w') as f:
        f.write(dumps(data, indent=4))
    meta_id += 1