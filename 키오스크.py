import pygame
import os
import json
from button import*
from random import*
from tkinter import*
####################################################################
pygame.init()

screen_width = 1500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("키오스크")
####################################################################
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "키오스크_img")
# 폰트
bfont = pygame.font.SysFont("휴먼편지체", 80)
xfont = pygame.font.SysFont("휴먼고딕", 40)
font = pygame.font.SysFont("휴먼편지체", 40)
sfont = pygame.font.SysFont("휴먼매직체", 20)
# 이미지
background = pygame.image.load(os.path.join(image_path, "background.png"))
button = pygame.image.load(os.path.join(image_path, "button.png"))
button_width = button.get_width()
button_height = button.get_height()
side_button = pygame.image.load(os.path.join(image_path, "side_button.png"))
side_button_width = side_button.get_width()
side_button_height = side_button.get_height()
white_board = pygame.image.load(os.path.join(image_path, "white_board.png"))
x_box = pygame.image.load(os.path.join(image_path, "x_box.png"))
x_box_width = x_box.get_width()
x_box_height = x_box.get_height()
pay_box = pygame.image.load(os.path.join(image_path, "pay_box.png"))
pay_box_width = pay_box.get_width()
pay_box_height = pay_box.get_height()
rbutton = pygame.image.load(os.path.join(image_path, "rbutton.png"))
rbutton_width = rbutton.get_width()
rbutton_height = rbutton.get_height()
checkbox = pygame.image.load(os.path.join(image_path, "checkbox.png"))
longbox = pygame.image.load(os.path.join(image_path, "longbox.png"))
longbox_width = longbox.get_width()
bbutton = pygame.image.load(os.path.join(image_path, "bbutton.png"))
brbutton = pygame.image.load(os.path.join(image_path, "brbutton.png"))
gside_button = pygame.image.load(os.path.join(image_path, "gside_button.png"))

# 추가요소 정의
delay = pygame.time.delay # 시간 지연
dtime = 200 # delay를 얼마나 오래 하는가
status = 'h' # 화면 나타태기
desk_time = [[0, 0] for i in range(4)] # 좌석 남은 시간
num = [0, 0, 0, 0, 0] # [블루레몬 총 판매량, 청포도 총 판매량, 아이스티 총 판매량, 아.아 총 판매량, 랜덤 음료 총 판매량]
cnum = [0, 0, 0, 0, 0] # [블루레몬 선택 개수, 청포도 선택 개수, 아이스티 선택 개수, 아.아 선택 개수, 랜덤 음료 선택 개수]
menu = ["마나물약", "행운의 물약", "체력물약", "어둠의 물약", "판도라의 물약"] # 메뉴
menu_money = [2000, 2000, 2000, 2000, 2000] # 메뉴당 가격
#order = [] # 테이크 아웃 주문
desk_order = [[0, 0, 0, 0, 0] for i in range(4)] # 매장 주문
num_order = 0 # 주문 번호
norder = 0 # 요리부가 볼 주문 번호
len_time = 900 # 대기 시간
r_time = [0, 0, 0] #[몇 번 테이블, 시간 만료된 시각, 메시지를 보여줄 남은 시간]
msg_time = 10 # 메시지를 보여줄 시간
img = [button, bbutton, brbutton, rbutton]
stop = 20
rainbow = 0
pandora_box = ["정말 이것을 고르겠는가 어리석은 인간이여", "고객님이 이것을 먹고 쓰러져도 저희는 책임을 지지 않습니다 ^^",\
    "판도라의 상자를 연 것은 자네이니 내 탓은 하지 말어", "미리 고인의 명복을...", "지금이라도 늦지 않았어, 어서 돌아가...!"]
is_data = False
# 버튼 정의

