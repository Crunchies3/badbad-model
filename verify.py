def verify_vocab_file(filepath):
    issues_found = False
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            stripped_line = line.strip()
            if not stripped_line:
                print(f"[ERROR] Empty line at line {line_num} in '{filepath}'")
                issues_found = True
                continue

            parts = stripped_line.split(None, 1)
            if len(parts) != 2:
                print(f"[ERROR] Line {line_num} in '{filepath}' does not have exactly two fields: '{stripped_line}'")
                issues_found = True
                continue

            word, freq = parts
            try:
                int(freq)
            except ValueError:
                print(f"[ERROR] Frequency is not an integer at line {line_num} in '{filepath}': '{freq}'")
                issues_found = True

    if not issues_found:
        print(f"[OK] No issues found in '{filepath}'")
    else:
        print(f"[WARNING] Issues detected in '{filepath}'. Please fix them before training.")

if __name__ == "__main__":
    src_vocab_path = "eng-ata/run/example.vocab.src"  # Change to your actual source vocab file path
    tgt_vocab_path = "eng-ata/run/example.vocab.tgt"  # Change to your actual target vocab file path

    print("Verifying source vocab file...")
    verify_vocab_file(src_vocab_path)

    print("\nVerifying target vocab file...")
    verify_vocab_file(tgt_vocab_path)
