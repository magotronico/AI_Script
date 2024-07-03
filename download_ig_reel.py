import instaloader
import os

# Initialize instaloader
L = instaloader.Instaloader()

def remove_non_mp4_files(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is not an mp4 file
        if not filename.endswith('.mp4'):
            # Construct full file path
            file_path = os.path.join(directory, filename)
            # Check if it's a file and not a directory
            if os.path.isfile(file_path):
                # Remove the file
                os.remove(file_path)
                print(f"Removed: {file_path}")

def reel(reel_url, num):
    # Extract the shortcode from the URL
    shortcode = reel_url.split("/")[-2]

    # Download the reel
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=f"videos")
        print(f"Reel downloaded successfully as video_{num}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Define the path to the Videos directory
    videos_directory = os.path.join(os.getcwd(), 'videos')

    # Call the function to remove non-mp4 files
    remove_non_mp4_files(videos_directory)

if __name__ == '__main__':
    reel_url = "https://www.instagram.com/reel/C8r_xd4uQCc/"
    num = 1
    reel(reel_url, num)
    
