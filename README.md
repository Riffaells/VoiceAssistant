Как установить?

1. Download and Install NodeJS >= 18.15.0

Install Flowise

npm install -g flowise

Start Flowise

npx flowise start

После зайти на localhost:3000 => Add New => Нажать на шестеренку и загрузить файл RAG_01 chatflow.json. Добавить ключ API к chat gpt и сохранить

2. Установка модели VOSK

Перейти на https://alphacephei.com/vosk/models и установить от сюда "vosk-model-small-ru-0.22"
После в файле app.py указать путь до модели VOSK

3. Настройка API, перейти на localhost:3000 и в модели получить свой API на обращение к ней, после чего вставить в ask_gpt.py

4. В words.py установлено слово тригер, слово после которого ассистент начнет слушать
