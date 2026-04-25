import os

imgs = os.listdir('dataset/train/images')
with open('train.txt', 'w') as f:
    for img in sorted(imgs):
        f.write('dataset/train/images/' + img + '\n')
print('train.txt created with', len(imgs), 'entries')

imgs = os.listdir('dataset/val/images')
with open('val.txt', 'w') as f:
    for img in sorted(imgs):
        f.write('dataset/val/images/' + img + '\n')
print('val.txt created with', len(imgs), 'entries')