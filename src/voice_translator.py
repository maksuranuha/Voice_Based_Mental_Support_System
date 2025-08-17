from deep_translator import GoogleTranslator
from langdetect import detect

def translator(text, target_language, input_language="auto"):
    
    language_codes = {
        'auto-detect': 'auto',
        'english': 'en',
        'spanish': 'es', 
        'french': 'fr', 
        'german': 'de', 
        'italian': 'it',
        'portuguese': 'pt', 
        'russian': 'ru', 
        'chinese': 'zh', 
        'japanese': 'ja',
        'korean': 'ko', 
        'arabic': 'ar', 
        'hindi': 'hi', 
        'dutch': 'nl',
        'polish': 'pl',
        'czech': 'cs',
        'slovak': 'sk',
        'bulgarian': 'bg',
        'croatian': 'hr',
        'serbian': 'sr',
        'romanian': 'ro',
        'hungarian': 'hu',
        'lithuanian': 'lt',
        'latvian': 'lv',
        'estonian': 'et',
        'slovenian': 'sl',
        'maltese': 'mt',
        'turkish': 'tr',
        'ukrainian': 'uk',
        'urdu': 'ur'
    }
    
    if input_language.lower() == "auto-detect" or input_language.lower() == "auto":
        source_code = 'auto'
        try:
            detected_lang = detect(text)
            print(f"Auto-detected language: {detected_lang}")
        except:
            print("Could not auto-detect language, using auto translation")
    else:
        source_code = language_codes.get(input_language.lower(), input_language.lower()[:2])
        print(f"Using specified input language: {input_language} ({source_code})")
    
    target_code = language_codes.get(target_language.lower(), target_language.lower()[:2])
    
    try:
        if source_code == 'auto':
            try:
                detected_lang = detect(text)
                source_code = detected_lang
                print(f"Auto-detected language: {detected_lang}")
            except:
                source_code = 'en'  
                print("Sorry, I could not auto-detect language, assuming English")
        
        translator_obj = GoogleTranslator(source=source_code, target=target_code)
        translated_text = translator_obj.translate(text)
        
        print(f"Original ({source_code}): {text}")
        print(f"Translated ({target_code}): {translated_text}\n")
        
        return translated_text, source_code
        
    except Exception as e:
        print(f"Translation error: {e}")
        return text, "unknown"

def get_language_name(code):
    code_to_name = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'pt': 'Portuguese',
        'ru': 'Russian',
        'zh': 'Chinese',
        'ja': 'Japanese',
        'ko': 'Korean',
        'ar': 'Arabic',
        'hi': 'Hindi',
        'nl': 'Dutch',
        'pl': 'Polish',
        'cs': 'Czech',
        'sk': 'Slovak',
        'bg': 'Bulgarian',
        'hr': 'Croatian',
        'sr': 'Serbian',
        'ro': 'Romanian',
        'hu': 'Hungarian',
        'lt': 'Lithuanian',
        'lv': 'Latvian',
        'et': 'Estonian',
        'sl': 'Slovenian',
        'mt': 'Maltese',
        'tr': 'Turkish',
        'uk': 'Ukrainian',
        'ur': 'Urdu'
    }
    return code_to_name.get(code, code.title())

def simple_translator(text, target_language):
    try:
        result, detected_lang = translator(text, target_language, "auto")
        return result
    except Exception as e:
        print(f"Translation failed: {e}")
        return text