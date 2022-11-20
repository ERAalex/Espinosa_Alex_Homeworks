

###################  TASK 1  ###################

class Stack():
    def __init__(self) -> None:
        self.list_done = []

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, element) -> None:
        self.list_done.append(element)


    def pop(self):
        try:
            return self.list_done.pop()
        except IndexError as error:
            return -1, error

    def peek(self):
        try:
            return self.list_done[-1]
        except IndexError as error:
            return -1, error

    def size(self) -> int:
        return len(self.list_done)




###################  TASK 2  ###################


list_1 = ['(','(','(','(','[','{','}',']',')',')',')',')']
list_2 = ['{','{','[','(',')',']','}','}']
list_3 = ['[','}','{','}',']']

list_boss = ['[', '(', '[', ']', ')', '(', '(', '(', '[', '[', '[', ']', ']', ']', ')', ')', ')', ']', '{', '(', ')', '}']


stack = Stack()

def check_bracket_sequence(list_gives, stack):
    dicc = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for item in list_gives:
        if item in dicc:
            stack.push(item)
        elif stack.peek()[0] == -1:
            return 'Несбалансированно'
        elif item == dicc.get(stack.peek()):
            stack.pop()
        elif item != dicc.get(stack.peek()):
            return 'Несбалансированно'

    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


print(check_bracket_sequence(list_boss, stack))