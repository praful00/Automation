try:
    file = open('E:\pro.txt')
    print(file.readline())
    file.close()

except Exception as e:
    print(e)


try:
    file = open('E:\pro.txt')
    print(file.readline())
    file.close()
except:
    print("file not found")

finally:
    print("clean file")