

with open('E:\pro.txt','r') as reader:
    content=reader.readlines()
    reversed(content)

with open('E:\pro.txt','w') as writer:
    for line in reversed(content):
        writer.write(line)





