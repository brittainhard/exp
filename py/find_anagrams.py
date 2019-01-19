words = ["dog", "silent", "listen", "god", "camera"]


def find_anagrams(words):
    anagrams = {}
    for x in words:
        sorted_key = "".join(sorted(x))
        if sorted_key not in anagrams:
            anagrams.update({sorted_key: {x}})
        else:
            anagrams[sorted_key].add(x)
    return anagrams.values()
