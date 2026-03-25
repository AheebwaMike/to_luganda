from deep_translator import GoogleTranslator
from tqdm import tqdm
import time

INPUT_FILE_PATH = r'general_phrases_2.txt'
OUTPUT_FILE_PATH = r'general_phrases_2_translated.txt'
START = 0

translator = GoogleTranslator(source='auto', target='lg')


# 1. Read input
with open(INPUT_FILE_PATH, 'r', encoding='utf-8') as file:
    phrases = [line.strip() for line in file if line.strip()][START:]

translated_phrases = 0
batch_size = 30  # Number of phrases per request (adjust based on phrase length)

# 2. Translate in batches
# the total number of batches that we can do at a single step is almost infinite and does not bring upt h
try:
    for i in tqdm(range(0, len(phrases), batch_size), desc='Translating batches'):
        batch = phrases[i:i + batch_size]
        
        translations = translator.translate_batch(batch)
        translated_phrases += len(translations)

        with open(OUTPUT_FILE_PATH, 'a', encoding='utf-8') as file:
            for original, translated in zip(batch, translations):
                file.write(f"{original}\t{translated}\n")
        
        # Small sleep to prevent IP blocking/rate limiting
        time.sleep(0.5)


except Exception as e:
    print(f"\nAn error occurred: {e}")


print(f"Done! Translated {translated_phrases} phrases.")
