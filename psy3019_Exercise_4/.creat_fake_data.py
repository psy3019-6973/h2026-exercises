import os
import numpy as np

#TODO:

data_types = {'func': '_bold.nii.gz',
               'anat': '_T1w.nii.gz',
               'beh': '.csv'}

for sub in range(1, 6):  # Crée des dossiers pour 5 sujets
    for data_type in data_types:
        sub_dir = f'bids_stroop_dataset/sub-{sub:02d}/{data_type}'
        os.makedirs(sub_dir, exist_ok=True)
        if sub == 5 :
            sub_dir = f'bids_stroop_dataset/sub-{sub-1:02d}/{data_type}'
        # Crée un fichier de données factices pour chaque type de données
        data_file = os.path.join(sub_dir, f'sub-{sub:02d}_task-stroop{data_types[data_type]}')
        if sub == 2 and data_type == 'beh':
            data_file = os.path.join(sub_dir, f'sub-XX_task-stroop{data_types[data_type]}')
        with open(data_file, 'w') as f:
            f.write('Données factices :)'.format(sub, data_type))

metadata_file = 'bids_stroop_dataset/dataset_description.json'
with open(metadata_file, 'w') as f:
    f.write('{"Name": "BIDS Stroop Dataset", "BIDSVersion": "X.X.X"}')

nrg = np.random.default_rng(seed=42)
participants_file = 'bids_stroop_dataset/participants.tsv'
with open(participants_file, 'w') as f:
    f.write('participant_id\tage\tsex\n')
    ages = nrg.integers(20, 40, size=5)
    for sub, age in zip(range(1, 6), ages):
        sexe = nrg.choice(['M', 'F'])
        f.write(f'sub-{sub:02d}\t{age}\t{sexe}\n')
