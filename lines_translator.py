from deep_translator import GoogleTranslator
from tqdm import tqdm
import time
import os

os.makedirs('translated', exist_ok=True)

INPUT_FILE_PATH = r'general_phrases_2.txt'
OUTPUT_FILE_PATH = r'translated\general_phrases_2_translated.txt'
START = 0
name = 'file 2'

RATE_LIMIT = 0.5
BATCH_SIZE = 30

translator = GoogleTranslator(source='auto', target='lg')

# 1. Read input
with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as file:
    phrases = [line.strip() for line in file if line.strip()][START:]

translated_phrases = 0
batch_size = BATCH_SIZE

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
