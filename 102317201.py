import sys
import os
import yt_dlp
from pydub import AudioSegment

def get_videos(singer_name, num_videos):
    print(f"Searching and downloading {num_videos} videos for {singer_name}...")
    
    # yt-dlp options to download audio directly
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'default_search': 'ytsearch',
        'max_downloads': num_videos,
        'quiet': True
    }
    
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch{num_videos}:{singer_name} audio"])
    except Exception as e:
        print(f"Error downloading videos: {e}")
        sys.exit(1)

def process_and_merge(audio_duration, output_filename):
    print("Processing and merging audios...")
    merged_audio = AudioSegment.empty()
    downloaded_files = os.listdir('downloads')
    
    if not downloaded_files:
        print("No files were downloaded.")
        sys.exit(1)
        
    try:
        for file in downloaded_files:
            if file.endswith(".mp3"):
                file_path = os.path.join('downloads', file)
                # Load audio
                audio = AudioSegment.from_mp3(file_path)
                # Cut first Y seconds (pydub works in milliseconds)
                trimmed_audio = audio[:audio_duration * 1000]
                # Merge
                merged_audio += trimmed_audio
                
        # Export final file
        merged_audio.export(output_filename, format="mp3")
        print(f"Successfully created mashup: {output_filename}")
        
    except Exception as e:
        print(f"Error during audio processing: {e}")
        sys.exit(1)

def main():
    # Check for correct number of parameters
    if len(sys.argv) != 5:
        print("Error: Invalid number of arguments.")
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)
        
    singer_name = sys.argv[1]
    
    try:
        num_videos = int(sys.argv[2])
        audio_duration = int(sys.argv[3])
    except ValueError:
        print("Error: NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)
        
    output_filename = sys.argv[4]
    
    # Validation based on constraints
    if num_videos <= 10:
        print("Error: Number of videos (N) must be greater than 10.")
        sys.exit(1)
        
    if audio_duration <= 20:
        print("Error: Audio duration (Y) must be greater than 20 seconds.")
        sys.exit(1)
        
    if not output_filename.endswith('.mp3'):
        print("Error: Output filename must end with .mp3")
        sys.exit(1)

    get_videos(singer_name, num_videos)
    process_and_merge(audio_duration, output_filename)

if __name__ == "__main__":
    main()