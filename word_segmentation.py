# setup
dictionary = open("dict_no_space.txt", "r",encoding="utf-8").readlines()
text = input("input : ")

def is_alnum(s):
    if (u'\u0041'<= s <= u'\u005a') or (u'\u0061'<= s <= u'\u007a') or (s.isdigit()) :
        return True
    else: return False

# FMM
def forward_maximum_matching(text,dictionary):
    max_length = max([(len(item)-len("\n")) for item in dictionary]) #從字典中最長的單詞開始檢查
    start = 0
    
    while start < len(text): #在還沒掃完整個text之前
        index = start + max_length #從start到index之間去找字典中的單詞
        if index > len(text): #如果輸入的text比字典的最常單詞還要短
            index = len(text) #直接掃整個text
        for i in range(max_length):
            #英文或數學斷詞
            if is_alnum(text[start]) :
                if (start != 0) :
                    print(",\'",end="")    #第一個不要print   
                while (start < len(text)) and is_alnum(text[start]) :
                    print(text[start],end="")   # 印出連續的英文或數字
                    start += 1
                print("\'",end="")
                break #這樣start才不會判定out of range
            #中文斷詞
            if ((text[start:index] + "\n") in dictionary) or (len(text[start:index]) == 1):
                if (start != 0) :
                    print(",\'",end="") #第一個不要print
                print(text[start:index],end = '\'')
                start = index   #從index處開始繼續向後檢查
                break #這樣start才不會判定out of range
            index -= 1  #縮小length範圍

# main
print('[\'', end = "")
forward_maximum_matching(text,dictionary)
print("]")