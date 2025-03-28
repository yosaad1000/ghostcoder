# 🚀 Ollama Auto-Responder with Hotkeys

This script allows users to interact with the **Ollama** AI model using custom global hotkeys. It enables users to quickly fetch AI-generated responses for highlighted text and automatically type them in any active input field. The script simulates human-like typing and includes additional features such as stopping mid-typing and a notification sound upon response retrieval.

## ✨ Features
- **Quick AI Querying**: Highlight text and press a hotkey to get an AI-generated response instantly.
- **Simulated Typing**: The AI response is typed character by character for a natural effect.
- **Customizable Hotkeys**: Uses unique key combinations to prevent interference with existing shortcuts.
- **Stop Typing Anytime**: Interrupt the AI-generated response typing with a hotkey.
- **Beep Notification**: Alerts the user when the response is ready.
- **Code Extraction & Formatting**: Ensures that only the essential code is typed, removing extra indentation and unnecessary spaces.

---

## 📥 Installation

### Prerequisites:
1. **Download and Install Ollama:**
   - Visit [Ollama's official download page](https://ollama.com/download) and install it for your platform.
   - Ensure Ollama is running by executing the following command in the terminal:
     ```sh
     ollama serve
     ```

2. **Install the required Ollama model:**
   - Run this command to download and set up the `codellama` model (or any other model of your choice):
     ```sh
     ollama run codellama
     ```

3. **Modify the script to match your AI model and role:**
   - Open the script file and change the `OLLAMA_MODEL` variable to your preferred model name.
   - Modify the `role` inside `chat_messages` to set your desired AI behavior.

4. **Install required dependencies using:**
   ```sh
   pip install -r requirements.txt
   ```

### Required Libraries:
- `keyboard` → Detects and binds hotkeys.
- `pyperclip` → Manages clipboard operations.
- `pyautogui` → Simulates keyboard typing.
- `ollama` → Interacts with the AI model.
- `threading`, `random`, `time`, `sys`, `re` → Supports various functionalities.
- `winsound` (Windows) or `os.system("afplay sound.wav")` (Mac) for notifications.

---

## 🛠 Usage Instructions

1. **Run the script**
   ```sh
   python script.py
   ```

2. **Hotkeys Available:**
   - 🔹 `F8` → Query AI with highlighted text
   - 🔹 `F9` → Start typing the AI response
   - 🔹 `F10` → Stop typing immediately

3. **Workflow:**
   - Highlight any text (e.g., a coding question).
   - Press `F8` → Sends the text to Ollama.
   - After receiving a response, you'll hear a **beep**.
   - Press `F9` to start typing the response.
   - If needed, press `F10` to stop typing mid-way.

---

## 🔥 Example Output

### **Query:**
> `bubble sort in C++`

### **AI Response (Typed Output):**
```cpp
#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        bool swapped = false;
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }
}
```

---

## 🛑 Troubleshooting
- **Hotkeys not working?** Ensure the script is running in the background.
- **AI not responding?** Check your internet connection and that **Ollama** is properly installed.
- **Beep sound not playing?** Windows users should hear a system beep. Mac/Linux users might need `afplay` or another sound method.

---

## 🎯 Future Enhancements
- ✅ More customizable hotkeys
- ✅ Option to select AI models dynamically
- ✅ Improved handling of code formatting
- ✅ Multi-language support

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

🚀 **Happy Coding!**