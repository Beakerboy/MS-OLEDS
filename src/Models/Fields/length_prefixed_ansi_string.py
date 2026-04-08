import struct
from typing import TypeVar


T = Typevar('T', bound='LengthPrefixedString')


class LengthPrefixedString:

    def __init__(self:T, value: str) -> None:
        self._value = value

    def to_bytes(self: T) -> bytes:
        return (
            struct.pack("<I", len(self._value) + 1) +
            self._value.encode("ansi") + "\x00)
        
