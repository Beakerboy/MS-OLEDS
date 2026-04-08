import struct
from typing import TypeVar


T = TypeVar('T', bound='CompObj')


class CompObj:

    def __init__(self: T) -> None:
        self._r1 = 0
        self._r2 = b''
        self._ver = 0
        self._type = ''
        self._clipboard = ''

    def to_bytes(self: T) -> bytes:
        type = LengthPrefixedString(self._type)
        output = b''
        header = (
            struct.pack('<II', self._r1, self._ver) +
            self._r2
        )
        output += header + type.to_bytes()
        return output
