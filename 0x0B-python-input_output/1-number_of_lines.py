def write_file(filename="", text=""):

    """Write a string to a text file (UTF-8) and return the number of characters written."""

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except IOError:
        return 0
