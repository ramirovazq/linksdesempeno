import base64

def decode_msg(msg_in_64):
    base64_message = msg_in_64
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message
