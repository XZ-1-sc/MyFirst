
class_info = []

def print_menu():
    print("-------------")
    print("学生管理系统V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("-------------")

def add_student():
    print("欢迎使用添加学生的伪功能")
    global class_info
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    score = input("请输入学生成绩：")

    for info in class_info:
        if info["name"] == name:
            print("学生姓名重名了")
            return
        
    student = {
        "name" : name,
        "age" : age,
        "score" : score
        }
    class_info.append(student)
    print("添加学生信息成功")
    print(class_info)

def show_student():
    global class_info
    print("姓名--年龄--成绩")
    for student in class_info:
        print(student["name"],student["age"],student["score"])

def del_student():
    print("欢迎使用删除学生功能")
    global class_info
    name = input("请输入删除学生的姓名")
    for student in class_info:
        if student["name"] == name:
            class_info.remove(student)
            print("删除学生信息成功")
            return
    print("删除学生信息不存在")

def modify_student():
    global class_info
    name = input("请输入需要修改的学生信息：")
    for student in class_info:
        if student["name"] == name:
            student["name"] = input("请输入修改后的学生姓名:")
            jx = input("是否继续修改：")
            if jx == "yes":
                student["age"] = input("请输入修改后学生的年龄:")
                student["score"] = input("请输入修改后学生的成绩：")
            else:
                return
            print("修改学生信息成功")
            return
    print("您输入的学生信息不存在")

def search_student():
    global class_info
    name = input("请输入查找学生的姓名:")
    for student in class_info:
        if student["name"] == name:
            print(student["name"],student["age"],student["score"])
            return
    print("您输入的学生信息不存在")

  
def main():
    pass

    while True:
        print_menu()
        choose = int(input("请输入需要的功能:"))

        if choose == 1:
            add_student()
        elif choose == 2:
            del_student()
        elif choose == 3:
            modify_student()
        elif choose == 4:
            search_student()
        elif choose == 5:
            show_student()
        elif choose == 6:
            print("退出系统")
            break

if __name__ == '__main__':
    main()
