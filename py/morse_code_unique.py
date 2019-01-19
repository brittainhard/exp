MORSE_CODE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]


def get_code(c):
    return MORSE_CODE[ord(c) - 97]


def morse_code_unique(words):
    unique_codes = set()
    for w in words:
        code = []
        ws = list(w)
        for c in ws:
            code.append(get_code(c))
        unique_codes.add("".join(code))
    return len(unique_codes)


def test_morse_code():
    assert morse_code_unique(["gin", "zen", "gig", "msg"]) == 2
