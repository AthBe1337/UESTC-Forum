import sys
import informations
import initializer
import autoFill

if __name__ == '__main__':

    args = sys.argv
    if args.__len__() < 2:
        print(informations.argErrorInfo)
        sys.exit(1)
        pass

    match args[1].lower():

        case '-init':
            print("开始初始化")
            if initializer.init():
                print("初始化完成")
                sys.exit(0)
            else:
                print("初始化失败")
                sys.exit(1)

        case '-help':
            print(informations.hInfo)
            sys.exit(0)

        case '-new':
            if args.__len__() == 6:
                target = args[2]
                content = [args[3], args[4]]
                execTime = args[5]
                ######
                if not autoFill.start(2, target, content, execTime):
                    print("执行失败, 请检查参数")
                    sys.exit(1)

                print("执行完成")
                sys.exit(0)
            elif args[2].lower() == '-num':
                if int(args[3]) > 0 and args.__len__() == 6 + int(args[3]):
                    target = args[4]
                    content = []
                    for i in range(5, 5 + int(args[3])):
                        content.append(args[i])
                    execTime = args[5 + int(args[3])]
                    #######
                    if not autoFill.start(int(args[3]), target, content, execTime):
                        print("执行失败, 请检查参数")
                        sys.exit(1)

                    print("执行完成")
                    sys.exit(0)
                else:
                    print(informations.numErrorInfo)
                    sys.exit(1)
            else:
                print(informations.argErrorInfo)

        case _:
            print(informations.argErrorInfo)
            sys.exit(1)
