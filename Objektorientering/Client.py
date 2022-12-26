import vidTransfer as v
import cv2

client = v.VideoClient(clientAddress="192.168.10.155", port="1234")

while True:
    frame = client.grabFrame()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
client.stop()
cv2.destroyAllWindows()