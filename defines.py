from deep_translator import GoogleTranslator
import pycountry

translator = GoogleTranslator()


def S_L(x):
    supported_languages = translator.get_supported_languages()

    for language_name in supported_languages:
        try:
            language_code = pycountry.languages.get(name=language_name).alpha_2
            x.append(f"{language_name} : {language_code}")
        except AttributeError:
            x.append(f"{language_name} : not found")


def Translating(text):
    translated = GoogleTranslator(
        source='auto', target='en').translate(text=text)
    return translated
