"""
Blocky Talky - Message (message.py)

A utility module for creating message objects used for communication in the
Blocky Talky system.
"""
import jsonpickle   # Install via "pip install jsonpickle"
                    # Doc: http://jsonpickle.github.io/

class Message(object):
    # Add new entries to this list when creating channels.
    validChannels = (
                        "Subs",     # Subscription
                        "HwVal",    # Hardware values
                        "HwCmd",    # Hardware commands
                        "MsgIn",    # Incoming remote messages (invisible, within mp.py)
                        "MsgOut",   # Outgoing remote messages (invisible, within mp.py)
                        "Message",  # Visible channel for all messages
                        "Logging",   # Data logging of user
                        "Sensor",
                        "Server"    # Data coming from the central server
                    )

    def __init__(self, source, destination, channel, content = None):
        """
        Creates an instance of the Message class. The result can
        be encoded into JSON format and forwarded to other modules.

        --- Parameters ---
            source:         The name of the module that created the
                            message.

            destination:    The hostname of the client the message should
                            be sent to.

            channel:        The destination where the message will be
                            distributed to the recipients.

            content:        The body of the message. Contains detailed
                            information.
        """
        if channel in Message.validChannels:
            self.channel = channel
        else:
            raise TypeError("Incorrect channel type.")

        self.source  = source
        self.destination = destination
        self.content = content

    def getSource(self):
        return self.source

    def getDestination(self):
        return self.destination

    def getChannel(self):
        return self.channel

    def getContent(self):
        return self.content

    def __eq__(self, otherMessage):
        return (self.source == otherMessage.getSource() and
                self.destination == otherMessage.getDestination() and
                self.channel == otherMessage.getChannel() and
                self.content == otherMessage.getContent())

    def __str__(self):
        return ("\n<< Source >>\n\t" + str(self.source) +
                "\n<< Destination >>\n\t" + str(self.destination) +
                "\n<< Channel >>\n\t" + str(self.channel) +
                "\n<< Content >>\n\t" + str(self.content))

    @staticmethod
    def encode(message):
        """
        Returns the message encoded in JSON.
        Static method, usage: Message.encode(message)
        """
        return jsonpickle.encode(message)

    @staticmethod
    def decode(encodedMessage):
        """
        Decodes a JSON formatted message and returns it.
        Static method, usage: Message.decode(encodedMessage)
        """
        return jsonpickle.decode(encodedMessage)

    @staticmethod
    def createImage(
                    led1 = None,
                    led2 = None,
                    motor1 = None,
                    motor2 = None,
                    motor3 = None,
                    motor4 = None,
                    encoder1 = None,
                    encoder2 = None,
                    encoder3 = None,
                    encoder4 = None,
                    sensor1 = None,
                    sensor2 = None,
                    sensor3 = None,
                    sensor4 = None,
                    pin7 = None,
                    pin11 = None,
                    pin13 = None,
                    pin15 = None,
                    pin12 = None,
                    pin16 = None,
                    pin18 = None,
                    pin22 = None,
                    type1 = None,
                    type2 = None,
                    type3 = None,
                    type4 = None
                   ):
        """
        Returns a dictionary containing the values of hardware elements that
        have changed since the last message.
        """
        return {
                "leds": [led1, led2],
                "motors": [motor1, motor2, motor3, motor4],
                "encoders": [encoder1, encoder2, encoder3, encoder4],
                "sensors": [sensor1, sensor2, sensor3, sensor4],
                "pins": [pin7, pin11, pin13, pin15, pin12, pin16, pin18, pin22],
                "types": [type1, type2, type3, type4]
               }

    @staticmethod
    def initStatus():
       """
       Returns a dictionary containing the startup values of the BrickPi.
       """
       return Message.createImage(
                                   led1 = 0,
                                   led2 = 0,
                                   motor1 = 0,
                                   motor2 = 0,
                                   motor3 = 0,
                                   motor4 = 0,
                                   encoder1 = 0,
                                   encoder2 = 0,
                                   encoder3 = 0,
                                   encoder4 = 0,
                                   sensor1 = 255,
                                   sensor2 = 255,
                                   sensor3 = 255,
                                   sensor4 = 255,
                                   pin7 = None,
                                   pin11 = None,
                                   pin13 = None,
                                   pin15 = None,
                                   pin12 = None,
                                   pin16 = None,
                                   pin18 = None,
                                   pin22 = None,
                                   type1 = 0,
                                   type2 = 0,
                                   type3 = 0,
                                   type4 = 0
                                 )
    @staticmethod
    def createSensorStatus():       
        return {
                "sensor1": False,
                "sensor2": False,
                "sensor3": False,
                "sensor4": False,
                "encoder1": False,
                "encoder2": False,
                "encoder3": False,
                "encoder4": False
               }
