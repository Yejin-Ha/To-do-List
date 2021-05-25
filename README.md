# :memo: To-do list Program 
**&nbsp; &nbsp; Team : 박철희, 이재선, 장수정, 하예진**

<br>

## :white_check_mark: Index
**1. 주제선정 이유**

&nbsp; &nbsp; : Step13 수업까지 들으며 일상생활속에서 자주 쓰이는 To-do list를 구현하는 프로그램을 만들 수 있을 것 같다는 생각이 들어

&nbsp; &nbsp; &nbsp; 이 주제를 선정하게 되었습니다.
 
<br> 
 
**2. 기능구현**

- 등록된 유저인지 체크
 
- 유저등록
 
- 할일등록(내용, 날짜)
 
- 해당 유저의 To-do list 출력
 






**3. Code**


```python
class Planner:    
    def __init__(self, name):
        self.name = name;
        
        
    # 등록된 유저인지 체크
    def checkUser(self):
        with open('./DataBase/users.txt', 'r', encoding='utf-8') as f:
            self.user_list = f.read().splitlines()

        if self.name in self.user_list:
            print('반갑습니다:) 회원정보가 확인되었습니다.') 
            print(' ' * 20)
        else:
            print('회원정보가 없습니다. 유저를 등록해주세요.')            
            def getUser(self):
                input_name = input('이름을 입력하세요 : ')
                with open('./DataBase/users.txt','a', encoding='utf-8') as f: 
                    f.write('\n'+input_name)
            getUser(self)

    # 유저 등록
    def getUser(self):
        input_name = input('이름을 입력하세요 : ')
        with open('./DataBase/users.txt','a', encoding='utf-8') as f: 
            f.write('\n'+input_name)


    # 할일등록(내용, 날짜)
    def todoList(self, todo, date):
        self.dates = []
        with open(f'./DataBase/Users/{self.name}.txt', 'r', encoding='utf-8') as f:
            self.todo_list = f.readlines()

        for idx in range(len(self.todo_list)):
            if self.todo_list[idx].startswith('#'):
                self.dates.append(idx)
                if self.todo_list[idx].startswith(f'# {date}'):
                    self.today = idx
                        
        self.next = self.dates.index(self.today)+1
        today_list = self.todo_list[self.today:self.next]
        today_list.insert(1, f'- {todo}\n')
        add_list = self.todo_list[:self.today]+ today_list + self.todo_list[self.next:]
        with open(f'./DataBase/Users/{self.name}.txt', 'w', encoding='utf-8') as f:
            f.writelines(add_list) 
 ```



**4. Pylint**


**5. 최총 Code 실행 결과**
