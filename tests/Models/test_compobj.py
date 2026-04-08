from ms_oleds.compobj import CompObj
def test_to_bytes() -> None:
    expected = (
        b'\x01\x00\xfe\xff\x03\x0a\x00\x00\xff\xff\xff\xff\xf0i*\xc6'
        b'\xdc\x16\xce\x11\x9e\x98\x00\xaa\x00WJO\x19\x00\x00\x00'
        b'Microsoft Forms '
        b'2.0 Form\x00\x10\x00\x00\x00Emb'
        b'edded Object\x00\x0d\x00\x00'
        b'\x00Forms.Form.1\x00\xf49'
        b'\xb2q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    )
    obj = CompObj()
    obj._h_r1 = 0xfffe0001
    obj._ver = 0x0a03
    obj._h_r2 = (
        b'\xff\xff\xff\xff\xf0i*\xc6\xdc\x16'
        b'\xce\x11\x9e\x98\x00\xaa\x00WJO'
    )
    obj._type = 'Microsoft Forms 2.0 Form'
    obj._clipboard = 'Embedded Object'
    obj._r1 = 'Forms.Form.1'
    assert obj.to_bytes() == expected
    
        
