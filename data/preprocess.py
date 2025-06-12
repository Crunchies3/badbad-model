import random
import re

random.seed(42)

# Load the data
with open('eng.txt', 'r', encoding='utf-8') as f_src, \
     open('ata.txt', 'r', encoding='utf-8') as f_tgt:
    
    src_lines = f_src.readlines()
    tgt_lines = f_tgt.readlines()

assert len(src_lines) == len(tgt_lines), "Line count mismatch!"

# Combine and shuffle
data = list(zip(src_lines, tgt_lines))
random.shuffle(data)

# Split sizes
total = len(data)
train_end = int(0.75 * total)
val_end = train_end + int(0.125 * total)

# Split data
train_data = data[:train_end]
val_data = data[train_end:val_end]
test_data = data[val_end:]

# Oversample training data by a factor of 5
train_data_oversampled = train_data * 5
random.shuffle(train_data_oversampled)

# Clean text: lowercase and retain letters, spaces, and basic punctuation
def clean_text(text):
    text = text.lower()
    # Keep letters, spaces, and these basic punctuation marks: . , ? ! : ; ' " -
    text = re.sub(r"[^a-zA-Z\s.,?!:;-]", '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Write function
def write_split(data, split_name):
    with open(f'src-{split_name}.txt', 'w', encoding='utf-8') as f_src, \
        open(f'tgt-{split_name}.txt', 'w', encoding='utf-8') as f_tgt:
        for src, tgt in data:
            f_src.write(clean_text(src) + '\n')
            f_tgt.write(clean_text(tgt) + '\n')

# Save files
write_split(train_data_oversampled, 'train')
write_split(val_data, 'val')
write_split(test_data, 'test')

print("Files created: src-*.txt and tgt-*.txt for train, val, and test.")
