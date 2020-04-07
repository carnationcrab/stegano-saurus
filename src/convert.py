# Converts file to binary and back again
from binascii import b2a_hex, a2b_hex

START_BUFFER = b'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'
END_BUFFER = b'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
TAB = b'\t'


def py_to_binary():

    FILE = 'hello_world.py'
    text_file = open(FILE, 'rb')
    hidden_file = FILE.split('.')[-1]

    text = text_file.read()
    text += TAB

    # add buffers and file format
    text += START_BUFFER + TAB
    text += str.encode(hidden_file) + TAB
    text += END_BUFFER
    text_file.close()

    # convert to hex string
    hex_text = b2a_hex(text).decode('ascii')
    # convert hex to binary
    b = ''
    for ch in hex_text:
        tmp = bin(ord(ch))[2:]
        if len(tmp) < 7:
            for _ in range(0, (7 - len(tmp))):
                tmp = '0' + tmp
        b += tmp
    return b


def reconstitute(raw_bits):
    # break long string into array for bytes
    b = [raw_bits[i:i + 7] for i in range(0, len(raw_bits), 7)]
    # convert to string
    c = ''
    for i in b:
        c += chr(int(i, 2))
        # if the string length is not even, add a digit
    if len(c) % 2 != 0:
        c += 'A'

    # convert back to ascii
    as_ascii = a2b_hex(c[:-10].encode('ascii'))

    print('AS_ASCII:', as_ascii)

    # check to see if the buffer is intact still
    buffer_idx = as_ascii.find(START_BUFFER)

    if buffer_idx != -1:
        fc = as_ascii[:buffer_idx]
    else:
        raise Exception('[!] Failed to find message buffer...')

    payload_file_type = '.py'


    to_save = open('hidden_file' + payload_file_type, 'wb')
    to_save.write(fc)
    to_save.close()
    print('[+] Successfully extracted message: {}{}'.format('hiddenFile', payload_file_type))
    return 'hidden_file' + payload_file_type


strang = py_to_binary()
reconstitute(strang)