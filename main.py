import os.path


def main():
    # Get input file
    input_file = ""
    while not (os.path.isfile(input_file) and input_file[-4:] == ".csv"):
        input_file = input("Please enter the name of a CSV file to parse (include .csv extension): ")
    # Get filter type
    data_type = ""
    while not (data_type == "first_name" or data_type == "last_name" or data_type == "birth_year"):
        data_type = input("Please enter a filter type (first_name, last_name, birth_year): ")

    # Generate key filter
    # Lambda takes record line, returns key
    if data_type == "first_name":
        key_filter = lambda record: record.split(',')[0]
    elif data_type == "last_name":
        key_filter = lambda record: record.split(',')[1]
    else:
        key_filter = lambda record: record.split(',')[2][:4]

    # Generate hash for records
    my_hash: dict[str, list[str]] = {}

    # Sort data
    file = open(input_file, 'r')
    for record_line in file.readlines()[1:]:
        my_key = key_filter(record_line)

        if my_key not in my_hash:
            my_hash[my_key] = []

        my_hash[my_key].append(record_line[:-1])

    file.close()

    # Return data while user asks
    input_str = ""
    while not (input_str == "q"):
        input_str = input("Please enter an item to search for, or 'q' to quit: ")

        if input_str in my_hash:
            for record in my_hash[input_str]:
                print(record)
        else:
            print(f"No records matching '{input_str}'.")


if __name__ == '__main__':
    main()
