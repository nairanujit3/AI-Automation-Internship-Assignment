import speech_recognition as sr

def listen_for_query():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎙️ Say your search query...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"✅ You said: {query}")
        return query
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"⚠️ Could not request results; {e}")
    
    return None
