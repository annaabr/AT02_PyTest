def count_vowels(str):
    # Приводим строку к нижнему регистру
    s = str.lower()

    # Определяем набор гласных
    vowels = "aeiouy"

    # Счетчик гласных
    count = 0

    # Проходим по каждому символу в строке
    for char in s:
        if char in vowels:
            count += 1

    return count