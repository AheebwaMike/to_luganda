from deep_translator import GoogleTranslator
from tqdm import tqdm
import time
import os
import argparse

os.path.makedirs("translated", exist_ok=True)

parser = argparse.ArgumentParser(description='Parser for File Selection.')
parser.add_argument("id", help="ID of the file to translate")
args = parser.parse_args()

ID = args.id
INPUT_FILE_PATH = fr'files\general_phrases_{ID}.txt'
OUTPUT_FILE_PATH = fr'translated\general_phrases_{ID}_translated.txt'

if os.path.exists(OUTPUT_FILE_PATH):
    with open(OUTPUT_FILE_PATH, 'r', encoding='UTF-8') as file:
        lines = file.read().splitlines()
        START = sum(1 for _ in lines)

else:
    START = 0

name = f'file {ID}'

RATE_LIMIT = 0.5
BATCH_SIZE = 30

translator = GoogleTranslator(source='auto', target='lg')

# 1. Read input
with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as file:
    phrases = [line.strip() for line in file if line.strip()][START:]

translated_phrases = 0
batch_size = BATCH_SIZE


print(f'\n🟢 Starting from line {START}')
# 2. Translate in batches
try:
    for i in tqdm(range(0, len(phrases), batch_size), desc=f'Translating batches: ({name})'):
        batch = phrases[i:i + batch_size]
        
        translations = translator.translate_batch(batch)
        translated_phrases += len(translations)

        with open(OUTPUT_FILE_PATH, 'a', encoding='utf-8') as file:
            for original, translated in zip(batch, translations):
                file.write(f"{original}\t{translated}\n")
        
        # Small sleep to prevent IP blocking/rate limiting
        time.sleep(RATE_LIMIT)

except Exception as e:
    print(f"\nAn error occurred: {e}")

print(f"Done! Translated {translated_phrases} phrases.")
