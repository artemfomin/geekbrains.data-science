from queue import Queue

import utils.input

rating = Queue(5)

while True:
    number = utils.input.request_number("Please enter number\n")
    if list(rating.queue).__len__() > 0 and number > list(rating.queue).pop():
        print("Sequence should not decrease. Please try again.")
        continue
    if rating.full():
        print(f"{rating.get()} dropped from rating")
    rating.put(number)
    print(list(rating.queue))
