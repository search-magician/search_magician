import subprocess
import sys

def check(name):
    is_available = True
    print('checking ' + name)
    try:
      print(subprocess.check_output(['which', name]))
    except Exception as e:
      print(e, e.output)
      is_available = False
    if not is_available:
      print(f"Could not find {name}.  Please run 'sudo apt-get install {name}'.")


if __name__ == "__main__":
    check("ffmpeg")
    fileName = sys.argv[1]
    if(fileName == ""):
        print("please add the file name as an arg to the script")

    fileName = fileName.replace(' ','\ ')
    command = f"ffmpeg -i {fileName} -ab 160k -ac 1 -ar 44100 -vn audio.wav"
    subprocess.call(command, shell=True)