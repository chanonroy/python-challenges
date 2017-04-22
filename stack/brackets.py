parString = '[{}}'


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])


def bracesChecker(string):

    a = Stack()
    b = Stack()
    c = Stack()

    balanced = True
    index = 0

    while index < len(string) and balanced:
        symbol = string[index]

        if symbol == "{" or "}":
            if symbol == "{":
                a.push(symbol)
            else:
                if a.is_empty():
                    balanced = False
                else:
                    a.pop()
        elif symbol == "(" or ")":
            if symbol == "(":
                b.push(symbol)
            else:
                if b.is_empty():
                    balanced = False
                else:
                    b.pop()
        elif symbol == "[" or "]":
            if symbol == "[":
                c.push(symbol)
            else:
                if c.is_empty():
                    balanced = False
                else:
                    c.pop()

        index += 1

    if balanced and a.is_empty() and b.is_empty() and c.is_empty():
        return True
    else:
        return False


result = bracesChecker(parString)
print(result)
