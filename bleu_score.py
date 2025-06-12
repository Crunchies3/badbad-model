import sacrebleu

# Reference sentences (from Ata Manobo Bible)
reference_corpus = [
    "ogsayoon ku si hisu kristu no lagboy no igbuyag ta no nigbogoy kanak to dayagang to oyow ogpakatood a no oghimu to soini no insugu din. ian su nigdoromdom sikandin to litos a rin no ogkasaligan, no sikan ian to nighimu a rin no suguanon din.",
   
]

# Hypothesis sentences as list
hypothesis = [
    "ogbuyu a to lagboy no igbuyag ta no si hisu kristu no ian lagboy no igbuyag ta no si hisu kristu kai to soini no kalibutan. ian su og-awoson din to",
  
]

# Compute BLEU score
bleu = sacrebleu.corpus_bleu(hypothesis, [reference_corpus])
print(f"BLEU score: {bleu.score:.2f}")
