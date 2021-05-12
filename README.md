# mira
Voice Assistant: Mira

İndirmeniz gereken kütüphaneler:
- SpeechRecognition
- PyAudio*
- playsound
- wikipedia (opsiyonel)

*PyAudio, speech_recognition.Microphone() için gereklidir.

macOS için PyAudio yüklerken bazı sorunlarla karşılaşabilirsiniz. Terminal üzerinden yüklemeniz gerekiyor. Homebrew kullanarak yükleme yaparsanız sorun çözülecektir.
  brew install portaudio
  pip install pyaudio
Sorun yaşamaya devam ederseniz:
  xcode-select --install