# Fontbtn은 안에 글씨 하나만 있는 버튼
store = Fontbtn(screen_width/3 - button_width/2, screen_height/2 - button_height/2, button, 1)
takeout = Fontbtn(screen_width*2/3 - button_width/2, screen_height/2 - button_height/2, button, 1)
see_desk = Fontbtn(0, 0, side_button, 1)
see_total = Fontbtn(screen_width - side_button_width, 0, side_button, 1)
ordered = Fontbtn(screen_width - side_button_width, screen_height - side_button_height, side_button, 1)
desk1 = Fontbtn(screen_width/2 - (button_width + 25), screen_height/2 - (button_height + 25), button, 1)
desk2 = Fontbtn(screen_width/2 + 25, screen_height/2 - (button_height + 25), button, 1)
desk3 = Fontbtn(screen_width/2 - (button_width + 25), screen_height/2 + 25, button, 1)
desk4 = Fontbtn(screen_width/2 + 25, screen_height/2 + 25, button, 1)
cal_x = Fontbtn(screen_width - 40, screen_height - (button_height + 150), x_box, 1)
back = Fontbtn(screen_width - 200, 0, side_button, 1)
pay = Fontbtn(screen_width - 80, screen_height - 40, pay_box, 1)
home_x = Fontbtn(screen_width - x_box_width*2, 0, x_box, 2)
note = Fontbtn(screen_width/2 - longbox_width/2, 0, longbox, 1)
pandora_button = Fontbtn(0, 0, side_button, 1)
plus = Fontbtn(screen_width/2 + button_width/2 + 100, screen_height/2 - button_height/4, button, 0.5)
minus = Fontbtn(screen_width/2 - button_width - 100, screen_height/2 - button_height/4, button, 0.5)
check = Fontbtn(screen_width/2 - side_button_width/2, screen_height/2 + button_height/2 + side_button_height, side_button, 1)
gui_btn = Fontbtn(screen_width - side_button_width, screen_height - side_button_height, side_button, 1)
yes_btn = Fontbtn(screen_width/2 - side_button_width*3/4, screen_height/2 + side_button_height*3/4, side_button, 0.5)
no_btn = Fontbtn(screen_width/2 + side_button_width/4, screen_height/2 + side_button_height*3/4, side_button, 0.5)
# Subbtn은 추가로 작은 글씨를 써넣는 버튼
blue = Subbtn(screen_width/5 - button_width/2, screen_height/2 - 200, button, 1)
green = Subbtn(screen_width*2/5 - button_width/2, screen_height/2 - 200, button, 1)
ice = Subbtn(screen_width*3/5 - button_width/2, screen_height/2 - 200, button, 1)
a_a = Subbtn(screen_width*4/5 - button_width/2, screen_height/2 - 200, button, 1)
crandom = Subbtn(screen_width*4/5 - button_width/2, screen_height/2 - 200, button, 1)
cblue = Subbtn(screen_width/5 - button_width/2, screen_height - (button_height + 100), button, 1)
cgreen = Subbtn(screen_width*2/5 - button_width/2, screen_height - (button_height + 100), button, 1)
cice = Subbtn(screen_width*3/5 - button_width/2, screen_height - (button_height + 100), button, 1)
ca_a = Subbtn(screen_width*4/5 - button_width/2, screen_height - (button_height + 100), button, 1)
rdesk1 = Subbtn(screen_width/2 - (button_width + 25), screen_height/2 - (button_height + 25), rbutton, 1)
rdesk2 = Subbtn(screen_width/2 + 25, screen_height/2 - (button_height + 25), rbutton, 1)
rdesk3 = Subbtn(screen_width/2 - (button_width + 25), screen_height/2 + 25, rbutton, 1)
rdesk4 = Subbtn(screen_width/2 + 25, screen_height/2 + 25, rbutton, 1)
#Checkbtn은 왼쪽에 글씨가 써지고 오른쪽에 체크박스가 있는 버튼
# ctable1 = Checkbtn(260, x_box_height*2 + 50, checkbox, 1, menu[0] + menu[1])
# ctable2 = Checkbtn(260, x_box_height*2 + 100, checkbox, 1, menu[0] + menu[1])
# ctable3 = Checkbtn(260, x_box_height*2 + 150, checkbox, 1, menu[0] + menu[1])
# ctable4 = Checkbtn(260, x_box_height*2 + 200, checkbox, 1, menu[0] + menu[1])
# c1 = Checkbtn(100, x_box_height*2 + 300, checkbox, 1, menu[0] + menu[1])
# c2 = Checkbtn(100, x_box_height*2 + 350, checkbox, 1, menu[0] + menu[1])
# c3 = Checkbtn(100, x_box_height*2 + 400, checkbox, 1, menu[0] + menu[1])
# 저장
try:
    with open("drink_data.txt") as file:
        data = json.load(file)
    is_data = True
