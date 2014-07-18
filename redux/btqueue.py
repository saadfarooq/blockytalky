def server(port="5556"):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:%s" % port)
    print "Running server on port: ", port
    # serves only 5 request and dies
    for reqnum in range(5):
        # Wait for next request from client
        message = socket.recv()
        print "Received request #%s: %s" % (reqnum, message)
        socket.send("World from %s" % port)
         
def client(ports=["5556"]):

    context = zmq.Context()
    print "Connecting to server with ports %s" % ports
    socket = context.socket(zmq.REQ)
    for port in ports:
        socket.connect ("tcp://localhost:%s" % port)
    for request in range (20):
        print "Sending request ", request,"..."
        socket.send ("Hello")
        message = socket.recv()
        print "Received reply ", request, "[", message, "]"
        time.sleep (1) 