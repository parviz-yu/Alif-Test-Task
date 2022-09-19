import sys
from dataclasses import dataclass
import os




@dataclass
class Product:
    name: str
    price: float


class ProductList:
    def __init__(self) -> None:
        self.products = []


    def add_item(self, file_name: str) -> None:
        if self.__is_file_exist(file_name):
            with open(file_name, 'a', encoding='utf-8') as curr_file:
                print('Для завершения ввода нажмите "q"')
                curr_file.write('\n')
                for line in sys.stdin:
                    if line.rstrip() == 'q':
                        break
                    *_, price = line.split(' ')
                    if float(price) > 0:
                        print(line, end='', file=curr_file)
                    else:
                        print('Цена не может быть отрицательной!')
                print('\nНаименования добавлены в список.')
        else:
            print('Файл не найден.')


    def calc_sum(self, file_name: str) -> None:
        total = 0
        self.__read_file(file_name)
        for item in self.products:
            total += item.price
        print(total)


    def __read_file(self, file_name: str) -> None:
        if self.__is_file_exist(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    name, _, price = line.split(' ')
                    self.products.append(Product(name, float(price)))
        else:
            print('Файл не найден')


    def __is_file_exist(self, filename: str) -> bool:
        split = filename.split('/')
        if len(split) != 1:
            os.chdir('/'.join(split[:-1]))

        return split[-1] in next(os.walk(os.getcwd()))[-1]



def main() -> None:
    file_name = sys.argv[1]
    command = sys.argv[2]


    product_list = ProductList()
    COMMANDS = {
    '--Добавить-в-список': product_list.add_item,
    '--Изменить-запись-в-списке': '',
    '--Удалить-из-списка': '',
    '--Вычесть-общую-сумму': ''
    }


    if command not in COMMANDS:
        return f"""
        \nНеправильный ввод. Используйте правильные команды.\n
        --Добавить-в-список
        --Изменить-запись-в-списке
        --Удалить-из-списка
        --Вычесть-общую-сумму
        """

    COMMANDS[command](file_name)


    

if __name__ == "__main__":
    main()