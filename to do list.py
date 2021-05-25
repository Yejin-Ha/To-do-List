class Planner:
    """
    투두리스트를 작성하는 클래스입니다.
    """
    def __init__(self, name):
        self.name = name
        self.next = ""
        self.today = ""
        self.my_list = []
        self.dates = []
        self.user_list = []
    def check_user(self):
        """
        존재하는 유저인지 확인입니다.
        """
        with open('./DataBase/users.txt', 'r', encoding='utf-8') as file:
            self.user_list = file.read().splitlines()
        if self.name in self.user_list:
            print('반갑습니다:) 회원정보가 확인되었습니다.')
            print(' ' * 20)
        else:
            print('회원정보가 없습니다. 유저를 등록해주세요.')
            def get_user(_self):
                input_name = input('이름을 입력하세요 : ')
                with open('./DataBase/users.txt','a', encoding='utf-8') as file:
                    file.write('\n'+input_name)
            get_user(self)
    def get_user(self):
        """
        유저를 등록합니다.
        """
        input_name = input('이름을 입력하세요 : ')
        with open('./DataBase/users.txt','a', encoding='utf-8') as file:
            file.write('\n'+input_name)
    def todo_list(self, todo, date):
        """
        할 일과 날짜를 입력받아서 추가합니다.
        """
        with open(f'./DataBase/Users/{self.name}.txt', 'r', encoding='utf-8') as file:
            self.my_list = file.readlines()
        for idx in range(len(self.my_list)):
            if self.my_list[idx].startswith('#'):
                self.dates.append(idx)
                if self.my_list[idx].startswith(f'# {date}'):
                    self.today = idx
        self.next = self.dates.index(self.today)+1
        today_list = self.my_list[self.today:self.next]
        today_list.insert(1, f'- {todo}\n')
        add_list = self.my_list[:self.today]+ today_list + self.my_list[self.next:]
        with open(f'./DataBase/Users/{self.name}.txt', 'w', encoding='utf-8') as file:
            file.writelines(add_list)