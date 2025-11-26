
def read_words(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().lower()
    
    return text.split()


def hash_func(word, size):
    h = 0
    for ch in word:
        h = (h+ord(ch)) % size
    return h


class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, word):
        index = hash_func(word, self.size)
        if word not in self.table[index]:
            self.table[index].append(word)

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            for i, lst in enumerate(self.table):
                f.write(f"{i}: {lst}\n")



def main():
    input_file = "input.txt"     
    out = "result14.txt"

    words = read_words(input_file)
    table_size = 20

    
    ht = HashTableChaining(table_size)
    for w in words:
        ht.insert(w)
    ht.save(out)


if __name__ == "__main__":
    main()
