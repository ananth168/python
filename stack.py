stack = []


def push():
    element = input("enter the element :")
    stack.append(element)
    print(stack)


def pop_stk():
    if len(stack) == 0:
        print('stack is empty')
    else:
        popped_element = stack.pop()
        print('element popped', popped_element)
        print(stack)


def top():
    print("top of the stack is : ")
    top_Ele = stack[-1]
    return top_Ele


while True:
    print('choose any function  1.push  2.pop  3.top_element 4.quit')
    choice = int(input())
    if choice == 1:
        push()
    if choice == 2:
        pop_stk()
    if choice == 3:
        top()
    if choice == 4:
        print('okay bye!')
        break
