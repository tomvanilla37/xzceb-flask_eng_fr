"""This modules translates from French to English and vice versa"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# In the constructor, letting the SDK manage the token
authenticator = IAMAuthenticator(apikey) # optional - the default value is https://iam.cloud.ibm.com/identity/token
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')
language_translator.set_disable_ssl_verification(True)


def englishToFrench(english_text):
    """translate from English to French"""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = (json.dumps(translation, indent=2, ensure_ascii=False))
    return french_text


def frenchToEnglish(french_text):
    """translate from French to English"""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = (json.dumps(translation, indent=2, ensure_ascii=False))
    return english_text
