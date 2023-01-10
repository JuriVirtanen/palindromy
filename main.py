def palindrom(word):
    slowo = word
    slowo = slowo.replace(' ', '')
    back = slowo[::-1]
    return bool(slowo == back)

# funkcja zwraca True/False w zależności od tego czy argument jest swoim palindromem, pomija spacje
print(palindrom("aaaba"))