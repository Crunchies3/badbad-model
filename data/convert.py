import sentencepiece as spm

# Load SentencePiece models
sp_en = spm.SentencePieceProcessor(model_file='spm_en.model')
sp_ata = spm.SentencePieceProcessor(model_file='spm_ata.model')

# Tokenization function
def tokenize_file(sp, input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as fin, \
         open(output_path, 'w', encoding='utf-8') as fout:
        for line in fin:
            pieces = sp.encode(line.strip().lower(), out_type=str)
            fout.write(' '.join(pieces) + '\n')

# Define file names for each split
splits = ['train', 'val', 'test']

for split in splits:
    src_in = f'src-{split}.txt'
    tgt_in = f'tgt-{split}.txt'
    src_out = f'src-{split}.spm.txt'
    tgt_out = f'tgt-{split}.spm.txt'

    print(f"Tokenizing {split} set...")
    tokenize_file(sp_en, src_in, src_out)
    tokenize_file(sp_ata, tgt_in, tgt_out)

print("✅ Tokenization complete. Files saved as *.spm.txt")
