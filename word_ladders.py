class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def get_neighbors(word, cache):
    neighbors = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    word_as_list = list(word)
    for i in range(len(word_as_list)):
        for letter in letters:
            temp = list(word_as_list)
            temp[i] = letter
            potential_match = "".join(temp)
            if potential_match != word and potential_match in cache[len(word)]:
                neighbors.append(potential_match)
    return neighbors

# Standard BFS algorithm to find the shortest path
def find_ladders(start_word, end_word, cache):
    visited = set()

    queue = Queue()
    queue.enqueue([start_word])

    while queue.size() > 0:
        curr_path = queue.dequeue()
        curr = curr_path[-1]

        if curr not in visited:
            if curr == end_word: return curr_path
            visited.add(curr)

            for neighbor in get_neighbors(curr, cache):
                new_path = curr_path[:]
                new_path.append(neighbor)
                queue.enqueue(new_path)

    return None

# Reads in the file and stores each word in a set. 
# A dictionary holds each set where key=length of chars, value=set of words
def read_file(file_name):
    file = open(file_name, 'r')
    words = file.read().split('\n')
    file.close()
    
    words_cache = {}
    for word in words:
        if len(word) not in words_cache:
            words_cache[len(word)] = set()

        words_cache[len(word)].add(word.lower())
    return words_cache

def main():
    word_cache = read_file('words.txt')
    start = 'sail'
    end = 'boat'
    path = find_ladders(start, end, word_cache)
    print(path)


if __name__ == '__main__':
    main()



