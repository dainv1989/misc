"""
measure delay of sending webcam data in multiprocess context using ZeroMQ
ref: https://stackoverflow.com/questions/53049141/how-to-send-both-imagendarray-and-string-data-in-single-zmq-send-request
"""
import cv2
import zmq
import time
import numpy as np

def send_array_and_str(socket, img, string, flags=0):
    md = dict(dtype = str(img.dtype), shape=img.shape)

    socket.send_string(string, flags | zmq.SNDMORE)
    socket.send_json(md, flags | zmq.SNDMORE)
    return socket.send(img, flags)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5667")
time.sleep(0.2)

my_ndarray = np.array([1, 2, 3])
my_string = "Hello World"
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        ts = time.time()
        send_array_and_str(socket, frame, str(ts))
