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


    def edit_item(self, file_name):
        if self.__is_file_exist(file_name):
            print('\nРежим изменения списка.')
            is_completed = False
            self.__read_file(file_name)
            n, _, p = input('Параметры товара, которые хотите изменить в формате (Имя - цена): ').split(' ')
            n_change, _, p_change = input('Новые параметры товара в формате (Имя - цена): ').split(' ')
            for i in range(len(self.products)):
                if self.products[i].name == n and self.products[i].price == float(p):
                    self.products[i].name, self.products[i].price = n_change, p_change
                    is_completed = True
            
            if is_completed:
                self.__rewrite_file(file_name)
                print('Товар успешно изменен')
            else:
                print('Указанного товара нет в списке.')
        else:
            print('Файл не найден.')


    def delete_item(self, file_name: str) -> None:
        if self.__is_file_exist(file_name):
            print('\nРежим удаления товара.')
            is_completed = False
            self.__read_file(file_name)
            n, _, p = input('Параметры товара в формате (Имя - цена): ').split(' ')
            for i in range(len(self.products)):
                if self.products[i].name == n and self.products[i].price == float(p):
                    self.products[i] = ''
                    is_completed = True
            
            if is_completed:
                self.__rewrite_file(file_name)
                print('Товар успешно удален.')
            else:
                print('Указанного товара нет в списке.')
        else:
            print('Файл не найден.')


    def __rewrite_file(self, file_name: str) -> None:
        with open(file_name, 'w', encoding='utf-8') as output:
            for prod in self.products:
                if prod:
                    print(f'{prod.name} — {prod.price}', end='\n', file=output)


    def __read_file(self, file_name: str) -> None:
        if self.__is_file_exist(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.strip():
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
    '--Изменить-запись-в-списке': product_list.edit_item,
    '--Удалить-из-списка': product_list.delete_item,
    '--Вычесть-общую-сумму': product_list.calc_sum
    }

    if command not in COMMANDS:
        print('\nНеправильный ввод. Используйте правильные команды.\n')
        for k in COMMANDS:
            print(k)

    COMMANDS[command](file_name)


if __name__ == "__main__":
    main()