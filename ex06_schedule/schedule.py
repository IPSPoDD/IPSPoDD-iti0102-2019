"""Create schedule from the given file."""
import re


def get_table_sizes(again_dict, key_list, value_list):
    """Get the maximum sizes for table."""
    if len(again_dict) == 0:
        return "------------------\n|  time | items  |\n------------------\n| No items found |\n------------------"
    else:
        table = ""
        t = []
        for v in value_list:
            k = int(len(str(v).replace("'", "").replace("]", "").replace("[", "")))
            t.append(k)
        g = max(t)
        line = "-" * (15 + int(g)) + "\n"
        maximum = 15 + int(g)
        header = f"""|{"time":>{1}} | {"item":<{1}}|\n"""
        table += line
        table += header
        table += line
        for k, v in zip(key_list, value_list):
            if len(k) == 7:
                n = "| " + k + " | "
                # table += n + str(v) + " " * (int(maximum) - len(v) - 15) + "  |\n"
                table += f"""|{"time":>{k + 1}} | {"item":<{v + 1}}|\n"""
            if len(k) == 8:
                n = "|" + k + " | "
                # table += n + str(v) + " " * (int(maximum) - len(v) - 15) + "  |\n"
                table += f"""|{"time":>{k + 1}} | {"item":<{v + 1}}|\n"""
            if len(v) == 0:
                n = "|" + k + " | "
                # table += n + " " * 7 + " |\n"
                table += f"""|{"time":>{k + 1}} | {"item":<{v + 1}}|\n"""
        table += line
        return table.replace("'", "").replace("]", "").replace("[", "")


def get_formated_time(time):
    """Get formated time."""
    hos = int(time)
    hours = hos // 60
    minutes = hos % 60
    if 0 == hours:
        if 0 <= minutes <= 9:
            f2 = str(0) + str(minutes)
            return f"12:{f2} AM"
        if 10 <= minutes <= 59:
            return f"12:{minutes} AM"
    if 1 <= hours < 12:
        if 0 <= minutes <= 9:
            f2 = str(0) + str(minutes)
            return f"{hours}:{f2} AM"
        if 10 <= minutes <= 59:
            return f"{hours}:{minutes} AM"
    if 12 <= hours < 24:
        if 0 <= minutes <= 9:
            f2 = str(0) + str(minutes)
            return f"{hours - 12}:{f2} PM"
        if 10 <= minutes <= 59:
            return f"{hours - 12}:{minutes} PM"


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    with open(input_filename) as file:
        c = file.read()
        b = create_schedule_string(c)
    with open(output_filename, "w", newline="") as file:
        file.write(b)
    return None


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    time_unformated = []
    dictionary = {}
    key_list = []
    value_list = []
    for match in re.finditer(r"([2][0-3]|[0-1][0-9]|[ ][\d]|\s[\d])[-_.,;:a-zA-Z]([0-5][0-9]|\d) +(\w+)", input_string):
        hours = int(match.group(1))
        minutes = int(match.group(2))
        item = match.group(3).lower()
        time = hours * 60 + minutes
        time_unformated.append(time)
        key = time
        if key in dictionary:
            if item not in dictionary[key]:
                dictionary[key].append(item)
        else:
            dictionary[key] = [item]
    sorted_items = dict(sorted(dictionary.items()))
    for value in sorted_items.values():
        value_list.append(value)
    for key in sorted_items.keys():
        time = get_formated_time(key)
        key_list.append(time)
    again_dict = dict(zip(key_list, value_list))
    n = []
    for i in value_list:
        if len(i) == 1:
            n.extend(i)
        if len(i) > 1:
            n.append(", ".join(i))
    return get_table_sizes(again_dict, key_list, n)


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
