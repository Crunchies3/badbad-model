def clean_text_file(filename):
    cleaned_lines = []
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            cleaned = line.strip()
            cleaned_lines.append(cleaned)

    with open(filename, 'w', encoding='utf-8') as f:
        for line in cleaned_lines:
            f.write(line + '\n')

clean_text_file('ata.txt')
clean_text_file('eng.txt')

print("Cleaned ata.txt and eng.txt (whitespace trimmed, non-UTF8 characters removed).")
