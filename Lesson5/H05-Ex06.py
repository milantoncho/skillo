#TODO: 6. Implement a basic queue structure ( as a global var ) by defining two functions `enqueue` and `dequeue`.

queue = []

def enqueue(some_element):
    queue.append(some_element)

def dequeue():
    queue.pop(0)

def control():
    next_action = 1
    while next_action != 0:
        next_action = int(input('\n'
                '1 - Add\n'
                '2 - Remove\n'
                '3 - View Content\n'
                '4 - View Length\n'
                '0 - Exit\n'
                'Choose what to do with the object "queue": '))
        if next_action == 1:
            enqueue(input("Add: "))
        elif next_action == 2:
            dequeue()
        elif next_action == 3:
            print("The current queue content is: ", queue)
        elif next_action == 4:
            print("The current queue length is: ", len(queue))
        elif next_action == 0:
            print("Exiting...")

print("start")
control()