# Lines Translator

Eng - Luganda support tool.

## 📋 Prerequisites

- Python 3.7 or higher
- Git (for cloning the repository)

## 🚀 Getting Started

### 1. Clone the Repository

`bash
git clone <your-repo-url>
cd <repo-name>
`

### 2. Create and Activate a Virtual Environment

**Windows:**
`bash
python -m venv venv
venv\Scripts\activate
`

### 3. Install Dependencies

`bash
pip install -r requirements.txt
`

### 4. Run the Translator

`bash
python lines_translator.py
`

## 🔄 Handling Interruptions and Resuming

The translation process may take a long time depending on the file size. This tool includes checkpoint functionality to allow you to resume from where it stopped.

### Important Workflow:

1. **During execution**: The script displays a tqdm progress bar showing the current progress:
   
   `text
   Translating: 45%|████▌     | 38/128 [00:30<00:37, 148.2 lines/s]
   `

2. **If the process stops** (due to error, network issues, or manual interruption):
   - Open the output file (the translated file being created)
   - Look at the **last successfully translated line number**
   - Note this number

3. **Resume translation**:
   - Open `lines_translator.py` in a text editor
   - Locate the `START` variable (usually near the top of the file)
   - Update it to the line number where the previous run stopped
   
   Example:
   `python
   # Before
   START = 0  # Start from beginning
   
   # After (resuming from line 4500)
   START = 4500  # Resume from line 4500
   `

4. **Re-run the script**:
   `bash
   python lines_translator.py
   `
   
## 👨‍💻 Author

**Written by: Michael**

---

For questions, suggestions, or issues, please feel free to reach out or submit an issue in the repository.

## 📄 License

This project is open source and free to use. You are free to:

- Use this software for any purpose
- Modify and adapt it to your needs
- Distribute copies of the software
- Use it commercially

No warranty is provided, and the author assumes no liability for any issues that may arise from using this software.

**This project is released under the MIT License.**

---

The MIT License

Copyright (c) 2026 Michael

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
