import sys

operation = input()
print(operation, file=sys.stderr)

pseudo_random_number = int(input())
print(pseudo_random_number, file=sys.stderr)

rotors = [input() for _ in range(3)]
print(rotors, file=sys.stderr)

message = input()
print(message, file=sys.stderr)


def encode_caesar(shift_no, msg):
    tmp = []
    for m in msg:
        tmp.append(chr((ord(m) - ord('A') + shift_no) % 26 + ord('A')))
        shift_no = (shift_no + 1) % 26
    return ''.join(tmp)


def encode_rotor(rotors, msg):
    return ''.join(rotors[ord(m) - ord('A')] for m in msg)


def decode_caesar(shift_no, msg):
    shift_no = (shift_no + len(msg) - 1) % 26
    tmp = []
    for m in reversed(msg):
        tmp.append(chr((ord(m) - ord('A') - shift_no) % 26 + ord('A')))
        shift_no = (shift_no - 1) % 26
    return ''.join(reversed(tmp))


def decode_rotor(rotors, msg):
    decode_map = {r: i for i, r in enumerate(rotors)}
    return ''.join(chr(decode_map[m] + ord('A')) for m in msg)


if operation == 'ENCODE':
    message = encode_caesar(pseudo_random_number, message)
    for r in rotors:
        message = encode_rotor(r, message)
    print(message)

elif operation == 'DECODE':
    for r in reversed(rotors):
        message = decode_rotor(r, message)
    message = decode_caesar(pseudo_random_number, message)
    print(message)
