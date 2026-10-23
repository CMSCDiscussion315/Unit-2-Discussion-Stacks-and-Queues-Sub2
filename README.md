# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

 Markdown
# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. **Implement stack operations.** (COMPLETED: Implemented using a Python list wrapper with `push`, `pop`, `peek`, and `is_empty` operations running at \(O(1)\) constant time complexity.)
2. **Implement queue operations.** (COMPLETED: Implemented using `collections.deque` with `enqueue`, `dequeue`, `front`, and `is_empty` operations, optimized for \(O(1)\) front-removals.)
3. **Demonstrate LIFO behavior.** (COMPLETED: Built an explicit unrolling loop tracking a text editor's undo log from most recent back to earliest entry.)
4. **Demonstrate FIFO behavior.** (COMPLETED: Built an explicit chronological processing loop tracking coffee shop customers in their strict order of arrival.)
5. **Create and test edge cases.** (COMPLETED: Integrated defensive conditional code blocks to intentionally raise and cleanly catch programmatic `IndexError` exceptions during empty states, alongside a single-item lifecycle test.)
6. **Create a real-world scenario.** (COMPLETED: Contextualized outputs around user UI interaction history and business service queuing systems.)

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

### My Reflection Submission

While completing this assignment, I reinforced my understanding of linear data structures by implementing Stacks (LIFO) and Queues (FIFO) in Python. I learned how underlying structural choices affect performance efficiency; standard Python lists offer optimal \(O(1)\) end-mutations for stacks, while `collections.deque` provides efficient \(O(1)\) front-removals for queues without costly memory-shifting operations.

The primary challenge I encountered was designing clean, uniform bounds-checking. Simply returning a default value like `None` when a structure is empty can mask bugs down the line. I overcame this by explicitly throwing an `IndexError`. This structural choice mirrors professional software libraries and forces calling environments to safely handle edge cases.

In real-world terms, access rules dictate system intent. Stacks optimize experiences requiring immediate state reversal, such as a text editor's undo logs or browser histories, where users prioritize their most recent interaction. Conversely, queues govern systems where fairness and chronological synchronization are mandatory, such as background print spoolers or network packet buffers. Selecting the correct architecture directly prevents lag and ensures intuitive software execution.