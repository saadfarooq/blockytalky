import OSC

# nickOSC.py
# Contains a few methods to make it easier
# to send OSC messages from blocks.

note_destination_hostname = "localhost"
note_destination_port = 1111

client = OSC.OSCClient()
client.connect( (note_destination_hostname, note_destination_port) )

def simple_play(notes):
	message = OSC.OSCMessage()
	# copy note content into message
	for i in range(len(notes)):
		print "currently on " + str(notes[i])
		print notes
		print notes[i]
		print notes[i][0]
		message.append(float(notes[i][0]))
		message.append(int(notes[i][1]))
	# pad message with empty notes
	# (phrases require 64 notes sent)
	for i in range(64 - len(notes)):
		message.append(-1)
		message.append(0.)
	client.send(message)
	print "message sent to " + note_destination_hostname + " from simple_play"