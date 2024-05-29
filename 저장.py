import sys
menuList = []
priceList = []

def printList():
    print("메뉴명:", menuList)
    print("가격:", priceList)

def addList(menu, price):
    menuList.append(menu)
    priceList.append(price)
    print("등록되었습니다")
def removeList(menu):
    if menu in memuList:
        i=menuList.index(menu)
        menuList.remove(menu)
        priceList.pop(i)


        print(menu,"가 삭제되었습니다.")



        
while True:
    print("")
    print("------------------")
    print("메뉴 관리 프로그램")
    print("------------------")
    print("1.메뉴 보기")
    print("2.메뉴 등록")
    print("3.메뉴 삭제")
    print("4.메뉴 변경")
    print("9.종     료")

    ans = int(input("메뉴번호를 입력하시오: "))

    if ans == 1:
        printList()
    elif ans == 2:
        name = input("메뉴 이름을 입력하시오: ")
        price = int(input("가격을 입력하시오: "))
        addList(name, price)
    elif ans == 3:
        name = input("삭제할 메뉴명을 입력하세요: ")
        removeList(menu)
   
