#!/usr/bin/env python3
import sys
from .dicttable import find_by_name
import struct


def dcm_need_reserved(vr):
    reserved = ["AE", "AS", "AT", "CS", "DA", "DS", "DT", "FL", "FD", "IS", "LO", "LT", "PN", "SH",
                "SL", "SS", "ST", "TM", "UI", "UL", "US"]
    return vr.decode() not in reserved


def dcm_write_file(buffer, filename):
    print(f"Writing file to {filename}")
    with open(sys.argv[1], "wb") as f:
        f.write(buffer)


def dcm_add_header():
    return b'\x00' * 16 * 8


def dcm_add_magic():
    return struct.pack("<I", 0x4d434944)  # DICM


def dcm_add_element(name, length, body):
    if length != 0xFFFFFFFF and len(body) < length:
        print(f"Invalid length for element {name} - expected \
                {length} found {len(body)}")
        sys.exit(-1)
    buf = b''
    element = find_by_name(name)
    if not element:
        print(f"Unable to find element {name} on the dict table")
        sys.exit(-1)
    tag, ul, _ = element

    buf += struct.pack("<H", ((tag & 0xffff0000) >> 16))  # First 4 bytes of the tag
    buf += struct.pack("<H", (tag & 0xffff))  # Second 4 bytes of the tag
    buf += ul.encode()  # UL
    need_reserved_byte = dcm_need_reserved(ul.encode())
    # Some tags require reserved byte and the length field is 4 bytes long
    if need_reserved_byte:
        buf += struct.pack("<H", 0x0)
        buf += struct.pack("<I", length)
    else:
        buf += struct.pack("<H", length)
    buf += body
    return buf

