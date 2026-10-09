a = int(input())
b = int(input())
s = int(input())

if (a != 0 and a != 1) or (b != 0 and b != 1) or (s != 0 and s != 1):
    print("輸入錯誤")
else:
    if a != b:
        middle = 1
    else:
        middle = 0


    if middle == 1 and s == 1:
        start = 1
    else:
        start = 0

    print(f"第一個閘輸出={middle}")
    print(f"允許啟動={start}")