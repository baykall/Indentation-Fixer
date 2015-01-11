indentation_string = "    "

content = []
with open("code.txt") as f:
    content = f.readlines()

new_content = []
for line in content:
    new_content.append(line.strip())

indent_level = 0
no_bracket_for_indentation = False
fo = open("new code.txt", 'w')
for line in new_content:
    if line.startswith('}'):
        indent_level -= 1               
    indent_str = ""
    for i in range(indent_level):
        indent_str += indentation_string
    fo.write(indent_str + line  + "\n")
    if line.endswith('{'):
        indent_level += 1 
    if no_bracket_for_indentation:
        indent_level -= 1  
        no_bracket_for_indentation = False          
    if line.endswith(')') or line == "else":
        indent_level += 1  
        no_bracket_for_indentation = True  
               

fo.close()
