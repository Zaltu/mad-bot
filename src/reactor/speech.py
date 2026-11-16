from omnivoice import OmniVoice, VoiceClonePrompt
import soundfile as sf
from torch import float16

from src.consts import DBPATH
import os

MODEL = OmniVoice.from_pretrained(
    "k2-fsa/OmniVoice",
    device_map="cuda:0",
    dtype=float16
)
VOICE_SAMPLE = VoiceClonePrompt.load(os.path.join(DBPATH, "aigis_voice_sample.pt"))

def generate_audio(text, path=""):
    audio = MODEL.generate(text, voice_clone_prompt=VOICE_SAMPLE)
    filepath = os.path.join(path, f"{text[:10]}.wav")
    sf.write(filepath, audio[0], 24000)
    return filepath
