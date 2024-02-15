if __name__ == '__main__':
    N = int(input())
list = []
command = ""
while N:
    command=input("")
    if command[0:3] == 'ins':
        i=int(command[command.find(" "):command.rfind(" ")])
        e=int(command[command.rfind(" ")::])
        list.insert(i,e)
        N-=1
    elif command[0:3]=='rem':
        e=int(command[command.rfind(" ")::])
        list.remove(e)
        N-=1
    elif command[0:3]=='app':
        e=int(command[command.rfind(" ")::])
        list.append(e)
        N-=1
    elif command[0:3]=='sor':
        list.sort()
        N-=1
    elif command[0:3]=='rev':
        list.reverse()
        N-=1
    elif command[0:3]=='pop':
        list.pop()
        N-=1
    else:
        print(list)
        N-=1