except:
    is_data = False
    data = {
        "num" : {
            'blue' : 0,
            'green' : 0,
            'ice' : 0,
            'a_a' : 0,
            'random' : 0
        }
    }
menu_table = [i for i in data['num'].keys()]
# 화면 정의
def gui():
    root = Tk()
    root.title("초기 설정")
    root.geometry(f"320x120+{int(screen_width/2-160)}+{int(screen_height/2 - 60)}")

    num = StringVar()
    label = Label(root, text = "메뉴 개수").grid(row=0, column=0)

    e = Entry(root, textvariable = num,width = 5).grid(row=0, column=1)

    def btncmd():
        global ans
        ans = num.get()
        print(ans)
        root.destroy()

    btn = Button(root, text = "확인", command = btncmd).grid(row = 0, column =2)

    root.mainloop()

def where(): # 현재 어떤 화면인가?
    global data, is_data
    if is_data:
        white_board_rect = white_board.get_rect(center = (screen_width/2, screen_height/2))
        screen.blit(white_board, white_board_rect)
        if yes_btn.draw(screen, font, "예"):
            is_data = False
        if no_btn.draw(screen, font, "아니오"):
            data = {
                "num" : {
                    'blue' : 0,
                    'green' : 0,
                    'ice' : 0,
                    'a_a' : 0,
                    'random' : 0
                }
            }
            is_data = False
        load_data = font.render("저장된 데이터가 있습니다. 불러오시겠습니까?", True, (0, 0, 0))
        load_data_rect = load_data.get_rect(center = (screen_width/2, screen_height/2 - 75))
        screen.blit(load_data, load_data_rect)
    elif status == 'h':
        home()
    elif status == 'dc':
        desk_check()
    elif status == 't':
        total_check()
    elif status == 'd':
        desk()
    elif status == 'o':
        ordering()
    elif status == 'p':
        pandora()
    # elif status == 'oc':
    #     ordered_check()
# 기본 화면
def home():
    global status, location
    if store.draw(screen, font, "매장"):
        status = 'd'
        delay(dtime)
    if takeout.draw(screen, font, "테이크아웃"):
        status = 'o'
        location = 't'
        delay(dtime)
    if see_desk.draw(screen, font, "좌석"):
        status = 'dc'
        delay(dtime)
    if see_total.draw(screen, font, "집계"):
        status = 't'
        delay(dtime)
    if gui_btn.draw(screen, font, "GUI"):
        gui()
    # if ordered.draw(screen, font, "주문"):
    #     status = 'oc'
    #     delay(dtime)
