import math

class WinDoor:
    def __init__(self, x, y):
        self.square = x * y

class Room:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.wd = []

    def total_surface(self):
        return 2 * self.height * (self.length + self.width)

    def add_wd(self, wd):
        self.wd.append(wd)

    def work_surface(self):
        total_square = self.total_surface()
        total_wd_square = sum(wd.square for wd in self.wd)
        return total_square - total_wd_square

    def number_of_rolls(self, r_length, r_width):
        return math.ceil(self.work_surface() / (r_length * r_width))

def main():
    print('Давайте рассчитаем площадь обклеиваемой поверхности и необходимое количество рулонов!')

    length = float(input('Введите длину комнаты (в метрах): '))
    width = float(input('Введите ширину комнаты (в метрах): '))
    height = float(input('Введите высоту комнаты (в метрах): '))
    room = Room(length, width, height)

    while True:
        input_wd = input('Добавить окно или дверь? (да/нет): ').strip().lower()
        if input_wd == 'нет':
            break
        w = float(input('Введите ширину окна/двери (в метрах): '))
        h = float(input('Введите высоту окна/двери (в метрах): '))
        room.add_wd(WinDoor(w, h))

    r_length = float(input('Введите длину рулона обоев (в метрах): '))
    r_width = float(input('Введите ширину рулона обоев (в метрах): '))

    work_surface = room.work_surface()
    rolls_needed = room.number_of_rolls(r_length, r_width)

    print(f"\nПлощадь обклеиваемой поверхности: {work_surface:.2f} м²")
    print(f"Необходимое количество рулонов: {rolls_needed}")

main()