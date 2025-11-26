def read_words(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().lower()
    return text.split()


def hash_func(word, size):
    h = 0
    for ch in word:
        h = (h+ord(ch)) % size
    return h


class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, word):
        index = hash_func(word, self.size)
        start = index

        while self.table[index] is not None:
            if self.table[index] == word:
                return  
            index = (index + 1) % self.size
            if index == start:
                raise Exception("Хеш-таблица переполнена")

        self.table[index] = word

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            for i, v in enumerate(self.table):
                f.write(f"{i}: {v}\n")



def main():
    input_file = "input.txt"     
    out = "result13.txt"

    words = read_words(input_file)
    table_size = 20 

    ht = HashTableOpenAddressing(table_size)
    for w in words:
        ht.insert(w)
    ht.save(out)


if __name__ == "__main__":
    main()
