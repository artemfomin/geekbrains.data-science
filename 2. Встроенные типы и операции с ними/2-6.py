from utils.input import request_number, request_alternative


def input_product():
    return {
        "name": input("Please type product name:\n"),
        "price": request_number("Please input product price:\n"),
        "quantity": request_number("Please input product quantity:\n"),
        "units": input("Please type product amount measuring units:\n")
    }


products = []

while True:
    product = input_product()
    products.append((products.__len__() + 1, product))
    response = request_alternative("Do you want to add another product? (Y / N)\n")
    if not response:
        break

print(products)

analytics = {
    "names": [item[1]["name"] for item in products],
    "prices": [item[1]["price"] for item in products],
    "quantities": [item[1]["quantity"] for item in products],
    "units": list(set([item[1]["units"] for item in products])),
}

print(analytics)
