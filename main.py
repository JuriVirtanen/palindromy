def palindrom(word):
    slowo = word
    slowo = slowo.replace(' ', '')
    back = slowo[::-1]
    if back == slowo:
        return True
    return False

# funkcja zwraca True/False w zależności od tego czy argument jest swoim palindromem, pomija spacje
print(palindrom("kajak"))