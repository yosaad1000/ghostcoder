import keyboard
import pyperclip
import pyautogui
import ollama
import time
import random
import threading
import sys
import re

# 🔹 Import sound module based on OS
if sys.platform == "win32":
    import winsound
else:
    import os

OLLAMA_MODEL = "mistral:latest"
response_text = ""
stop_typing = False
typing_thread = None


def beep():
    """Plays a small notification sound when response is ready."""
    try:
        if sys.platform == "win32":
            winsound.Beep(1000, 200)  # Beep at 1000 Hz for 200ms
        else:
            os.system("printf '\a'")  # Terminal beep sound (Linux/macOS)
    except Exception as e:
        print(f"⚠️ Error playing beep sound: {e}")


def extract_code_block(text):
    """Extract the first code block from the response."""
    match = re.search(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else ""


def get_highlighted_text():
    """Retrieve text from clipboard."""
    time.sleep(0.2)
    copied_text = pyperclip.paste().strip()

    if not copied_text:
        print("⚠️ No text found in clipboard! Copy manually before pressing F8.")
    else:
        print(f"📋 Copied Text: {copied_text}")

    return copied_text


def ask_ollama():
    """Send highlighted text to Ollama and store response."""
    global response_text
    query = get_highlighted_text()

    if not query:
        return

    print(f"\n🔎 Querying Ollama ({OLLAMA_MODEL} model): {query}")
    response_text = ""

    chat_messages = [
        {"role": "system", "content": "Generate a single, simplified and easy C++ function using STL. Do NOT include any comments, header files, or input/output operations. Only provide one block of code with the most efficient implementation. Ensure each response is unique and does not reference previous interactions"},
        {"role": "user", "content": query}
    ]

    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=chat_messages,
            stream=True
        )

        full_response = ""
        for part in response:
            full_response += part["message"]["content"]

        print("\n💬 Ollama's Full Response:\n" + full_response)

        # 🔍 Extract only the code block
        response_text = extract_code_block(full_response)

        if response_text:
            print("\n📝 Extracted Code:\n" + response_text)
        else:
            print("⚠️ No code block found in response!")

        # 🔔 Play beep notification when response is ready
        beep()

    except Exception as e:
        print(f"❌ Error querying Ollama: {e}")
        response_text = "Error fetching response from Ollama."


def type_response():
    """Simulate human-like character-by-character typing while adjusting indentation."""
    global response_text, stop_typing, typing_thread

    if not response_text:
        print("⚠️ No code block found to type!")
        return

    print("⌨️ Typing response...")
    stop_typing = False

    def typing_task():
        global stop_typing
        lines = response_text.split("\n")

        for line in lines:
            if stop_typing:
                print("\n⏹️ Typing stopped!")
                break

            # Strip all leading spaces except the first character
            stripped_line = line.lstrip()

            for index, char in enumerate(stripped_line):
                if stop_typing:
                    print("\n⏹️ Typing stopped!")
                    return

                # Type one character at a time
                pyautogui.write(char)
                time.sleep(random.uniform(0.05, 0.15))  # Simulate natural typing speed

            pyautogui.press("enter")  # Move to next line

    typing_thread = threading.Thread(target=typing_task)
    typing_thread.start()


def stop_typing_command():
    """Stops the typing process."""
    global stop_typing, typing_thread
    stop_typing = True

    if typing_thread and typing_thread.is_alive():
        typing_thread.join()

    print("\n⏹️ Typing manually stopped!")


# 🔹 Shorter, conflict-free hotkeys
keyboard.add_hotkey("f8", ask_ollama)  # Query Ollama
keyboard.add_hotkey("f9", type_response)  # Start typing response
keyboard.add_hotkey("f10", stop_typing_command)  # Stop typing mid-response

print("\n🚀 Hotkeys Ready! Use:")
print("  - F8 → Ask Ollama (highlight & copy text first)")
print("  - F9 → Start typing response")
print("  - F10 → Stop typing immediately")

keyboard.wait()
