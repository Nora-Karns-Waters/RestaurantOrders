

def get_layouts():
    layouts = []

    with open('layouts.txt', 'r') as f:
        layouts = [line.strip() for line in f]

    return layouts

