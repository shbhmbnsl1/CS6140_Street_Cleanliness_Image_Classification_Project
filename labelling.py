import os
import csv

labels = []

def list_files(directory, label):
    files = os.listdir(directory)
    for file in files:
        labels.append({
            'image': directory + '/' + file,
            'label': label
        })

directories = ['final_dataset/train/clean', 'final_dataset/train/dirty', 'final_dataset/test/clean', 'final_dataset/test/dirty']
label_types = [0, 1, 0, 1]

for i in range(len(directories)):
    list_files(directories[i], label_types[i])

print(labels)

field_names = labels[0].keys()

with open('labels.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(labels)

