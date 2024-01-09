from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
import os

def get_translation():
    translator = Translator()

    # Prompt user for language input
    target_language = input("Select target language (e.g., 'en' for English): ")

    # Ask the user how they want to input text
    input_option = input("Enter text or speak? (text/speak): ").lower()

    if input_option == 'text':
        # Prompt user for text input
        text_to_translate = input("Enter the text to translate: ")
    elif input_option == 'speak':
        # Capture user's voice input
        text_to_translate = recognize_speech()
    else:
        print("Invalid input option. Please choose 'text' or 'speak'.")
        return

    # Translate text
    translation = translator.translate(text_to_translate, dest=target_language)
    translated_text = translation.text

    # Print translated text
    print(f"\nTranslation ({translation.dest}): {translated_text}")

    # Prompt user to pronounce
    pronounce_option = input("Do you want to hear the pronunciation? (yes/no): ").lower()

    if pronounce_option == 'yes':
        pronounce_translation(translation, target_language)

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio, language="en")
        print(f"Text recognized: {text}")
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def pronounce_translation(translation, target_language):
    tts = gTTS(text=translation.text, lang=target_language)
    tts.save("translation.mp3")
    os.system("start translation.mp3")

if __name__ == "__main__":
    get_translation()