def count_freq(text):
    words = text.lower().split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    for word, count in counts.items():
        print(f"{word}: {count}")


with open("week-1/dict_counter_sample.txt") as f:
    text = f.read()
count_freq(text)
