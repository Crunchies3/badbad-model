import sentencepiece as spm

# Load Ata SentencePiece model
sp = spm.SentencePieceProcessor()
sp.load("eng-ata/sentence_piece/spm_ata.model")

# Read tokenized output
with open("eng-ata/pred.spm.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Detokenize
decoded = [sp.decode(line.strip().split()) for line in lines]

# Save detokenized predictions
with open("eng-ata/pred.txt", "w", encoding="utf-8") as f:
    for line in decoded:
        f.write(line + "\n")
