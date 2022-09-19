import sys
from dataclasses import dataclass



@dataclass
class Product:
    name: str
    price: float


class ProductList:
    def __init__(self) -> None:
        self.products = []

    def add_item(self, file_name: str) -> None:
        print('Для завершения ввода нажмите "q"')
        with open(file_name, 'a', encoding='utf-8') as curr_file:
            curr_file.write('\n')
            for line in sys.stdin:
                if line.rstrip() == 'q':
                    break
                print(line, end='', file=curr_file)
            print('\nНаименования добавлены в список')



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