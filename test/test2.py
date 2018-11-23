# import pyalsaaudio as alsaaudio, time, audioop
#
# inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
#
# inp.setchannels(1)
# inp.setrate(8000)
# inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
#
# inp.setperiodsize(160)
#
# while True:
#     # Read data from device
#     l,data = inp.read()
#     if l:
#         # Return the maximum of the absolute value of all samples in a fragment.
#         print audioop.max(data, 2)
#     time.sleep(.001)
import sounddevice as sd
import winsound as ws

fs = 44100
duration = 10000
datatype = 'int32'
fs2 = 200

ws.Beep(fs2,duration)


myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2,dtype=datatype)
sd.wait()
print("fin")
while True:
    myrecording = sd.playrec(myrecording, fs, channels=2)
    print("fin")
    sd.wait()
w











