import sys
import informations
import initializer
import autoFill


if __name__ == '__main__':
    # 读取命令行参数，固定参数为 -init, -help,中的一个或者 -new -fID + 字符串, -sName + 字符串 , -sID + 字符串, -t + 字符串
    args = sys.argv
    if args.__len__() == 2:
        if args[1].lower() == "-help" or args[1].lower() == "-h":
            print(informations.hInfo)
            sys.exit(0)
            pass
        elif args[1].lower() == "-init":
            print("开始初始化")
            try:
                if initializer.init():
                    print("初始化完成")
                    sys.exit(0)
                    pass
            except Exception:
                print("初始化失败\n" + Exception)
                sys.exit(0)

            print("初始化失败")
            sys.exit(0)
            pass
        else:
            print(informations.argErrorInfo)
            sys.exit(1)
            pass
    elif args.__len__() == 6:
        if args[1].lower() == "-new":
            forumID = args[2]
            studentName = args[3]
            studentID = args[4]
            startTime = args[5]
            autoFill.start(forumID, studentName, studentID, startTime)
            sys.exit(0)
            pass
        else:
            print(informations.argErrorInfo)
            sys.exit(1)
            pass
    else:
        print(informations.argErrorInfo)
        sys.exit(1)
        pass
