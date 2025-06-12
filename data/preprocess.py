import random

random.seed(42)

# Read and lowercase
with open('eng.txt', 'r', encoding='utf-8') as f_src, \
     open('ata.txt', 'r', encoding='utf-8') as f_tgt:
    
    src_lines = [line.strip().lower() for line in f_src.readlines()]
    tgt_lines = [line.strip().lower() for line in f_tgt.readlines()]

assert len(src_lines) == len(tgt_lines), "Line count mismatch!"

# Original data
original_data = list(zip(src_lines, tgt_lines))

# Probabilistic oversampling (30% no oversample, 50% duplicated once, 20% duplicated twice)
data = []
for pair in original_data:
    rand = random.random()
    if rand < 0.3:
        copies = 1  # 30% chance: keep once
    elif rand < 0.8:
        copies = 2  # 50% chance: duplicate once
    else:
        copies = 3  # 20% chance: duplicate twice
    data.extend([pair] * copies)


# Final shuffle
random.shuffle(data)

# Split sizes
total = len(data)
train_end = int(0.75 * total)
val_end = train_end + int(0.125 * total)

# Split data
train_data = data[:train_end]
val_data = data[train_end:val_end]
test_data = data[val_end:]

# Write function
def write_split(data, split_name):
    with open(f'src-{split_name}.txt', 'w', encoding='utf-8') as f_src, \
         open(f'tgt-{split_name}.txt', 'w', encoding='utf-8') as f_tgt:
        for src, tgt in data:
            f_src.write(src + '\n')
            f_tgt.write(tgt + '\n')

# Save files
write_split(train_data, 'train')
write_split(val_data, 'val')
write_split(test_data, 'test')

print("Files created: src-*.txt and tgt-*.txt for train, val, and test.")