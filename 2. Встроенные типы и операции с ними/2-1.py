items = [ "Some item", 123, 8.5, 'item', True, 1j, range(3), { "item1", "item2" },
          ("whatever", "smth else"), b"byte stuff",  bytearray(2), memoryview(bytes(3))]

for list_item in items:
    print(f"{items.index((list_item)) + 1}. Data type : {type(list_item)}.")
    print(f"Data type simplified: {type(list_item).__name__}")
    print(f"Content: {list_item}.")
    print()