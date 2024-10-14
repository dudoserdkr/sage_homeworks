import time
from math import factorial


class FileWriter:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def write(self, data: dict) -> None:
        i = 0
        with open(self.file_name, 'w') as f:
            for key, value in data.items():
                i += 1
                f.write(f'Order: {key}: Count: {value}\n')


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
        S100 = {}
        for partition in file:
            lcd = LCD(partition, 100)
            S100[lcd.lcd] = S100.get(lcd.lcd, 0) + lcd.perm_count

    S100_sorted = dict(sorted(S100.items()))

    A100_sorted = {}
    for order, count in S100_sorted.items():
        if order % 2 == 0:
            A100_sorted[order] = count // 2

    file_writer = FileWriter("output02_S100.txt")
    file_writer.write(S100_sorted)

    file_writer.file_name = "output02_A100.txt"
    file_writer.write(A100_sorted)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")