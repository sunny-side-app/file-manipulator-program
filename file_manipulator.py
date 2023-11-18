import sys
import shutil

class Reverse():
    def __init__(self, params: list):
        print('reverse')
        self.params: list = params
        self.input_path: str = self.params[2]
        self.output_path: str = self.params[3]

    def exec(self):
        read_data: str = ''
        reversed_data: str = ''

        # open(): https://docs.python.org/ja/3/tutorial/inputoutput.html
        with open(self.input_path, mode='r', encoding='utf-8') as f:
            read_data = f.read()
        
        reversed_data = read_data[::-1]

        with open(self.output_path, mode='w', encoding='utf-8') as f:
            f.write(reversed_data)


class Copy():
    def __init__(self, params: list):
        print('copy')
        self.params: list = params
        self.input_path: str = self.params[2]
        self.output_path: str = self.params[3]

    def exec(self):
        # shutil.copy():https://docs.python.org/ja/3/library/shutil.html#shutil.copy
        copied_data = shutil.copy(self.input_path, self.output_path)

class Duplicate():
    def __init__(self, params: list) -> None:
        self.params: list = params
        self.input_path: str = self.params[2]
        # 文字列の演算を行うためintへ型変換
        self.number_of_duplicates: int = int(self.params[3])
        print('duplicate')

    def exec(self):
        read_data: str = ''
        duplicated_data: str = ''

        with open(self.input_path, mode='r', encoding='utf-8') as f:
            read_data = f.read()

        duplicated_data = read_data*self.number_of_duplicates

        with open(self.input_path, mode='w', encoding='utf-8') as f:
            f.write(duplicated_data)
        

class Replace():
    def __init__(self, params: list):
        self.params: list = params
        self.input_path: str = self.params[2]
        self.old_str: str = self.params[3]
        self.new_str: str = self.params[4]
        print('replace')
    
    def exec(self):
        with open(self.input_path, mode='r', encoding='utf-8') as f:
            read_data = f.read()

        replaced_data = read_data.replace(self.old_str, self.new_str)
        # 'w'でopenすると内容は削除されるためopen
        with open(self.input_path, mode='w', encoding='utf-8') as f:
            f.write(replaced_data)
        

class FileManipulator():
    def __init__(self):
        print("Hello World!")
        # 変数の型の型付け：https://future-architect.github.io/articles/20201223/
        self.manipulator_map: dict = {
            'reverse': Reverse,
            'copy': Copy,
            'duplicate-contents': Duplicate,
            'replace-string': Replace
        }
        self.manipulator_length_map: dict = {
            "reverse": 4,
            'copy': 4,
            'duplicate-contents': 4,
            'replace-string': 5
        }
    
    def is_valid(self) -> bool:
        if not (sys.argv[1] in self.manipulator_map):
            print('\nそのコマンドは存在しません')
            return False

        if not (len(sys.argv) == self.manipulator_length_map[sys.argv[1]]):
            print('\nコマンドの引数に過不足があります')
            return False
        
        return True
    
    def validate_input(self):
        manipulator_obj: object
        # コマンドの存在、引数チェック
        if self.is_valid():
            # 各manipulatorのクラスにパラメータを渡す
            manipulator_obj = self.manipulator_map[sys.argv[1]](sys.argv)
            # 各manipulatorを実行
            manipulator_obj.exec()

def main():
    file_manipulator_program = FileManipulator()
    file_manipulator_program.validate_input()

if __name__ == '__main__':
    main()



