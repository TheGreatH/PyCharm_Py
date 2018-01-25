#coding=utf-8
import pyHook
import pythoncom

list_2D = [[1 for col in range(5)] for row in range(5)]
def iterat(array):
    array1 = []
    if len(array) == 1:
        return array[0]
    else:
        if array[0] == array[1]:
            array[0] += array[1]
    array1.extend(array[0])
    temp = array.pop(0)
    array.append(temp)
    array[len(array)-1] = 0
    array1 += iterat(array[1:])
    return array1

def onKeyboardEvent(event):
    # 监听键盘事件
    if event.Key == "Up":
        list_2D[1][1] += 1
    elif event.Key == "Down":
        iterat(list_2D[0])
    print list_2D
    return (event.Key)

def main():
    # 创建一个“钩子”管理对象
    hm = pyHook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 监听所有鼠标事件
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()
