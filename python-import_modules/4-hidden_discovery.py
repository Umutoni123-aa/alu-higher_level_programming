#!/usr/bin/python3
if __name__ == "__main__":
    hidden_module = __import__('hidden_4')
    all_names = dir(hidden_module)
    public_names = [name for name in all_names if not name.startswith('__')]
    public_names.sort()
    for name in public_names:
        print(name)
