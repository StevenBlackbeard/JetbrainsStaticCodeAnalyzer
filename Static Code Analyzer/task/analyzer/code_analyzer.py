def too_long_001(i, line):
    """check line too long"""
    if len(line) > 79:
        return f'Line {i}: S001 Too Long'


def indent_002(i, line):
    """# [S002] Indentation is not a multiple of four;"""
    diff = len(line) - len(line.lstrip())
    if diff % 4 != 0 and line != '\n':
        # print(diff)
        return f'Line {i}: S002 Indentation is not a multiple of four'


def semi_003(i, line):
    """# [S003] Unnecessary semicolon after a statement (note that semicolons are acceptable in comments);"""
    message = f'Line {i}: S003 Unnecessary semicolon'
    line_strip = line.replace(" ", "")
    idx_semi = line_strip.find(";")
    idx_comment = line_strip.find("#")
    idx_eol = line_strip.find("\n")
    if idx_semi != -1:  # semi exists
        if idx_comment != -1:  # comment exists
            if line_strip[idx_comment - 1] == ";":
                return message
        elif idx_eol != -1:  # not final line
            if line_strip[idx_eol - 1] == ";":
                return message
        else:  # is final line
            if line_strip[len(line_strip)] == ";":
                return message


def comments_004(i, line):
    """# [S004] Less than two spaces before inline comments;"""
    idx = line.find("#")
    if idx != -1 and line[0] != "#":
        if line[idx-2:idx] != '  ':
            return f'Line {i}: S004 At least two spaces required before inline comments'


def tdo_005(i, line):
    """# [S005] TDO found (in comments only and case-insensitive);"""
    idx_todo = line.lower().find("todo")
    idx_comment = line.find("#")
    if idx_todo != -1 and idx_comment != -1 and idx_todo > idx_comment:
        return f'Line {i}: S005 TODO found'


def blank_lines_006(count_blank, i):
    """[S006] More than two blank lines preceding a code line (applies to the first non-empty line)"""
    if count_blank > 2:
        return f'Line {i}: S006 More than two blank lines used before this line'


def class_spaces_007(i, line):
    """[S007] too many spaces after class"""
    idx_class = line.lower().find("class")
    idx_colon = line.lower().find(":")
    idx_def = line.lower().find("def")
    if idx_class != -1:
        if not bool(re.match("\s{1}[A-Za-z]", line[idx_class+5:])):
            return f"Line {i}: S007 Too many spaces after 'class'"
    elif idx_def != -1:
        if not bool(re.match("\s{1}[A-Za-z_]", line[idx_def+3:])):
            return f"Line {i}: S007 Too many spaces after 'def'"


def class_camel_008(i, line):
    """[S008] class_name should be written in CamelCase"""
    idx_class = line.lower().find("class")
    idx_colon = line.lower().find(":")
    if idx_class != -1:
        class_name = line[idx_class + 5:idx_colon].lstrip()
        message = f"Line {i}: S008 Class name '{class_name}' should use CamelCase"
        if not bool(re.match(r"[A-Z]", class_name)):
            return message
        elif bool(re.match(r'.*_.*', class_name)):  # or use re.search("_",...) if not at start of string
            return message


def def_snake_009(i, line):
    """[S009] Functions should sue snake case"""
    idx_def = line.lower().find("def")
    idx_colon = line.lower().find("(")
    if idx_def != -1:
        def_name = line[idx_def + 3:idx_colon].lstrip()
        message = f"Line {i}: S009 Function name '{def_name}' should use snake_case"
        if bool(re.search(r'[A-Z]', def_name)):
            return message
        if bool(re.search(r'[a-z][0-9]', def_name)) and not bool(re.match('_', def_name)):
            return message
        elif bool(re.search(r'[A-Z].*[A-Z]', def_name)) and not bool(re.search('_', def_name)):
            return message


def print_func(path, x):
    if x is not None:
        print(path + ": " + x)


def run_search(path):
    file = open(path, "r")
    count_blank = 0
    for i, line in enumerate(file, start=1):
        # print(i, line)
        print_func(path, too_long_001(i, line))
        print_func(path, indent_002(i, line))
        print_func(path, semi_003(i, line))
        print_func(path, comments_004(i, line))
        print_func(path, tdo_005(i, line))
        print_func(path, blank_lines_006(count_blank, i))
        print_func(path, class_spaces_007(i, line))
        print_func(path, class_camel_008(i, line))
        print_func(path, def_snake_009(i, line))
        if line == '\n':
            count_blank += 1
        else:
            count_blank = 0
    file.close()


