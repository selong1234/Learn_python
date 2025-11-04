import win32gui
import win32con
import win32api
# import psutil
import win32process
import time

# 获取当前鼠标【x y】坐标
while (True):
    point = win32api.GetCursorPos()  
    # 通过坐标获取坐标下的【窗口句柄】
    hwnd = win32gui.WindowFromPoint(point.x, point.y)  # 请填写 x 和 y 坐标  
    # 通过句柄获取【线程ID 进程ID】
    hread_id, process_id = win32process.GetWindowThreadProcessId(hwnd)   
    print(hread_id, process_id)
    time.sleep(1)
    
