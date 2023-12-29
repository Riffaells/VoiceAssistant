from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import sounddevice as sd
import vosk
import json
import queue
import ask_gpt
import threading

q = queue.Queue()

model = vosk.Model('') # твой путь до модели воск
# model = vosk.Model('E:\\Downloads\\vosk-model-ru-0.42\\vosk-model-ru-0.42')
device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def start_assistant():
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                print(data)
                if len(data) > 0:
                    ask_gpt.ask_gpt(prompt=data)
            else:
                print(rec.PartialResult())


def main():
    start_assistant()


if __name__ == '__main__':
    main()