# 좌석 확인
def desk_check():
    global status
    if home_x.draw(screen, bfont, "X"):
        status = 'h'
        delay(dtime)
    if desk_time[0][1] == 0: #만일 좌석 시간이 없다면 초록 박스 나타내기
        desk1.draw(screen, font, "1")
    else: # 아니라면 빨간 박스 나타내며 누를 시 좌석 시간 초기화 및 초록 박스 나타내기
        if desk_time[0][1] % 60 >= 10:
            if rdesk1.draw(screen, font, "1", sfont, str(int(desk_time[0][1]/60))+":"+str(int(desk_time[0][1]%60)), 50):
                desk_time[0] = [0, 0]
                desk_order[0] = [0, 0]
        else:
            if rdesk1.draw(screen, font, "1", sfont, str(int(desk_time[0][1]/60))+":0"+str(int(desk_time[0][1]%60)), 50):
                desk_time[0] = [0, 0]
                desk_order[0] = [0, 0]
    if desk_time[1][1] == 0:
        desk2.draw(screen, font, "2")
    else:
        if desk_time[1][1] % 60 >= 10:
            if rdesk2.draw(screen, font, "2", sfont, str(int(desk_time[1][1]/60))+":"+str(int(desk_time[1][1]%60)), 50):
                desk_time[1] = [0, 0]
                desk_order[1] = [0, 0]
        else:
            if rdesk2.draw(screen, font, "2", sfont, str(int(desk_time[1][1]/60))+":0"+str(int(desk_time[1][1]%60)), 50):
                desk_time[1] = [0, 0]
                desk_order[1] = [0, 0]
    if desk_time[2][1] == 0:
        desk3.draw(screen, font, "3")
    else:
        if desk_time[2][1] % 60 >= 10:
            if rdesk3.draw(screen, font, "3", sfont, str(int(desk_time[2][1]/60))+":"+str(int(desk_time[2][1]%60)), 50):
                desk_time[2] = [0, 0]
                desk_order[2] = [0, 0]
        else:
            if rdesk3.draw(screen, font, "3", sfont, str(int(desk_time[2][1]/60))+":0"+str(int(desk_time[2][1]%60)), 50):
                desk_time[2] = [0, 0]
                desk_order[2] = [0, 0]
    if desk_time[3][1] == 0:
        desk4.draw(screen, font, "4")
    else:
        if desk_time[3][1] % 60 >= 10:
            if rdesk4.draw(screen, font, "4", sfont, str(int(desk_time[3][1]/60))+":"+str(int(desk_time[3][1]%60)), 50):
                desk_time[3] = [0, 0]
                desk_order[3] = [0, 0]
        else:
            if rdesk4.draw(screen, font, "4", sfont, str(int(desk_time[3][1]/60))+":0"+str(int(desk_time[3][1]%60)), 50):
                desk_time[3] = [0, 0]
                desk_order[3] = [0, 0]
# 집계
def total_check():
    global status
    if home_x.draw(screen, bfont, "X"):
        status = 'h'
        delay(dtime)
    total = bfont.render("총 판매액: " + str(menu_money[0] * data["num"][menu_table[0]] + menu_money[1] * data["num"][menu_table[1]]\
         + menu_money[2] * data["num"][menu_table[2]]+ menu_money[3] * data["num"][menu_table[3]]\
             + menu_money[4] * data["num"][menu_table[4]]) + "원", True, (0, 0, 0))
    screen.blit(total, (0, 2*x_box_height))
    num_blue = font.render(menu[0] + ": " + f'{data["num"]["blue"]}' + "개", True, (0, 0, 0))
    screen.blit(num_blue, (0, 2*x_box_height+160))
    num_green = font.render(menu[1] + ": " + f'{data["num"]["green"]}' + "개", True, (0, 0, 0))
    screen.blit(num_green, (0, 2*x_box_height+220))
    num_ice = font.render(menu[2] + ": " + f'{data["num"]["ice"]}' + "개", True, (0, 0, 0))
    screen.blit(num_ice, (0, 2*x_box_height+280))
    num_a_a = font.render(menu[3] + ": " + f'{data["num"]["a_a"]}' + "개", True, (0, 0, 0))
    screen.blit(num_a_a, (0, 2*x_box_height+340))
    num_random = font.render(menu[4] + ": " + f'{data["num"]["random"]}' + "개", True, (0, 0, 0))
    screen.blit(num_random, (0, 2*x_box_height+400))
