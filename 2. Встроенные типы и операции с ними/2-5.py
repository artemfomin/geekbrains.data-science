from queue import Queue

import utils.input

rating = Queue(5)

while True:
    number = utils.input.request_number("Please enter number\n")
    if rating.full():
        print(f"{rating.get()} dropped from rating")
    rating.put(number)
    print(list(rating.queue))
