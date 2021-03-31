from pydub import AudioSegment
import sys
sound = AudioSegment.from_mp3(sys.argv[1])
fileName = sys.argv[1]
newFileName = fileName[:-3] + "wav"
sound.export(newFileName, format="wav")