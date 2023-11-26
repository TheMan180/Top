import os
from PIL import Image
from PIL import ImageFilter

class BoxBlur:
    def change_img(self, original_img):
        blur_img = original_img.filter(ImageFilter.BLUR)
        blur_img.show()
        return original_img

class Details:
    def change_img(self, original_img):
        for i in range(3):
            details_img = original_img.filter(ImageFilter.MinFilter(3))
            details_img.show()
            return original_img

class Counter:
    def change_img(self, original_img):
        edges_image = original_img.filter(ImageFilter.FIND_EDGES)
        edges_image.show()
        return original_img
class GrayScale:
    def change_img(self, original_img):
        grayscale_image = original_img.convert('L')
        grayscale_image.show()
        return original_img

def main():
    filters_list = {
        1: {
            "name": "BoxBlur",
            "description": "Делает каринку мутной, убрает пиксели на изображении.",
            "func": BoxBlur,
        },
        2: {
            "name": "Details",
            "decription": "Подчёркивает детали и делает фон размытым.",
            "func": Details,
        },
        3: {
            "name": "Counter",
            "decription": "Фильтр позволяет получить контурное изображение объекта на картинке(эрозия).",
            "func": Counter,
        },
        4: {
            "name": "GrayScale",
            "decription": "Превращает фото из цветного в серый цвет.",
            "func": GrayScale,
        },
        0: {
            "name": "Exit.",
            "func":  lambda: exit(print("Спасибо, что попользовались программой!До свидания!"))
        },
    }
    print("Приветствую тебя дорогой пользователь в моём фоторедакторе.\n"
          "Бери чаёк и развлекайся с фильтрами."),
    print("Выберите фильтр (или 0 для выхода).")
    is_finished: bool = False
    while not is_finished:
        path = input("Введите путь к файлу:")
        while not os.path.exists(path):
            path = input("Неверный путь. Введите путь к файлу:")

        original_img = Image.open(path)
        print("Менюшка Фотофильтров:")
        for key, items in filters_list.items():
            print(f"{key}. {items['name']}")

        choice = input("Выберите фильтр и сразу примените его:")
        while not choice.isdigit() or int(choice) not in filters_list:
            choice = input("Неверный ввод.Возвращение к меню.")

        filter = filters_list[int(choice)]['func']()
        new_img = filter.change_img(original_img)

        new_path = input("Куда сохранить?:")
        while not os.path.exists(path):
            new_path = input("Неверный ввод. Введите путь к файлу:")

        new_img.save(new_path)
        choice = input("Продолжить? (да/нет): ").lower()
        while choice != "да" and choice != "нет":
            choice = input("Некорректный ввод. Продолжить? (да/нет): ")

        if choice != "да":
            new_img.save(new_path)


        is_finished = choice == "нет"

    print("Спасибо, что попользовались программой!\n"
          "До свидания!")


if __name__ == "__main__":
    main()
