from playsound import playsound

def play_audio(file_path):
    try:
        # Attempt to play the audio file
        playsound(file_path)
    except Exception as e:
        # Handle any exceptions that occur during playback
        print(f"Error playing audio: {e}")

# Specify the file path
audio_file_path = "Jkt48 Aitakatta.mp3"

# Call the play_audio function with the specified file path
play_audio(audio_file_path)
