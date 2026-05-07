# Luganda Batch Processor
Powered by *Google Translate*

A Python script that translates text files in batches using Google Translate, with built-in resume capability and rate limiting to avoid IP blocks.

## Features

- **Batch Translation**: Translates phrases in configurable batches for efficiency
- **Resume Support**: Automatically resumes from where it left off if interrupted
- **Rate Limiting**: Built-in delays to prevent IP blocking by Google Translate
- **Progress Tracking**: Visual progress bars using `tqdm`
- **Luganda Support**: Default target language is Luganda (can be modified)
- **Error Handling**: Gracefully handles errors and saves progress

## Prerequisites

- Python 3.6+
- Required packages:
  ```bash
  pip install deep-translator tqdm
  ```

## File Structure

```
project/
├── split_files/
│   ├── general_phrases_{ID}.txt      # Input files
│   └── translated/                    # Output directory
│       └── general_phrases_{ID}_translated.txt
└── translate.py                       # This script
```

## Usage

```bash
python translate.py <ID>
```

Where `<ID>` is the identifier of the file to translate.

### Example

```bash
python translate.py 001
```

This will:
- Read from: `split_files/general_phrases_001.txt`
- Write to: `split_files/translated/general_phrases_001_translated.txt`

## Input File Format

Each input file should contain one phrase per line:
```
Hello world
How are you?
Good morning
```

## Output File Format

Output files are tab-separated with original and translated text:
```
Hello world	Mirembe ensi
How are you?	Oli otya?
Good morning	Wasuze otya?
```

## Configuration

You can modify these variables at the top of the script:

| Variable | Default | Description |
|----------|---------|-------------|
| `RATE_LIMIT` | 0.5 | Seconds to wait between batches |
| `BATCH_SIZE` | 30 | Number of phrases per batch |
| `target` | 'lg' | Target language (lg = Luganda) |

### Changing Target Language

Modify this line in the script:
```python
translator = GoogleTranslator(source='auto', target='lg')  # Change 'lg' to your language code
```

Common language codes:
- `es` - Spanish
- `fr` - French
- `de` - German
- `zh` - Chinese
- `ja` - Japanese
- `lg` - Luganda

## How It Works

1. **Checks for existing output**: If a partial translation exists, it resumes from where it stopped
2. **Reads input**: Loads all untranslated phrases from the input file
3. **Batch translation**: Processes phrases in batches of 30 (default)
4. **Rate limiting**: Pauses between batches to avoid detection
5. **Appends results**: Writes translations to output file immediately after each batch
6. **Error recovery**: If interrupted, simply re-run with the same ID to resume

## Error Handling

- **Network issues**: The script will stop with an error message; just re-run to resume
- **IP blocking**: Increase `RATE_LIMIT` if you encounter blocking
- **File not found**: Ensure the input file exists before running

## Notes

- Google Translate has usage limits; consider increasing `RATE_LIMIT` for large files
- The script creates the `translated` directory automatically if it doesn't exist
- Uses UTF-8 encoding for full Unicode support

## License

Feel free to modify and distribute as needed.
```
