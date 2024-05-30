class RandomizedSet:

    def __init__(self):
        self.random_set = set()
        self.random_cnt = set()

    def insert(self, val: int) -> bool:
        if val in self.random_set:
            return False

        self.random_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.random_set:
            return False

        self.random_set.remove(val)
        return True


    def getRandom(self) -> int:
        random_num_list = list(self.random_set)

        return random.choice(random_num_list)
