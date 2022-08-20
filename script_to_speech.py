from gtts import gTTS
import os


#  Consider using language parameter to translate into other languages
def script_to_speech(in_text: str, f_name: str, dest="", language="en"):
    audio_obj = gTTS(text=in_text, lang=language, slow=False)
    audio_obj.save(f_name + ".mp3")


if __name__ == '__main__':
    sample_text = "What is a myth that is passed from generation to generation," \
                  "and people still believe it?"
    script_to_speech(sample_text, "sample_audio", '/sample_dir/')

    os.system('afplay ' + 'sample_audio.mp3')
