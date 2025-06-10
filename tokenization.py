import sentencepiece as spm

spm.SentencePieceTrainer.train(
    input='train.all.txt',
    model_prefix='spm',
    vocab_size=8000,
    character_coverage=1.0,
    model_type='bpe'
)
