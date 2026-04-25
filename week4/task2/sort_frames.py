import os, shutil

src = 'all_frames'
frames = sorted(os.listdir(src))

train = frames[0:400:4]
val   = frames[400::4]
test  = [f for f in frames if f not in train and f not in val]

for f in train: shutil.copy(os.path.join(src,f), 'dataset/train/images/')
for f in val:   shutil.copy(os.path.join(src,f), 'dataset/val/images/')
for f in test:  shutil.copy(os.path.join(src,f), 'dataset/test/images/')

print('Train:', len(train))
print('Val:',   len(val))
print('Test:',  len(test))
print('Done!')