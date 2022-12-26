import vidTransfer as v

stream = v.VideoStream(clientAddress="192.168.10.155", port="1234")

while True:
    try:
        stream.sendFrame()
    except KeyboardInterrupt:
        break
stream.stop()
