from flask import Flask,render_template,Response
import cv2
# setup video capture
cam = cv2.VideoCapture(0)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
def gen(cam):
	while True:
		ret,img = cam.read()
		ret,jpegdata=cv2.imencode("capture.jpeg",img)
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+jpegdata.tobytes()+b'\r\n')
		

@app.route('/video_feed')
def video_feed():
	return Response(gen(cam),mimetype='multipart/x-mixed-replace; boundary=frame')
	
if __name__=='__main__':
	app.run(host='localhost', port=8080)