# 매장에서 좌석 고르기
def desk():
    global status, location
    if back.draw(screen, font, "처음으로"):
        delay(dtime)
        status = 'h'
    if desk_time[0][1] == 0: # 좌석 시간이 없다면 클릭했을 시 시간 감소
        if desk1.draw(screen, font, "1"):
            desk_time[0][0] = pygame.time.get_ticks()
            status = 'o'
            location = 0
            delay(dtime)
    else:   # 아니라면 빨간 박스 나타내기
        if desk_time[0][1] % 60 >= 10: 
            rdesk1.draw(screen, font, "1", sfont, str(int(desk_time[0][1]/60))+":"+str(int(desk_time[0][1]%60)), 50)
        else:
            rdesk1.draw(screen, font, "1", sfont, str(int(desk_time[0][1]/60))+":0"+str(int(desk_time[0][1]%60)), 50)
    if desk_time[1][1] == 0:
        if desk2.draw(screen, font, "2"):
            desk_time[1][0] = pygame.time.get_ticks()
            status = 'o'
            location = 1
            delay(dtime)
    else:
        if desk_time[1][1] % 60 >= 10:
            rdesk2.draw(screen, font, "2", sfont, str(int(desk_time[1][1]/60))+":"+str(int(desk_time[1][1]%60)), 50)
        else:
            rdesk2.draw(screen, font, "2", sfont, str(int(desk_time[1][1]/60))+":0"+str(int(desk_time[1][1]%60)), 50)
    if desk_time[2][1] == 0:
        if desk3.draw(screen, font, "3"):
            desk_time[2][0] = pygame.time.get_ticks()
            status = 'o'
            location = 2
            delay(dtime)
    else:
        if desk_time[2][1] % 60 >= 10:
            rdesk3.draw(screen, font, "3", sfont, str(int(desk_time[2][1]/60))+":"+str(int(desk_time[2][1]%60)), 50)
        else:
            rdesk3.draw(screen, font, "3", sfont, str(int(desk_time[2][1]/60))+":0"+str(int(desk_time[2][1]%60)), 50)
    if desk_time[3][1] == 0:
        if desk4.draw(screen, font, "4"):
            desk_time[3][0] = pygame.time.get_ticks()
            status = 'o'
            location = 3
            delay(dtime)
    else:
        if desk_time[3][1] % 60 >= 10:
            rdesk4.draw(screen, font, "4", sfont, str(int(desk_time[3][1]/60))+":"+str(int(desk_time[3][1]%60)), 50)
        else:
            rdesk4.draw(screen, font, "4", sfont, str(int(desk_time[3][1]/60))+":0"+str(int(desk_time[3][1]%60)), 50)
