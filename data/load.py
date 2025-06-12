import sentencepiece as spm

# Load tokenizer
sp_en = spm.SentencePieceProcessor(model_file='spm_en.model')
sp_ata = spm.SentencePieceProcessor(model_file='spm_ata.model')

# Example
eng = "Where are you going?"
ata = "Adto kaw sadiin?"

# Encode
eng_ids = sp_en.encode(eng, out_type=int)
ata_ids = sp_ata.encode(ata, out_type=int)

# Decode
print("Encoded:", eng_ids)
print("Decoded:", sp_en.decode(eng_ids))
