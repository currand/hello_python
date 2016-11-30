import textwrap

lines = [
    {'title': "Title",
     'level': "Important",
     'description': "This is a long line that I'd like to wrap"}
]

for line in lines:
    wrapped_lines = []
    for key, length in [('title', 16), ('description', 24), ('level', 16)]:
        if len(line[key]) > length:
            wrapped_lines = textwrap.wrap(line[key], length)
            line[key] = wrapped_lines


#
# This will likely go into show_todos
#
output = {}

for index, line in enumerate(lines):
    output[0] = str(index + 1).ljust(8)
    from_left = 0
    for key, length in [('title', 16), ('description', 24), ('level', 16)]:
        from_left += length
        x = 0
        if isinstance(line[key], list):
            for long_line in line[key]:
                try:
                    output[x] += long_line.ljust(from_left)
                except KeyError:
                    output[x] = long_line.ljust(length)
                x += 1
        else:
            output[x] += line[key].ljust(length)
            x += 1

#print output

items = ['a', 'b', 'c']
items2 = ['d']
max_len = max(range(0,len(items)))
print max_len

print "making a change"
print "and another change"