# 주문 화면
def ordering():
    global location, cnum, status, norder, pandora_text
    if back.draw(screen, font, "처음으로"):
        cnum = [0, 0, 0, 0, 0]
        delay(dtime)
        status = 'h'
        if location != 't':
            desk_time[location] = [0, 0]
    if blue.draw(screen, font, menu[0], sfont, "블루레몬 에이드", 120): # 블루레몬 클릭시 개수 증가
        cnum[0] += 1
    if green.draw(screen, font, menu[1], sfont, "청포도 에이드", 120): # 청포도 클릭시 개수 증가
        cnum[1] += 1
    if ice.draw(screen, font, menu[2], sfont, "아이스티", 120): # 아이스티 클릭시 개수 증가
        cnum[2] += 1
    if a_a.draw(screen, font, menu[3], sfont, "아이스 아메리카노", 120):
        cnum[3] += 1
    if pandora_button.draw(screen, font, "판도라의 상자"):
        status = 'p'
        pandora_text = choice(pandora_box)
        delay(dtime)
    if cnum[0] != 0 or cnum[1] != 0 or cnum[2] != 0 or cnum[3] != 0 or cnum[4] != 0:
        screen.blit(white_board, (0, screen_height - (button_height + 150)))
        if cblue.draw(screen, font, menu[0], sfont, "개수: " + str(cnum[0]), 120):
            if cnum[0] != 0:
                cnum[0] -= 1
        if cgreen.draw(screen, font, menu[1], sfont, "개수: " + str(cnum[1]), 120):
            if cnum[1] != 0:
                cnum[1] -= 1
        if cice.draw(screen, font, menu[2], sfont, "개수: " + str(cnum[2]), 120):
            if cnum[2] != 0:
                cnum[2] -= 1
        if ca_a.draw(screen, font, menu[3], sfont, "개수: " + str(cnum[3]), 120):
            if cnum[3] != 0:
                cnum[3] -= 1
        if cal_x.draw(screen, xfont, "X"):
            cnum = [0, 0, 0, 0, 0]
        money = font.render("금액: " + str(menu_money[0] * cnum[0] + menu_money[1] * cnum[1] + menu_money[2] * cnum[2]\
            + menu_money[3] * cnum[3] + menu_money[4] * cnum[4]) + "원", True, (0, 0, 0))
        screen.blit(money, (screen_width - 320, screen_height - 40))
        if pay.draw(screen, font, "결제"):
            for i in range(len(cnum)):
                data["num"][menu_table[i]] += cnum[i]
            if location == 't':
                print(str(norder + 1) + ". " + menu[0] + " " + str(cnum[0]) + "개, "+ \
                    menu[1]+ " " +str(cnum[1])+"개, " + menu[2] + " " + str(cnum[2]) + "개, " + menu[3] + " " + str(cnum[3]) + " 개, "+\
                        menu[4] + " " + str(cnum[4]) + "개")
                norder += 1
            else:
                desk_order[location] = cnum
                print(str(location+1) + "번 테이블 - "+ menu[0] + " " +str(desk_order[location][0]) + "개, "+ \
                    menu[1]+ " " +str(desk_order[location][1]) + "개, " + menu[2] + " " +str(desk_order[location][2]) + "개, " +\
                        menu[3] + " " +str(desk_order[location][3]) + " 개, " + menu[4] + " " + str(desk_order[location][4]) + "개")
            cnum = [0, 0, 0, 0, 0]
            status = 'h'
            delay(dtime)

def pandora():
    global cnum, status, pandora_text
    random.draw(screen, font, menu[4], sfont, pandora_text, 120)
    number = sfont.render("개수: " + str(cnum[4]), True, (0, 0, 0))
    number_rect = number.get_rect(center = (screen_width/2, screen_height/2 - button_height/2 - 20))
    screen.blit(number, number_rect)
    if plus.draw(screen, font, "+"):
        cnum[4] += 1
        pandora_text = choice(pandora_box)
    if minus.draw(screen, font, "-"):
        if cnum[4] != 0:
            pandora_text = choice(pandora_box)
            cnum[4] -= 1
    if check.draw(screen, font, "확인"):
        status = 'o'
        delay(dtime)

