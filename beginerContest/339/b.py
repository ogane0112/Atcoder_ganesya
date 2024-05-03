#なんか賢い方法ありそうだけども愚直に解いてみる
h,w,n = map(int,input().split())

#xとyの初期値
now_x = 0
now_y = 0
#向いてる方角の初期状態
direction = "↑"
direction_list = ["↑","→","↓","←"]
def move(now_x,now_y,field,direction):
    if field[now_x][now_y]==".":
        
        field[now_x][now_y] = "#"
        print(field[now_x][now_y])
        if direction == direction_list[0]:        
            #矢印を時計周りに更新する
            direction = direction_list[1]
            #現在の地点を更新する
            now_x += 0
            now_y += 1
            now_x ,now_y = check(now_x,now_y)
            return now_x ,now_y,field,direction
            
            
        elif direction == direction_list[1]:
            #矢印を時計周りに更新する
            direction = direction_list[2]
            #現在の地点を更新する
            now_x += 1
            now_y += 0
            now_x ,now_y = check(now_x,now_y)
            return now_x ,now_y,field,direction
        elif direction == direction_list[2]:
            #矢印を時計周りに更新する
            direction = direction_list[3]
            #現在の地点を更新する
            now_x += 0
            now_y -= 1
            now_x ,now_y = check(now_x,now_y)
            return now_x ,now_y,field,direction
        elif direction == direction_list[3]:
            
            #矢印を時計周りに更新する
            direction = direction_list[0]
            #現在の地点を更新する
            now_x -= 1
            now_y += 0
            now_x ,now_y = check(now_x,now_y)
            return now_x ,now_y,field,direction
    elif field[now_x][now_y]=="#":
        field[now_x][now_y] = "."
        if direction == direction_list[0]:
            #矢印を時計周りに更新する
            direction = direction_list[3]
            #現在の地点を更新する
            now_x += 0
            now_y -= 1
            now_x ,now_y = check(now_x,now_y)
            return now_x ,now_y,field,direction

        elif direction == direction_list[1]:
            #矢印を時計周りに更新する
            direction = direction_list[0]
            #現在の地点を更新する
            now_x -= 1
            now_y += 0
            now_x ,now_y = check(now_x,now_y)
            return now_x ,now_y,field,direction
            
        elif direction == direction_list[2]:
            #矢印を時計周りに更新する
            direction = direction_list[1]
            #現在の地点を更新する
            now_x += 0
            now_y += 1
            now_x ,now_y = check(now_x,now_y)
            return now_x ,now_y,field,direction
            
        elif direction == direction_list[3]:
            #矢印を時計周りに更新する
            direction = direction_list[2]
            #現在の地点を更新する
            now_x += 1
            now_y += 0
            now_x ,now_y = check(now_x,now_y)
            return now_x ,now_y,field,direction
            
    
    
    
    
#ドラクエの地図の処理を実装する
def check(now_x,now_y):    
    if now_x < 0 :
        now_x = h-2
    elif h-2 < now_x:
        now_x = 0
        
    if now_y < 0 :
        now_y = w-2
    elif h-2 < now_y:
        now_y = 0
    return now_x ,now_y
    
        
        
        
        
    
field = []
temp = []
for i in range(w):
   temp.append(".")
for i in range(h):
        field.append(temp)
        
# for i in range(n):
#     now_x ,now_y, field, direction = move(now_x ,now_y,field,direction)

now_x ,now_y, field, direction = move(now_x ,now_y,field,direction)
print(field)
now_x ,now_y, field, direction  = move(now_x ,now_y,field,direction)

        
        
