import sys
from dataclasses import dataclass



@dataclass
class Product:
    name: str
    price: float


class ProductList:
    def __init__(self) -> None:
        self.products = []





def main() -> None:
    file_name = sys.argv[1]
    command = sys.argv[2]


    product_list = ProductList()
    COMMANDS = {
    '--Добавить-в-список': '',
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



if __name__ == "__main__":
    main()