import whisper
from moviepy.editor import VideoFileClip
from deep_translator import GoogleTranslator
import os
from gtts import gTTS
from transformers import pipeline
import spacy

print('starting')
model_type_stt = "medium"
# Load the Whisper model
model = whisper.load_model(model_type_stt)
print('model loaded')
nlp = spacy.load("xx_ent_wiki_sm")
print('nlp loaded')
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print('summarizer loaded')

def extract_audio_from_video(video_file, output_audio_format="mp3"):
    """
    Extracts audio from a video file and saves it as a separate audio file.

    Parameters:
        video_file (str): The path to the video file from which audio will be extracted.
        output_audio_format (str, optional): The format of the output audio file. Defaults to "mp3".

    Returns:
        str: The path to the saved audio file.
    """
    video = VideoFileClip(video_file)
    audio_file = f"{video_file.rsplit('.', 1)[0]}.{output_audio_format}"
    # Disable logging for faster I/O
    video.audio.write_audiofile(audio_file, logger=None)
    return audio_file


def transcribe_with_whisper(audio_file, model=model):
    """
    Transcribes the given audio file using the specified model.

    Parameters:
        audio_file (str): The path to the audio file.
        model (Model): The model to use for transcription.

    Returns:
        str: The transcribed text.
    """
    # Transcribe the audio
    return model.transcribe(audio_file)


def translate_text(text, lang):
    """
    Translates the given text to the specified language.

    Parameters:
        text (str): The text to be translated.
        lang (str): The target language for translation.

    Returns:
        str: The translated text.
    """
    # Create a translator object and specify only the target language
    translator = GoogleTranslator(target=lang)
    # Translate the text
    return translator.translate(text)


def text2speech(text, lang='en'):
    """
    Converts text to speech using the specified language.

    Args:
        text (str): The text to be converted to speech.
        lang (str, optional): The language of the text. Defaults to 'en'.

    Returns:
        bytes or None: The audio data as bytes if successful, None otherwise.
    """
    try:
        # Initialize the TTS engine
        return gTTS(text=text, lang=lang)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def exctract_entities(text_lang):
    """
    Extracts entities from the given text in a specified language.

    Parameters:
        text_lang (str): The text in the specified language.

    Returns:
        list: A list of tuples containing the extracted entities. Each tuple contains the entity text and its label.
    """
    return [(ent.text, ent.label) for ent in nlp(text_lang).ents]


def summarized_text(text, lang):
    """
    Generates a summarized text in the specified language.

    Args:
        text (str): The text to be summarized.
        lang (str): The language of the text.

    Returns:
        str: The summarized text in the specified language.
    """
    if lang != 'en':
        en_text = translate_text(text, 'en')
    else:
        en_text = text
    en_summ_text = summarizer(en_text, max_length=200,
                              min_length=10, do_sample=False, truncation=True)
    return translate_text(en_summ_text[0]['summary_text'], lang)


def speech2text(video_file):
    """
    Converts a video file to text using speech recognition.

    Parameters:
        video_file (str): The path to the video file to be converted.

    Returns:
        dict: A dictionary containing the transcribed text and timecodes with text.
              The 'text' key holds the transcribed text as a string.
              The 'timecode_with_text' key holds a list of lists, where each inner list
              contains the start time, end time, and transcribed text for a segment.
              The start and end times are in seconds, and the text is a string.
    """
    audio_file = extract_audio_from_video(video_file)
    data = transcribe_with_whisper(audio_file)
    return {
        'timecode_with_text': [[x['start'], x['end'], x['text']] for x in data['segments']],
        'text': data['text']
    }


def main(video_file, lang='en'):
    """
    Generate the main function.

    Args:
        video_file (str): The path to the video file.
        lang (str, optional): The language to translate the text to. Defaults to 'en'.

    Returns:
        str: The path to the generated speech file.
    """
    print('start')
    d_text_timecodes = speech2text(video_file)
    print(f"d_text_timecodes: {d_text_timecodes}")
    translated_text = translate_text(d_text_timecodes['text'], lang)
    print(f"translated_text: {translated_text}")
    exctr_ents = exctract_entities(translated_text)
    print(f"exctr_ents: {exctr_ents}")
    summ_text = summarized_text(translated_text, lang)
    print(f"summ_text: {summ_text}")
    speech_file = text2speech(translated_text, lang)
    # TODO: save speech mp3 to file
    save_path = "./speech.mp3"  # Update with your desired save path
    with open(save_path, "wb") as file:
        speech_file.write_to_fp(file)
    return speech_file


# Example usage:
if __name__ == "__main__":
    video_file = "./video.mp4"  # Update with your video file path
    lang = 'en'
    print('starting main:')
    main(video_file, lang)