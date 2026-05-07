# Luganda Batch Processor
Powered by *Google Translate*

A Python script that batch-translates text files from English (auto-detected) to Luganda using Google Translate, with resume support and rate limiting to avoid IP blocking.

## Requirements

- Python 3.7 or higher
- Internet connection (for Google Translate API)

All dependencies are listed in `requirements.txt`:

- `deep-translator`
- `tqdm`

## Installation & Setup

1. Clone or download this repository to your local machine.

2. Create and activate a virtual environment (recommended):

   **On Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **On macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## File Structure

```
project_root/
│
├── raw_files/                    # Place your input files here
│   └── general_phrases_1.txt    # Example input file
│
├── translated_files/             # Translated output files will be saved here
│   └── general_phrases_1_translated.txt
│
├── translator.py                 # Main script
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Input File Format

Place your input files in the `raw_files/` folder using this naming convention:

`general_phrases_{ID}.txt`

Where `{ID}` is any unique identifier (number, text, etc.)

Each line in the input file should contain one phrase to translate. Empty lines are automatically skipped.

**Example** (`raw_files/general_phrases_1.txt`):
```
Hello, how are you?
Good morning
Thank you very much
```

## Usage

Run the script from the command line, providing the ID of the file you want to translate:

```bash
python translator.py [ID]
```

**Examples:**
```bash
python translator.py 1
python translator.py project_a
python translator.py test_001
```

This will:
- Read from: `raw_files/general_phrases_1.txt`
- Write to:   `translated_files/general_phrases_1_translated.txt`

## Features

- **Auto-resume**: If translation is interrupted, the script will pick up where it left off (skips already translated lines)
- **Batch processing**: Translates 30 phrases at a time for efficiency
- **Rate limiting**: 0.5 second delay between batches to avoid IP blocking
- **Progress bar**: Shows real-time translation progress using `tqdm`
- **Error handling**: Continues to save progress even if an error occurs
- **Tab-separated output**: Original and translated phrases are separated by tabs

## Output Format

The translated file contains tab-separated values:

```
Original phrase 1    Translated phrase 1
Original phrase 2    Translated phrase 2
Original phrase 3    Translated phrase 3
```

## Notes

- The script translates from `auto` (auto-detects source language) to `lg` (Luganda)
- A small delay is added between batches to prevent IP blocking by Google Translate
- If you need to change the target language, modify the `target='lg'` parameter in the script
- The script creates the `translated_files` folder automatically if it doesn't exist

## Troubleshooting

**Error: `No module named 'deep_translator'`**  
→ Make sure you've activated your virtual environment and run `pip install -r requirements.txt`

**Translation stops midway**  
→ Just run the same command again - the script will resume from where it stopped

**IP blocked by Google**  
→ Increase the `RATE_LIMIT` value in the script (e.g., change from 0.5 to 1.0 seconds)

## License

Feel free to use and modify as needed.
```
