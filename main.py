import tkinter as tk
import random
import threading
import time
def dow():
    window = tk.Tk()
    width=window.winfo_screenwidth()
    height=window.winfo_screenheight()
    a=random.randrange(0,width)
    b=random.randrange(0,height)
    window.title('XX祝您')
    window.geometry("200x50"+"+"+str(a)+"+"+str(b))
    tk.Label(window,
        text='天天快乐，不要emo！',    # 标签的文字
        bg='pink',     # 背景颜色
        font=('楷体', 17),     # 字体和字体大小
        width=15, height=2  # 标签长宽
        ).pack()    # 固定窗口位置
    window.mainloop()
 
threads = []
for i in range(100):#需要的弹框数量
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()
