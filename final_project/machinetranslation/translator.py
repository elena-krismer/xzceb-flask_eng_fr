from deep_translator import MyMemoryTranslator

def english_to_french(english_text:str) -> str:
    """Tranlate english to french
    Args:
        english_text (str): english 
    Returns:
        str: french string
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text:str) -> str:
    """Tranlate french to english
    Args:
        french_text (str): french 
    Returns:
        str: english string
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
