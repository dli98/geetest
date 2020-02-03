# Owner: <dli>
# @Time    : 2020/2/3 17:27
# @Software: PyCharm
original = "t_dict_unix.pkl"
destination = "t_dict.pkl"

outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))
