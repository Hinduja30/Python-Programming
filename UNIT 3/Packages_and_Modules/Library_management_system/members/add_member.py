from ..utilities.formatter import format_name

def add_member(first_name, last_name):
    full_name = format_name(first_name, last_name)
    print(f"Member '{full_name}'added to the library.")
    