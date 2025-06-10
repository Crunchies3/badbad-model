import sentencepiece as spm

# Load the SentencePiece model
sp = spm.SentencePieceProcessor()
sp.load("spm.model")

# Define input and output file paths
files = [
    ("eng-ata/src-train.txt", "eng-ata/src-train.spm.txt"),
    ("eng-ata/tgt-train.txt", "eng-ata/tgt-train.spm.txt"),
    ("eng-ata/src-val.txt", "eng-ata/src-val.spm.txt"),
    ("eng-ata/tgt-val.txt", "eng-ata/tgt-val.spm.txt"),
]

# Encode each file
for input_path, output_path in files:
    with open(input_path, "r", encoding="utf-8") as infile, \
         open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            encoded = sp.encode(line.strip(), out_type=str)
            outfile.write(" ".join(encoded) + "\n")

print("All files encoded successfully.")
