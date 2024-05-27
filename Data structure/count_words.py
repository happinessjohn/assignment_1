def count_words(text):
    text = text.lower()
    words = text.split()
    word_counts = {}
    for word in words:
        cleaned_word = word.strip(".,!?")
        if cleaned_word:
            word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    return word_counts

user_text = input("Enter a sentence or paragraph: ")
result = count_words(user_text)
for word, count in result.items():
    print(f"{word}: {count}")