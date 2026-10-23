"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # This supports LIFO because appending targets the end of the list,
        # making that element the immediate "top" of the stack for the next retrieval.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # If the stack is empty, it should raise an IndexError to signal an
        # illegal underflow operation, preventing silent None bugs downstream.
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # peek looks at the very last element in the list (index -1),
        # allowing us to inspect the top of the stack without altering it.
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self._items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # This supports FIFO behavior because new elements append to the right (tail),
        # ensuring that older elements remaining at index 0 (head) get processed first.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # If empty, raising an IndexError ensures uniform, predictable exception patterns.
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # front inspects index 0 of the deque, showing the oldest item in line
        # without removing it from the data structure.
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self._items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    # 1. Create a Stack object.
    my_stack = Stack()

    # 2. Add at least 4 values to the stack (Real-world scenario: Text Editor Undo History)
    actions = ["Type 'Hello'", "Apply Bold style", "Insert image.png", "Delete last sentence"]
    print("Pushing historical actions onto our text editor stack:")
    for action in actions:
        print(f" -> [Pushing]: {action}")
        my_stack.push(action)

    # 3. Improve the print statements so they clearly explain what is happening.
    print(f"Current top action available to undo (peek): '{my_stack.peek()}'")

    # 4. Demonstrate LIFO behavior.
    print("\nExecuting user 'Undo' operations (Demonstrating LIFO):")
    while not my_stack.is_empty():
        print(f" <- [Undone/Popped]: {my_stack.pop()}")

    # 5. Show what happens when pop() is used on an empty stack.
    print("\nTesting Exception Handling - Pop from empty stack:")
    try:
        my_stack.pop()
    except IndexError as e:
        print(f"    Caught expected exception: {e}")

    # 6. Show what happens when peek() is used on an empty stack.
    print("Testing Exception Handling - Peek at empty stack:")
    try:
        my_stack.peek()
    except IndexError as e:
        print(f"    Caught expected exception: {e}")

    # 7. Create a stack with only one item, remove it, and verify the stack is empty afterward.
    print("Verifying Single Item Lifecycle:")
    my_stack.push("Isolated Single Action")
    print(f"    Item pushed. Is stack empty? {my_stack.is_empty()}")
    print(f"    Removing item: '{my_stack.pop()}'")
    print(f"    Is stack empty now? {my_stack.is_empty()}")


    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    # 1. Create a Queue object.
    my_queue = Queue()

    # 2. Add at least 4 values to the queue (Real-world scenario: Coffee Shop Customer Line)
    customers = ["Customer Alice", "Customer Bob", "Customer Charlie", "Customer David"]
    print("Enqueuing patrons into the coffee shop line:")
    for customer in customers:
        print(f" -> [Enqueued]: {customer}")
        my_queue.enqueue(customer)

    # 3. Improve the print statements so they clearly explain what is happening.
    print(f"The next patron to be served at the front of the line is: '{my_queue.front()}'")

    # 4. Demonstrate FIFO behavior.
    print("\nServing patrons in order of arrival (Demonstrating FIFO):")
    while not my_queue.is_empty():
        print(f" <- [Served/Dequeued]: {my_queue.dequeue()}")

    # 5. Show what happens when dequeue() is used on an empty queue.
    print("\nTesting Exception Handling - Dequeue from empty queue:")
    try:
        my_queue.dequeue()
    except IndexError as e:
        print(f"    Caught expected exception: {e}")

    # 6. Show what happens when front() is used on an empty queue.
    print("Testing Exception Handling - Checking front of empty queue:")
    try:
        my_queue.front()
    except IndexError as e:
        print(f"    Caught expected exception: {e}")

    # 7. Create a queue with only one item, remove it, and verify the queue is empty afterward.
    print("Verifying Single Item Lifecycle:")
    my_queue.enqueue("Solo Customer")
    print(f"    Customer enqueued. Is queue empty? {my_queue.is_empty()}")
    print(f"    Removing customer: '{my_queue.dequeue()}'")
    print(f"    Is queue empty now? {my_queue.is_empty()}")


if __name__ == "__main__":
    main()
