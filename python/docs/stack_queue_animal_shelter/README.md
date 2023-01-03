# stack-queue-animal-shelter


## Challenge
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.
Implement the following methods:
enqueue
Arguments: animal
animal can be either a dog or a cat object.
dequeue
Arguments: pref
pref can be either "dog" or "cat"
Return: either a dog or a cat, based on preference.
If pref is not "dog" or "cat" then return null.

## Approach & Efficiency
 Create an animal shelter that has 2 attributes
- enqueue the input cat or dog
-  then dequeue will have a result = None
- create loop that add elements to queue 2
- when queue is complete turn queue 2 into queue 1 and reset queue 2.

Big O

Time O(n): is linear because of the loop used
space O(n): cause it will grow when the commands are taking place

## Contributors
Ricardo, Jason, Aubrey

## Time it took to complete
1 hour and a half

## Whiteboard
![](./whiteboard.png)

## API
The solution code is located in the code_challenges/stack_queue_animal_shelter.py file.

Within the virtual environment, install pytest via pip install pytest.
From the Python folder, run tests via pytest tests/code_challenges/test_stack_queue_animal_shelter.py.
All 5 tests passed.
