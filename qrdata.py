from imutils.video import VideoStream
import imutils
import cv2
import time
from pyzbar import pyzbar
from playsound import playsound

def decoder(to_decode):
	found = ""
	codes = pyzbar.decode(to_decode)
	for code in codes:
		codeData = code.data.decode("utf-8")
		if codeData not in found:
			found += codeData
	
	return found
def qrdata():
	bought = []
	vs = VideoStream(src=0).start()		
	time.sleep(1.0)
	while True:
		frame = vs.read()
		frame = imutils.resize(frame, width=400)

		cv2.imshow("Scanner", frame)	
		key = cv2.waitKey(1) % 0xFF
		
		data = decoder(frame)	
		
		if data != "":		
			strdata = str(data)
			playsound("scan.wav")
			print(strdata)
			bought.append(strdata)

		if key == ord(' '):
			break
	cv2.destroyAllWindows()
	vs.stop()
	return bought
