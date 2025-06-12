import sentencepiece as spm

# Train English tokenizer
spm.SentencePieceTrainer.train(
    input='eng-ata/src-train.txt',
    model_prefix='spm_en',
    vocab_size=8000,
    character_coverage=1.0,
    model_type='bpe'  # or 'unigram'
)

# Train Ata Manobo tokenizer
spm.SentencePieceTrainer.train(
    input='eng-ata/tgt-train.txt',
    model_prefix='spm_ata',
    vocab_size=8000,
    character_coverage=1.0,
    model_type='bpe'
)
