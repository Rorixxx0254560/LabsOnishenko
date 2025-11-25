#бибилиотека re
import re

#перевод текста в строчный вид
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё","е").replace("Ё","Е")
    text = text.replace("\r"," ").replace("\t"," ")
    text = text.strip()
    text = text.split()
    text = " ".join(text)
    return text

#превращение строки в кортеж
def tokenize(text: str) -> list[str]:
    return re.findall(r"[\w-]+", text)

#
def count_freq(tokens: list[str]) -> dict[str, int]:
    result = {}

    for token in tokens:
        if token in result:
            result[token]+=1
        else:
            result[token]=1

    return result

def top_n(freq: dict[str, int], n: int = 2) -> list[tuple[str, int]]:
    result = []
    for key in freq:
        value = freq[key]
        element = (key, value)
        result.append(element)
    result = sorted(result, reverse=True, key=lambda n: n[1])[:n]

    return result



