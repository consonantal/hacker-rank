import re
# float_regex = re.compile(r'^[0-9]+\.[0.9]')
float_regex = re.compile(r'^[+-]?\d*?\.{1}\d+$')
for _ in range(int(raw_input())):
    number = raw_input()
    print(bool(re.match(float_regex, number)))