import sys
import os
import re

args = sys.argv
path = args[1]
# print(path)
# path = "example_temp.txt"
# path = "C:/Users/steve/PycharmProjects/Static Code Analyzer/Static Code Analyzer/task/test/this_stage/test_9.py"
# path = "C:/Users/steve/PycharmProjects/Static Code Analyzer/Static Code Analyzer/task/test"
# path = input() # "example.txt"
if os.path.isdir(path):
    avail_files = os.listdir(path)
    avail_files = [x for x in avail_files if x[-2:] == "py"] # could use x.endswith('.py')
    for x in avail_files:
        run_search(path + "\\" + x)
else:
    run_search(path)




# other 1
# if len(line) > 79:
#     print(error_source, "S001 Too long")
#
# if re.match(r"(?!^( {4})*[^ ])", line):
#     print(error_source, "S002 Indentation is not a multiple of four")
#
# if re.search(r"^([^#])*;(?!\S)", line):
#     print(error_source, "S003 Unnecessary semicolon")
#
# if re.match(r"[^#]*[^ ]( ?#)", line):
#     print(error_source, "S004 At least two spaces before inline comment required")
#
# if re.search(r"(?i)# *todo", line):
#     print(error_source, "S005 TODO found")
#
# if preceding_blank_line_counter > 2:
#     print(error_source, "S006 More than two blank lines used before this line")
# preceding_blank_line_counter = 0
#
# if re.match(r"^([ ]*(?:class|def) ( )+)", line):
#     print(error_source, "S007 Too many spaces after construction_name (def or class)")
#
# if matches := re.match(r"^(?:[ ]*class (?P<name>\w+))", line):
#     if not re.match(r"(?:[A-Z][a-z0-9]+)+", matches["name"]):
#         print(error_source, f'S008 Class name {matches["name"]} should use CamelCase')
#
# if matches := re.match(r"^(?:[ ]*def (?P<name>\w+))", line):
#     if not re.match(r"[a-z_]+", matches["name"]):
#         print(error_source, f'S009 Function name {matches["name"]} should use snake_case')

# other2
#     f = open(f"{z}", "r")
#     linie = f.readlines()
#     for i in range(len(linie)):
#         if len(linie[i]) > 79:
#             bledy.append(f"{z}: Line {i+1}: S001 Too long")
#         if re.search('^\s+\S', linie[i]):
#             if len(re.match('^\s+\S', linie[i]).group(0)[:-1]) % 4 != 0:
#                 bledy.append(f"{z}: Line {i + 1}: S002 Indentation is not a multiple of four")
#         if (";" in linie[i] and "#" not in linie[i]) or ((";" in linie[i] and "#" in linie[i]) and (linie[i].index(';') < linie[i].index('#'))):
#             if not re.search("\'.*?;.*?\'", linie[i]):
#                 bledy.append(f"{z}: Line {i + 1}: S003 Unnecessary semicolon")
#         if re.search(r"^[^#]+(?<=[^ ]) ?#", linie[i]):
#             bledy.append(f"{z}: Line {i + 1}: S004 Less than two spaces before inline comments")
#         if re.search(r'#.*todo', linie[i], re.IGNORECASE):
#             bledy.append(f"{z}: Line {i + 1}: S005 TODO found")
#         if counter > 2:
#             bledy.append(f"{z}: Line {i + 1}: S006 More than two blank lines used before this line")
#         if re.match(r"^\n$", linie[i]):
#             counter += 1
#         else:
#             counter = 0
#         if re.search('class(\s+)', linie[i]):
#             if len(re.search('class(\s+)', linie[i]).group(1)) > 1:
#                 bledy.append(f"{z}: Line {i + 1}: S007 Too many spaces after 'class'")
#         if re.search('def(\s+)', linie[i]):
#             if len(re.search('def(\s+)', linie[i]).group(1)) > 1:
#                 bledy.append(f"{z}: Line {i + 1}: S007 Too many spaces after 'def'")
#         if re.search('class\s+(\w+)', linie[i]):
#             if re.search('class\s+(\w+)', linie[i]).group(1)[0].islower():
#                 bledy.append(f"{z}: Line {i + 1}: S008 Class name 'user' should use CamelCase")
#         if re.search('def\s+(\w+)', linie[i]):
#             if re.search('def\s+(\w+)', linie[i]).group(1)[0].isupper():
#                 bledy.append(f"{z}: Line {i + 1}: S009 Function name 'Print2' should use snake_case")