import subprocess
URLS = [
    "https://www.youtube.com/watch?v=ySrNh4IOha4"

]

for url in URLS:
    subprocess.run(['yt-dlp',
                    "-f", "bestaudio",
                    "--extract-audio",
                    "--audio-format", "wav",
                    "--output", "../data/audio/%(id)s.%(ext)s",
                    url
                    ])

# output: data/audio/abc123.wav