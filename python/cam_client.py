"""
measure delay of sending webcam data in multiprocess context using ZeroMQ
ref: https://stackoverflow.com/questions/53049141/how-to-send-both-imagendarray-and-string-data-in-single-zmq-send-request
"""
import cv2
import zmq
import numpy as np
import time

def recv_array_and_str(socket, flags=0, copy=True, track=False):
    string = socket.recv_string(flags=flags)
    md = socket.recv_json(flags=flags)
    msg = socket.recv(flags=flags, copy=copy, track=track)

    img = np.frombuffer(bytes(memoryview(msg)), dtype=md['dtype'])
    return string, img.reshape(md['shape'])

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
socket.connect("tcp://localhost:5667")

delay = 0
frame_cnt = 0

while True:
    ts, img = recv_array_and_str(socket)
    recv_ts = time.time()
    delay += (recv_ts - float(ts)) * 1000 # ms
    frame_cnt += 1

    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print("average delay {:.2f}ms".format(delay / frame_cnt))

