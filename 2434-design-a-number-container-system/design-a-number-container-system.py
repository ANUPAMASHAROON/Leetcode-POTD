class NumberContainers:

    def __init__(self):
        self.number_to_indices = collections.defaultdict(SortedSet)
        
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:
        
        if index in self.index_to_number:
            previous_number = self.index_to_number[index]
            self.number_to_indices[previous_number].remove(index)
            if not self.number_to_indices[previous_number]:
                del self.number_to_indices[previous_number]

        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
       
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        return -1


