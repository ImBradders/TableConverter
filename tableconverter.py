import os

class format_table:
    def __init__(self):
        self.internal = []
    def add_row(self, list):
        self.internal.append(list)
    def get_col_count(self):
        return len(self.internal[0])
    def get_row(self, id):
        return self.internal[id]
    def get_row_count(self):
        return len(self.internal)

def convert_file(file):
    table = format_table()
    # extract data from file
    with open(file, "r") as source:
        for line in source:
            split_line = line.split(",")
            for i in range(len(split_line)):
                split_line[i] = split_line[i].strip(" \n\t" )
            table.add_row(split_line)

    # create output file
    new_file = file[0:len(file)-4] + ".txt"
    with open(new_file, "w") as dest:
        # output header
        dest.write("\\begin{tabular}{")
        for col in range(table.get_col_count()):
            dest.write("|c")
        dest.write("|}\n")
        # output each row - indent all of these in output for readability
        for row in range(table.get_row_count()):
            dest.write("\t\hline\n")
            output = ""
            for item in table.get_row(row):
                output += item + " & "
            output = output[0: len(output)-3]
            dest.write("\t" + output + " \\\\" + "\n")
        dest.write("\t\hline\n")
        # output table closure
        dest.write("\end{tabular}")
    full_path = os.path.join(os.getcwd(), new_file)
    print(f"File converted. Find at {full_path}")

def check_access(filepath):
    try:
        file = open(filepath, "r")
        file.close()
    except:
        return True
    return False

def check_type(filepath):
    path_end = filepath[len(filepath) - 4:len(filepath)]
    return path_end != ".csv"

def check_length(filepath):
    return len(filepath) < 5

def get_filepath():
    filepath = None
    while filepath == None:
        filepath = input("Enter the path of the file to convert: ")
        if check_length(filepath):
            print("Filename not long enough. Please check entered path and try again.\n")
            filepath = None
        elif check_type(filepath):
            print("File must be csv. Please check entered path and try again.\n")
            filepath = None
        elif check_access(filepath):
            print("Unable to open file. Please check entered path and try again.\n")
            filepath = None

    return filepath

def convert_table():
    file_to_convert = get_filepath()
    convert_file(file_to_convert)

if __name__ == "__main__":
    convert_table()