# 주문 확인
# def ordered_check():
#     global status, num_order
#     if home_x.draw(screen, bfont, "X"):
#         status = 'h'
#         delay(dtime)
#     table = font.render("테이블:", True, (0, 0, 0))
#     screen.blit(table, (0, x_box_height*2))
#     table1 = font.render("1번 테이블 - ", True, (0, 0, 0))
#     screen.blit(table1, (50, x_box_height*2 + 50))
#     if desk_order[0][0] != 0 or desk_order[0][1] != 0:
#         if ctable1.draw(screen, font, menu[0] + " " + str(desk_order[0][0]) + "개, " + menu[1] + " " + str(desk_order[0][1]) + "개"):
#             desk_order[0] = [0, 0]
#     table2 = font.render("2번 테이블 - ", True, (0, 0, 0))
#     screen.blit(table2, (50, x_box_height*2 + 100))
#     if desk_order[1][0] != 0 or desk_order[1][1] != 0:
#         if ctable2.draw(screen, font, menu[0] + " " + str(desk_order[1][0]) + "개, " + menu[1] + " " +str(desk_order[1][1])+"개"):
#             desk_order[1] = [0, 0]
#     table3 = font.render("3번 테이블 - ", True, (0, 0, 0))
#     screen.blit(table3, (50, x_box_height*2 + 150))
#     if desk_order[2][0] != 0 or desk_order[2][1] != 0:
#         if ctable3.draw(screen, font, menu[0] + " " + str(desk_order[2][0]) + "개, "+ menu[1]+ " " +str(desk_order[2][1])+"개"):
#             desk_order[2] = [0, 0]
#     table4 = font.render("4번 테이블 - ", True, (0, 0, 0))
#     screen.blit(table4, (50, x_box_height*2 + 200))
#     if desk_order[3][0] != 0 or desk_order[3][1] != 0:
#         if ctable4.draw(screen, font, menu[0] + " " + str(desk_order[3][0]) + "개, "+ menu[1] + " " +str(desk_order[3][1])+"개"):
#             desk_order[3] = [0, 0]
#     take = font.render("테이크 아웃:", True, (0, 0, 0))
#     screen.blit(take, (0, x_box_height*2 + 250))
#     one = font.render(str(num_order + 1) + ". ", True, (0, 0, 0))
#     screen.blit(one, (50, x_box_height*2 + 300))
#     if len(order) >= 1:
#         if c1.draw(screen, font, menu[0] + " " + str(order[0][0]) + "개, "+ menu[1]+ " " +str(order[0][1])+"개"):
#             del order[0]
#             num_order += 1
#     two = font.render(str(num_order + 2) + ". ", True, (0, 0, 0))
#     screen.blit(two, (50, x_box_height*2 + 350))
#     if len(order) >= 2:
#         if c2.draw(screen, font, menu[0] + " " + str(order[1][0]) + "개, "+ menu[1] + " " +str(order[1][1])+"개"):
#             del order[1]
#             num_order += 1
#     three = font.render(str(num_order + 3) + ". ", True, (0, 0, 0))
#     screen.blit(three, (50, x_box_height*2 + 400))
#     if len(order) >= 3:
#         if c3.draw(screen, font, menu[0] + " " + str(order[2][0]) + "개, "+ menu[1] + " " +str(order[2][1])+"개"):
#             del order[2]
#             num_order += 1
# 실제 작업 환경
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('drink_data.txt', 'w') as file:
                json.dump(data, file)
            running = False

    # 만일 좌석을 클릭했다면 시간을 감소시키기
    current_time = pygame.time.get_ticks()
    for idx, i in enumerate(desk_time):
        if i[0] != 0:
            i[1] = int(len_time - (current_time - i[0])/1000)
            if i[1] == 0:
                desk_time[idx] = [0, 0]
                r_time = [idx+1, pygame.time.get_ticks(), msg_time]
    if stop == 20:
        if rainbow:
            random = Subbtn(screen_width/2 - button_width/2, screen_height/2 - button_height/2, img[rainbow], 1)
        else: 
            random = Subbtn(screen_width/2 - button_width/2, screen_height/2 - button_height/2, img[rainbow], 1)
        stop = 0
        rainbow += 1
        if rainbow == len(img):
            rainbow = 0
    else: stop += 1

    # 화면 구성
    screen.blit(background, (0, 0))
    where()

    # 시간이 다 지났으면 메시지 알리기
    if r_time[2] != 0:
        r_time[2] = int(msg_time - (current_time - r_time[1])/1000)
        note.draw(screen, font, str(r_time[0]) + "번 테이블 시간이 다 되었습니다.")
    else:
        r_time = [0, 0, 0]

    pygame.display.update()

pygame.quit()