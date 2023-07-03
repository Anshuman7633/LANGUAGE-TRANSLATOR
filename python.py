from translate import Translator

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translated = translator.translate(text)
    return translated

def main():
    while True:
        text = input("Enter the text to translate (or 'q' to quit): ")

        if text.lower() == 'q':
            break

        print("Supported Languages:")
        print("1. French")
        print("2. Italian")
        print("3. Hindi")
        print("4. Spanish")
        print("5. German")

        target_language = input("Enter the target language number: ")

        languages = {
            "1": "fr",
            "2": "it",
            "3": "hi",
            "4": "es",
            "5": "de"
            # Add more languages here with their corresponding language codes
        }

        if target_language not in languages:
            print("Invalid target language number.")
            continue

        target_language_code = languages[target_language]

        translated_text = translate_text(text, target_language_code)
        print("Translated text:", translated_text)
        print()

if __name__ == '__main__':
    main()
