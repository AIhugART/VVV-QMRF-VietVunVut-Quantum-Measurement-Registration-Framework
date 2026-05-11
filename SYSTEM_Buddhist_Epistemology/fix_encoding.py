filepath = r"h:\Other computers\My Computer\Buddhist_Epistemology_Quantum_Measurement\SYSTEM_Buddhist_Epistemology\system_be_full.md"

with open(filepath, 'rb') as f:
    raw = f.read()

text = raw.decode('utf-8')

has_macron = '\u0101' in text
has_underdot_n = '\u1e47' in text

if has_macron and has_underdot_n:
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    print("Diacritics are correct. File re-saved as clean UTF-8.")
    print(f"File size: {len(text)} chars")
else:
    print("ERROR: diacritics not found")
