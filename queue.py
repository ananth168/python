queue = []


def enqueue():
    print("enter a element to the ")
    element = input()
    queue.append(element)
    print(queue)


def dequeue():
    if len(queue) == 0:
        print('queue is empty')
    else:
        ii = queue.pop(0)
        print("popped element is : ", ii)
        print(queue)


while True:
    print('choose any function  1.push  2.pop  ')
    choice = int(input())
    if choice == 1:
        enqueue()
    if choice == 2:
        dequeue()
    if choice == 3:
        print('okay bye ')
        break

