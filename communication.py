class CommunicationProtocol:
    def __init__(self):
        self.message_queue = Queue()
        
    def send_message(self, sender, receiver, message):
        """Handle inter-agent communication"""
        formatted_message = self.format_message(sender, receiver, message)
        self.message_queue.put(formatted_message) 