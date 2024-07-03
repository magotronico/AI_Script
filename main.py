from download_ig_reel import reel
from whisper_gen_transcript import transcript
from generate_new_script import new_script


# List of Instagram Reel links
video1 = "https://www.instagram.com/reel/C8r_xd4uQCc/"
video2 = "https://www.instagram.com/reel/C8kQqWPPP8F/"
video3 = "https://www.instagram.com/reel/C8c658ZSCp9/"

# Variables
videos = [video1, video2, video3]
transcripts = []


# Main function
def main():
    # Download the videos and generate transcripts
    for num, video in enumerate(videos):
        downloaded_Vid = reel(video, num)
        transcripts.append(transcript(downloaded_Vid))

    # Generate new script
    newScript = new_script(transcripts)
    print(f"New Script Suggested:\n\n{newScript}")

if __name__ == "__main__":
    main()
