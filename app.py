
import os
from scipy.io.wavfile import write
import demucs.separate

print("Hello song")


os.makedirs("out", exist_ok=True)

#os.system("python3 -m demucs.separate -n htdemucs --two-stems=vocals test.wav -o out")
demucs.separate.main(["-n", "htdemucs", "--mp3", "--two-stems=vocals", "test.mp3", "-o", "out"])
#return "./out/htdemucs/test/vocals.wav","./out/htdemucs/test/no_vocals.wav"