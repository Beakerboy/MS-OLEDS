import struct
from typing import TypeVar


T = TypeVar('T', bound='CompObj')


class CompObj:

    def __init__(self: T) -> None:
        self._h_r1 = 0
        self._h_r2 = b''
        self._ver = 0
        self._type = ''
        self._clipboard = ''

    def to_bytes(self: T) -> bytes:
        type = LengthPrefixedString(self._type)
        clipboard = LengthPrefixedString(self._clipboard)
        output = b''
        header = (
            struct.pack('<II', self._h_r1, self._ver) +
            self._h_r2
        )
        output += (
            header + type.to_bytes() + clipboard.to_bytes() +
            struct.pack('<IIII', 0x71B239F4, 0, 0, 0)
            
        return output
