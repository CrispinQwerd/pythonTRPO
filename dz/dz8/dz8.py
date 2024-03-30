def find_word(text, word):
    # Преобразуем текст и слово к нижнему регистру для учета регистра букв
    text_lower = text.lower()
    word_lower = word.lower()

    # Ищем слово в тексте
    index = text_lower.find(word_lower)
    
    # Проверяем, найдено ли слово
    if index != -1:
        print(f"Слово '{word}' найдено в тексте на позиции {index+1}.")
    else:
        print(f"Слово '{word}' не найдено в тексте.")


text = input("Введите текст: ")


word = input("Введите слово для поиска: ")


find_word(text, word)
