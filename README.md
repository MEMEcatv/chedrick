
```markdown name=README.md url=https://github.com/MEMEcatv/chedrick/blob/0f971adb8c7cb391b9e97576f95211f760f24dd1/README.md
# Chedrick - Преобразование файлов в видео и аудио

**Chedrick** - проект с открытым исходным кодом для преобразования любых файлов (текст, бинарные данные, изображения) в видео и аудио форматы с использованием пользовательских алгоритмов кодирования **h33** и **che5848**.

## Особенности

✨ **Два продвинутых формата кодирования:**
- **h33** - Преобразует файлы в видео через паттерны цветных квадратов (каждый байт = цветной квадрат)
- **che5848** - Преобразует файлы в аудио через модуляцию частоты (каждый байт = частота звука)

🔐 **Поддержка шифрования:**
- Шифруйте файлы перед кодированием флагом `-sh`
- PBKDF2 производство ключей от пароля
- SHA-256 контрольные суммы для проверки целостности
- Совместимость с AES-256

📹 **Видео выход:**
- Формат MP4 с кодеком H.264
- Настраиваемое разрешение и FPS
- Встроенный аудио трек

🔊 **Аудио выход:**
- Поддержка MP3 и WAV
- Диапазон частот: 50Hz - 20kHz
- ADSR конверт для формирования звука

## Установка

```bash
git clone https://github.com/MEMEcatv/chedrick.git
cd chedrick
pip install -r requirements.txt
```

## Требования

- Python 3.8+
- ffmpeg
- Зависимости из `requirements.txt`:
  - opencv-python
  - numpy
  - pydub
  - cryptography

## Использование

### Кодирование файла в видео (h33)

```bash
python chedrick.py encode -i input.txt -o output.mp4 -f h33
```

### Кодирование файла в аудио (che5848)

```bash
python chedrick.py encode -i input.txt -o output.mp3 -f che5848
```

### С шифрованием

```bash
python chedrick.py encode -i secret.txt -o encrypted_video.mp4 -f h33 -sh password123
```

### Декодирование

```bash
python chedrick.py decode -i output.mp4 -o recovered.txt -f h33
python chedrick.py decode -i output.mp3 -o recovered.txt -f che5848 -sh password123
```

## API

### Функции основного модуля

#### `encode(input_file, output_file, format, password=None)`
Кодирует файл в видео или аудио

**Параметры:**
- `input_file` (str) - путь к исходному файлу
- `output_file` (str) - путь к выходному файлу
- `format` (str) - формат кодирования: `h33` или `che5848`
- `password` (str, опционально) - пароль для шифрования

#### `decode(input_file, output_file, format, password=None)`
Декодирует видео или аудио обратно в исходный файл

**Параметры:**
- `input_file` (str) - путь к закодированному файлу
- `output_file` (str) - путь к во��становленному файлу
- `format` (str) - формат декодирования: `h33` или `che5848`
- `password` (str, опционально) - пароль для дешифрования

## Примеры

### Пример 1: Скрытие текстового файла в видео

```bash
# Кодирование
python chedrick.py encode -i secret_message.txt -o video.mp4 -f h33

# Декодирование
python chedrick.py decode -i video.mp4 -o decoded.txt -f h33
```

### Пример 2: Защита файла паролем

```bash
python chedrick.py encode -i important_data.bin -o audio.wav -f che5848 -sh MySecurePassword
python chedrick.py decode -i audio.wav -o recovered.bin -f che5848 -sh MySecurePassword
```

## Структура проекта

```
chedrick/
├── chedrick.py          # Основной модуль
├── encoders/
│   ├── h33.py          # Видео кодер
│   └── che5848.py      # Аудио кодер
├── decoders/
│   ├── h33.py          # Видео декодер
│   └── che5848.py      # Аудио декодер
├── crypto/
│   └── encryption.py   # Шифрование и дешифрование
├── requirements.txt
└── README.md
```

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле LICENSE.

## Вклад

Приветствуются pull requests! Для больших изменений сначала откройте issue для обсуждения предложенных изменений.

## Автор

**MEMEcatv** - [GitHub](https://github.com/MEMEcatv)

## Поддержка

Если у вас есть вопросы или найдены ошибки, пожалуйста, откройте [issue](https://github.com/MEMEcatv/chedrick/issues) в репозитории.

---

⭐ Если проект вам понравился, не забудьте поставить звезду!
```

