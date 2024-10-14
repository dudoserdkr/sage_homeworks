import time
from math import factorial

class LCD:
    def __init__(self, partition: str, partitioned_number: int) -> None:
        self.part = list(map(int, partition.strip().split()))
        self.lcd = self.calc_lcd()
        self.pn = partitioned_number
        self.perm_count = self.permutations_count()

    @staticmethod
    def gcd(a, b) -> int:
        while b:
            a, b = b, a % b
        return a

    def calc_lcd(self) -> int:
        lcd = self.part[0]
        for i in range(1, len(self.part)):
            number = self.part[i]
            lcd = lcd * number // self.gcd(lcd, number)
        return lcd

    @staticmethod
    def part_to_dict(part) -> dict:
        d = {}
        for item in part:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        return d

    def permutations_count(self) -> int:
        perm_dict = self.part_to_dict(self.part)
        a = factorial(self.pn)
        for key, value in perm_dict.items():
            a //= (key ** value) * factorial(value)
        return a


if __name__ == '__main__':
    start_time = time.time()

    with open("integers_partitions_100.txt", "r") as file:
        i = 0
        S100 = {}
        for partition in file:
            i += 1
            lcd = LCD(partition, 100)
            S100[lcd.lcd] = S100.get(lcd.lcd, 0) + lcd.perm_count
            if i == 100000:
                break

    S100_sorted = dict(sorted(S100.items()))

    with open('output02_S100.txt', 'w') as f:
        for key, value in S100_sorted.items():
            f.write(f'Order: {key}; Count: {value}\n')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")