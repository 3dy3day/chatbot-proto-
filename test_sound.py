# from playsound import playsound

# playsound("audio.wav")

import simpleaudio

wav_obj = simpleaudio.WaveObject.from_wave_file("audio.wav")
play_obj = wav_obj.play()
play_obj.wait_done()