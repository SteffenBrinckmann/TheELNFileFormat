import os, json
from zipfile import ZipFile
from pathlib import Path
from eln2md import tree

elns = {
        'SampleDB':'examples/SampleDB/sampledb_export.eln',
        'elabFTW':'examples/elabftw/export.eln',
        'kadi4mat':'examples/kadi4mat/collections-example.eln',
        'PASTA':'examples/PASTA/PASTA.eln'}

METADATA_FILE = 'ro-crate-metadata.json'

for title, path in elns.items():
    print(f'\n\n===============================\n========= {title} ===========')
    parentDir = Path(path).parent
    with ZipFile(path, 'r') as elnFile:
        elnFile.extractall(parentDir)
    pathDir = [parentDir/i for i in os.listdir(parentDir) if (parentDir/i).is_dir()][0]
    print('Filesystem tree:')
    os.system(f'tree --noreport {pathDir}')
    metadataJsonFile = [i.as_posix() for i in pathDir.iterdir() if i.as_posix().endswith(METADATA_FILE)][0]
    print(f'Json file: {metadataJsonFile}')
    metadataContent = json.load(open(metadataJsonFile))
    print(tree(metadataContent))
