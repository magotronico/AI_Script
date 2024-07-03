from openai import OpenAI
client = OpenAI()

def transcript(num):
    audio_file= open(f"C:/Users/dilan/Documents/Github/Videos/AI_Script/videos/video_{num}.mp4", "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    return transcription.text

if __name__ == '__main__':
    transcription = transcript(3)
    print(transcription)