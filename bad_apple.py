import os
import requests
import time

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def fetch_bad_apple_frames():
    url = "https://github.com/chezzakowo/BadApple/raw/main/frame.txt"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text.split("\n\n")
    else:
        print("Lỗi tìm File chứa khung hình!")
        return []

def display_frame(frame):
    clear_console()
    print(frame)

def main():
    time.sleep(1)  
    frames = fetch_bad_apple_frames()
    
    if not frames:
        return
    
    frame_duration = 1/60  # Chỉnh FPS ở đây
    
    for frame in frames:
        lines = frame.split("\n")
        timecode_line = lines.pop(0)
        timecode = timecode_line.split(" --> ")[0]
        frame_delay = float(timecode.replace(",", "."))
        display_frame("\n".join(lines))
        time.sleep(frame_duration)

if __name__ == "__main__":
    main()
