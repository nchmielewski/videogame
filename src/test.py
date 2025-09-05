# Testing suite

import world
import sys

world.run()

def run_all():
    current_module = sys.modules[__name__]
    for item_name in dir(current_module):
        item = getattr(current_module, item_name)
        if callable(item) and not item_name.startswith('__') and item_name != run_all.__name__:
            try:
                item()
            except TypeError:
                print(f"Skipping '{item_name}' as it requires arguments or is not callable without them.")

def test1():
    print("Hello World!")
    return True

def test2():
    print("Test2")
    print(world.e.load_state())
    return True

def test3():
    print("Test3")
    print(world.e.generate_word())
    return True

def test4():
    print("Test4")
    print(world.e.tick())
    return True

def test5():
    print("Test5")
    print(world.e.word_list)



run_all()
test4()
