from tkinter import *
from tkinter import messagebox
import csv
import folium  # cmd 에서 pip install folium
import webbrowser
import pandas as pd  # cmd 에서 pip install pandas
import random





main_map = folium.Map(location=[37.508077, 126.960482], zoom_start=30) #메인 지도 생성

#밑으로는 마커를 찍기 위한 좌표 설정

# pandas에서 제공하는 dataFrame 형태로 저장

dessert_place = pd.DataFrame({#디저트 가게
    'lon': [37.506902, 37.506953, 37.507645], #경도
    'lat': [126.958160, 126.958424, 126.959961], #위도
    'name': ['Starbucks', 'Ediya', 'BeBridge'] #상호
})

korean_place = pd.DataFrame({ #한식
    'lon': [37.507188, 37.507249, 37.507599],
    'lat': [126.959696, 126.959244, 126.960208],
    'name': ['YukSsam ColdNoodle', 'NaeJjimDak', 'YangPun KimChiJjiGae']

})

chinese_place = pd.DataFrame({ #중식
    'lon': [37.508210, 37.507840, 37.507591],
    'lat': [126.960972, 126.960686, 126.960096],
    'name': ['AnDongJang', 'HongKong BanJum', 'NiPPong NaePPong']
})
17931
japanese_place = pd.DataFrame({ #일식
    'lon': [37.508491, 37.508198, 37.507661],
    'lat': [126.961256, 126.961061, 126.959239],
    'name': ['Misoya', 'EunHengGol', 'HaGgoMen']
})

drink_place = pd.DataFrame({ #술집
    'lon': [37.508346, 37.507664, 37.507940],
    'lat': [126.961599, 126.960490, 126.960674],
    'name': ['JangDokDae', 'FishAndGrill', 'YoSulShiGye']
})

vegeterian_place = pd.DataFrame({ #베지테리안
    'lon': [37.506954, 37.507407],
    'lat': [126.958458, 126.959619],
    'name': ['Subway', 'ToGoSalad']
})


def Start(): # Start버튼을 눌렀을 때
    window2.deiconify()
def Bye(): #quit 버튼을 눌렀을 때
    global window1
    window1.destroy() #창을 모두 닫는다

def Meal(): # Meal 버튼을 눌렀을 때
    window3.deiconify()
    window2.withdraw()
    


#csv 파일에 있는 데이터를 csvlist에 딕셔너리 형태로 저장
csvlist=[]
with open("Rest_info.csv", mode="r") as f:
    reader=csv.reader(f)
    header=next(reader)
    for a in reader:
        a[0]={"name":a[0],"category":a[1],"main menu":a[3], "spicy":a[4], "open":a[5], "preference":a[6]}
        csvlist.append(a[0])

    

def Dessert(): # Meal, Dessert, Drink, Vegeterian 중 Dessert 선택

    window2.withdraw() #윈도우 2 닫기
    dessertlist = [] #리스트 초기화



    def clicked(): #Detail 버튼이 클릭되었을 때 실행되는 함수 
        doublelist = []
        curselect = listbox2.curselection() #리스트박스에서 선택된 값을 저장

        
        for a in csvlist: # csvlist에 저장했던 딕셔너리의 name키에 해당하는 value값이 
            if a["name"]==listbox2.get(curselect): # listbox에서 선택된 값과 csvlist에 저장했던 각 딕셔너리의 name키에 해당하는 value값을 비교해서
                #가게이름, 메인메뉴, 매운정도, 오픈시간, 고기재료의 종류 정보를 가져와서 doublelist에 저장한다. 
                doublelist.append(a["name"])
                doublelist.append(a["main menu"])
                doublelist.append(a["spicy"])
                doublelist.append(a["open"])
                doublelist.append(a["preference"])

 
        #새 윈도우를 띄워서 선택된 가게 맞춤 디테일 정보 제공
        window_detail = Toplevel()
        window_detail.title("Information")
        window_detail.geometry("400x400")
        window_detail.configure(background="#3c4f55")


        text_detail = Text(window_detail,width=60, height=65, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff' ) #doublelist에 저장된 값들을 Text창에 띄운다
        text_detail.insert(1.0, doublelist[0]+"\n")
        text_detail.insert(2.0,"Main Menu: "+doublelist[1]+"\n") #메인메뉴?
        text_detail.insert(3.0,"Spicy?: "+doublelist[2]+"\n") #매운지?
        text_detail.insert(4.0,"Open: "+doublelist[3]+"\n") #오픈시간은?
        text_detail.insert(5.0,"Preference: "+doublelist[4]) # 고기재료의 종류?
   
        text_detail.pack()
        


    def rd():
        randomlist=[]
        random2 = random.randint(0,len(dessertlist)-1) #랜덤값 오류없이 조정
       
        for a in csvlist:
            if a["name"]==dessertlist[random2]:
                randomlist.append(a["name"])
                randomlist.append(a["main menu"])
                randomlist.append(a["spicy"])
                randomlist.append(a["open"])
                randomlist.append(a["preference"])

        
        #새 윈도우를 띄워서 선택된 가게 맞춤 디테일 정보 제공
        window_detail = Toplevel() # 디테일 정보 제공을  위한 새 창
        window_detail.title("Information")
        window_detail.geometry("400x400")
        window_detail.configure(background="#3c4f55")

        text_detail = Text(window_detail,width=60, height=65, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff' ) #randomlist에 저장된 값들을 Text창에 띄운다
        text_detail.insert(1.0, randomlist[0]+"\n") #가게이름?
        text_detail.insert(2.0,"Main Menu: "+randomlist[1]+"\n") #메인메뉴?
        text_detail.insert(3.0,"Spicy?: "+randomlist[2]+"\n") #매운지?
        text_detail.insert(4.0,"Open: "+randomlist[3]+"\n") #오픈시간은?
        text_detail.insert(5.0,"Preference: "+randomlist[4]) # 고기재료의 종류?

        text_detail.pack()
                                  

           

       
    with open("Rest_info.csv", mode="r") as f: #CSV 파일에서 '디저트'에 맞는 항목들을 찾는 함수
        reader = csv.reader(f)
        header = next(reader)
        for a in reader:
            if a[1] == "Dessert":
                dessertlist.append(a[0])

    window = Toplevel()
    window.geometry("400x400")
    window.configure(background="#3c4f55")

    listbox2 = Listbox(window,selectmode='extended',width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff') #한 번에 여러 가지 항목 선택해서 Detail 보기 가능
    for dessert in dessertlist:
        listbox2.insert(END, dessert)
    listbox2.pack()

    button_dessert = Button(window, text="Detail", relief='groove',  width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff',command=clicked) #Detail 버튼 제공 (위에 clicked함수와 연동)
    button_dessert.pack()

    randombtn=Button(window,text="Random", relief='groove',  width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff',command=rd) #Random 버튼 제공
    randombtn.pack()

    how=Label(window, text="When you click 'Detail' button, please choose one. \n Click 'Random' if you can't choose :-)", width=70, bg='#3c4f55', font=("나눔고딕", 10), fg='#ffffff')
    how.pack()
    
    window2.withdraw()


    main_map = folium.Map(location=[37.508077, 126.960482], zoom_start=30) #지도 초기화
    
    for i in range(0, len(dessert_place)): #지도상에 좌표를 찍음
        folium.Marker([dessert_place.iloc[i]['lon'], dessert_place.iloc[i]['lat']],
                      popup=dessert_place.iloc[i]['name'],
                      icon=folium.Icon(color='purple', icon='star')).add_to(main_map)

    main_map.save('CAU_map.html')
    f = webbrowser.open('CAU_map.html')


def Drink():# Meal, Dessert, Drink, Vegeterian 중 Drink 선택

    window2.withdraw() #윈도우 2 닫기
    
    drinklist = [] #리스트 초기화
    
    def clicked(): #Detail 버튼이 클릭되었을 때 실행되는 함수 
        doublelist = []
        curselect = listbox3.curselection() #리스트박스에서 선택된 값을 저장

        
        for a in csvlist: # csvlist에 저장했던 딕셔너리의 name키에 해당하는 value값이 
            if a["name"]==listbox3.get(curselect): # listbox에서 선택된 값과 csvlist에 저장했던 각 딕셔너리의 name키에 해당하는 value값을 비교해서
                #가게이름, 메인메뉴, 매운정도, 오픈시간, 고기재료의 종류 정보를 가져와서 doublelist에 저장한다. 
                doublelist.append(a["name"])
                doublelist.append(a["main menu"])
                doublelist.append(a["spicy"])
                doublelist.append(a["open"])
                doublelist.append(a["preference"])

 
        #새 윈도우를 띄워서 선택된 가게 맞춤 디테일 정보 제공
        window_detail = Toplevel() # 디테일 정보 제공을  위한 새 창
        window_detail.title("Information")
        window_detail.geometry("400x400")
        window_detail.configure(background="#3c4f55")


        text_detail = Text(window_detail,width=60, height=65, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff' ) #doublelist에 저장된 값들을 Text창에 띄운다
        text_detail.insert(1.0, doublelist[0]+"\n")
        text_detail.insert(2.0,"Main Menu: "+doublelist[1]+"\n") #메인메뉴?
        text_detail.insert(3.0,"Spicy?: "+doublelist[2]+"\n") #매운지?
        text_detail.insert(4.0,"Open: "+doublelist[3]+"\n") #오픈시간은?
        text_detail.insert(5.0,"Preference: "+doublelist[4]) # 고기재료의 종류?
   
        text_detail.pack()



    def rd():
        randomlist=[]
        random2 = random.randint(0,len(drinklist)-1) #랜덤값 오류없이 조정
       
        for a in csvlist:
            if a["name"]==drinklist[random2]:
                randomlist.append(a["name"])
                randomlist.append(a["main menu"])
                randomlist.append(a["spicy"])
                randomlist.append(a["open"])
                randomlist.append(a["preference"])

        
        #새 윈도우를 띄워서 선택된 가게 맞춤 디테일 정보 제공
        window_detail = Toplevel() # 디테일 정보 제공을  위한 새 창
        window_detail.title("Information")
        window_detail.geometry("400x400")
        window_detail.configure(background="#3c4f55")

        text_detail = Text(window_detail,width=60, height=65, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff' ) #randomlist에 저장된 값들을 Text창에 띄운다
        text_detail.insert(1.0, randomlist[0]+"\n") #가게이름?
        text_detail.insert(2.0,"Main Menu: "+randomlist[1]+"\n") #메인메뉴?
        text_detail.insert(3.0,"Spicy?: "+randomlist[2]+"\n") #매운지?
        text_detail.insert(4.0,"Open: "+randomlist[3]+"\n") #오픈시간은?
        text_detail.insert(5.0,"Preference: "+randomlist[4]) # 고기재료의 종류?

        text_detail.pack()


    with open("Rest_info.csv", mode="r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for a in reader:
            if a[1] == "Drink":
                drinklist.append(a[0])

    window = Toplevel()
    window.geometry("400x400")
    window.configure(background="#3c4f55")

    listbox3 = Listbox(window, selectmode="extended", width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff')
    for drink in drinklist:
        listbox3.insert(END, drink)
    listbox3.pack()

    button_drink = Button(window,text="Detail", relief='groove',  width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff',command=clicked) #Detail 버튼 제공
    button_drink.pack()

    randombtn=Button(window,text="Random", relief='groove',  width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff',command=rd) #Random 버튼 제공
    randombtn.pack()

    how=Label(window, text="When you click 'Detail' button, please choose one. \n Click 'Random' if you can't choose :-)", width=70, bg='#3c4f55', font=("나눔고딕", 10), fg='#ffffff')
    how.pack()

    main_map = folium.Map(location=[37.508077, 126.960482], zoom_start=30)
    
    for i in range(0, len(drink_place)):
        folium.Marker([drink_place.iloc[i]['lon'], drink_place.iloc[i]['lat']],
                      popup=drink_place.iloc[i]['name'],
                      icon=folium.Icon(color='darkblue', icon='glass')).add_to(main_map)

    main_map.save('CAU_map.html')
    f = webbrowser.open('CAU_map.html')


def Meallist():# Meal, Dessert, Drink, Vegeterian 중 Meal 선택

    window2.withdraw()
    meallist = [] #저장 리스트 초기화
    
    def clicked(): #Detail 버튼이 클릭되었을 때 실행되는 함수 
        doublelist = []
        curselect = listbox1.curselection() #리스트박스에서 선택된 값을 저장

        
        for a in csvlist: # csvlist에 저장했던 딕셔너리의 name키에 해당하는 value값이 
            if a["name"]==listbox1.get(curselect): # listbox에서 선택된 값과 csvlist에 저장했던 각 딕셔너리의 name키에 해당하는 value값을 비교해서
                #가게이름, 메인메뉴, 매운정도, 오픈시간, 고기재료의 종류 정보를 가져와서 doublelist에 저장한다. 
                doublelist.append(a["name"])
                doublelist.append(a["main menu"])
                doublelist.append(a["spicy"])
                doublelist.append(a["open"])
                doublelist.append(a["preference"])

 
        #새 윈도우를 띄워서 선택된 가게 맞춤 디테일 정보 제공
        window_detail = Toplevel() # 디테일 정보 제공을  위한 새 창
        window_detail.title("Information")
        window_detail.geometry("400x400")
        window_detail.configure(background="#3c4f55")


        text_detail = Text(window_detail,width=60, height=65, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff' ) #doublelist에 저장된 값들을 Text창에 띄운다
        text_detail.insert(1.0, doublelist[0]+"\n")
        text_detail.insert(2.0,"Main Menu: "+doublelist[1]+"\n") #메인메뉴?
        text_detail.insert(3.0,"Spicy?: "+doublelist[2]+"\n") #매운지?
        text_detail.insert(4.0,"Open: "+doublelist[3]+"\n") #오픈시간은?
        text_detail.insert(5.0,"Preference: "+doublelist[4]) # 고기재료의 종류?
   
        text_detail.pack()

    def rd():
        randomlist=[]
        random2 = random.randint(0,len(meallist)-1) #랜덤값 오류없이 조정
       
        for a in csvlist:
            if a["name"]==meallist[random2]:
                randomlist.append(a["name"])
                randomlist.append(a["main menu"])
                randomlist.append(a["spicy"])
                randomlist.append(a["open"])
                randomlist.append(a["preference"])

        
        #새 윈도우를 띄워서 선택된 가게 맞춤 디테일 정보 제공
        window_detail = Toplevel() # 디테일 정보 제공을  위한 새 창
        window_detail.title("Information")
        window_detail.geometry("400x400")
        window_detail.configure(background="#3c4f55")

        text_detail = Text(window_detail,width=60, height=65, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff' ) #randomlist에 저장된 값들을 Text창에 띄운다
        text_detail.insert(1.0, randomlist[0]+"\n") #가게이름?
        text_detail.insert(2.0,"Main Menu: "+randomlist[1]+"\n") #메인메뉴?
        text_detail.insert(3.0,"Spicy?: "+randomlist[2]+"\n") #매운지?
        text_detail.insert(4.0,"Open: "+randomlist[3]+"\n") #오픈시간은?
        text_detail.insert(5.0,"Preference: "+randomlist[4]) # 고기재료의 종류?

        text_detail.pack()
                                  
    
    if mealtype1.get() == 1:
        for a in csvlist:
            if a["category"] == "Korean-food":
                meallist.append(a["name"])

    if mealtype2.get() == 1:
        for b in csvlist:
            if b["category"] == "Chinese-food":
                meallist.append(b["name"])

    if mealtype3.get() == 1:
        for c in csvlist:
            if c["category"] == "Japanese-food":
                meallist.append(c["name"])
    
    window = Toplevel()
    window.geometry("400x400")
    window.configure(background="#3c4f55")

    listbox1 = Listbox(window, selectmode="extended", width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff')
    for meal in meallist:
        listbox1.insert(END, meal)

    listbox1.pack()
    window3.withdraw()
    
    button_meal = Button(window,text="Detail", relief='groove',  width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff',command=clicked) #Detail 버튼 제공
    button_meal.pack()

    randombtn=Button(window,text="Random", relief='groove',  width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff',command=rd) #Random 버튼 제공
    randombtn.pack()

    how=Label(window, text="WWhen you click 'Detail' button, please choose one. \n Click 'Random' if you can't choose :-)", width=70, bg='#3c4f55', font=("나눔고딕", 10), fg='#ffffff')
    how.pack()

    main_map = folium.Map(location=[37.508077, 126.960482], zoom_start=30) #지도 마커 초기화
    
    if mealtype1.get()==1: #한식
        for i in range(0, len(korean_place)):
            folium.Marker([korean_place.iloc[i]['lon'], korean_place.iloc[i]['lat']],
                          popup=korean_place.iloc[i]['name'],
                          icon=folium.Icon(color='blue', icon='flag')).add_to(main_map)

    if mealtype2.get()==1: #중식
        for i in range(0, len(chinese_place)):
            folium.Marker([chinese_place.iloc[i]['lon'], chinese_place.iloc[i]['lat']],
                          popup=chinese_place.iloc[i]['name'],
                          icon=folium.Icon(color='red', icon='flag')).add_to(main_map)

    if mealtype3.get()==1: #일식
        for i in range(0, len(japanese_place)):
            folium.Marker([japanese_place.iloc[i]['lon'], japanese_place.iloc[i]['lat']],
                          popup=japanese_place.iloc[i]['name'],
                          icon=folium.Icon(color='gray', icon='flag')).add_to(main_map)

    main_map.save('CAU_map.html')

    f = webbrowser.open('CAU_map.html')
    

def Vege():# Meal, Dessert, Drink, Vegeterian 중 Vegeterian 선택

    window2.withdraw()
    
    vegelist = [] #리스트 초기화
    
    def clicked(): #Detail 버튼이 클릭되었을 때 실행되는 함수 
        doublelist = []
        curselect = listbox4.curselection() #리스트박스에서 선택된 값을 저장

        
        for a in csvlist: # csvlist에 저장했던 딕셔너리의 name키에 해당하는 value값이 
            if a["name"]==listbox4.get(curselect): # listbox에서 선택된 값과 csvlist에 저장했던 각 딕셔너리의 name키에 해당하는 value값을 비교해서
                #가게이름, 메인메뉴, 매운정도, 오픈시간, 고기재료의 종류 정보를 가져와서 doublelist에 저장한다. 
                doublelist.append(a["name"])
                doublelist.append(a["main menu"])
                doublelist.append(a["spicy"])
                doublelist.append(a["open"])
                doublelist.append(a["preference"])

 
        #새 윈도우를 띄워서 선택된 가게 맞춤 디테일 정보 제공
        window_detail = Toplevel() # 디테일 정보 제공을  위한 새 창
        window_detail.title("Information")
        window_detail.geometry("400x400")
        window_detail.configure(background="#3c4f55")


        text_detail = Text(window_detail,width=60, height=65, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff' ) #doublelist에 저장된 값들을 Text창에 띄운다
        text_detail.insert(1.0, doublelist[0]+"\n")
        text_detail.insert(2.0,"Main Menu: "+doublelist[1]+"\n") #메인메뉴?
        text_detail.insert(3.0,"Spicy?: "+doublelist[2]+"\n") #매운지?
        text_detail.insert(4.0,"Open: "+doublelist[3]+"\n") #오픈시간은?
        text_detail.insert(5.0,"Preference: "+doublelist[4]) # 고기재료의 종류?
   
        text_detail.pack()



    def rd():
        randomlist=[]
        random2 = random.randint(0,len(vegelist)-1) #랜덤값 오류없이 조정
       
        for a in csvlist:
            if a["name"]==vegelist[random2]:
                randomlist.append(a["name"])
                randomlist.append(a["main menu"])
                randomlist.append(a["spicy"])
                randomlist.append(a["open"])
                randomlist.append(a["preference"])

        
        #새 윈도우를 띄워서 선택된 가게 맞춤 디테일 정보 제공
        window_detail = Toplevel() # 디테일 정보 제공을  위한 새 창
        window_detail.title("Information")
        window_detail.geometry("400x400")
        window_detail.configure(background="#3c4f55")

        text_detail = Text(window_detail,width=60, height=65, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff' ) #randomlist에 저장된 값들을 Text창에 띄운다
        text_detail.insert(1.0, randomlist[0]+"\n") #가게이름?
        text_detail.insert(2.0,"Main Menu: "+randomlist[1]+"\n") #메인메뉴?
        text_detail.insert(3.0,"Spicy?: "+randomlist[2]+"\n") #매운지?
        text_detail.insert(4.0,"Open: "+randomlist[3]+"\n") #오픈시간은?
        text_detail.insert(5.0,"Preference: "+randomlist[4]) # 고기재료의 종류?

        text_detail.pack()

                                  
    with open("Rest_info.csv", mode="r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for a in reader:
            if a[1] == "Vege":
                vegelist.append(a[0])

    window = Toplevel()
    window.geometry("400x400")
    window.configure(background="#3c4f55")

    listbox4 = Listbox(window, selectmode='extended', width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff')
    for vege in vegelist:
        listbox4.insert(END, vege)

    listbox4.pack()

    button_drink = Button(window,text="Detail", relief='groove',  width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff',command=clicked) #Detail 버튼 제공
    button_drink.pack()

    randombtn=Button(window,text="Random", relief='groove',  width=40, bg='#3c4f55', font=("Arial Bold", 15), fg='#ffffff',command=rd) #Random 버튼 제공
    randombtn.pack()   

    how=Label(window, text="When you click 'Detail' button, please choose one. \n Click 'Random' if you can't choose :-)", width=70, bg='#3c4f55', font=("나눔고딕", 10), fg='#ffffff')
    how.pack()

 

    main_map = folium.Map(location=[37.508077, 126.960482], zoom_start=30) #지도 초기화
    
    for i in range(0, len(vegeterian_place)): #지도상에 좌표를 찍음
        folium.Marker([vegeterian_place.iloc[i]['lon'], vegeterian_place.iloc[i]['lat']],
                      popup=vegeterian_place.iloc[i]['name'],
                      icon=folium.Icon(color='green', icon='star')).add_to(main_map)

    main_map.save('CAU_map.html')
    f = webbrowser.open('CAU_map.html')



window1 = Tk() #가장 첫 번째 윈도우 (start 버튼과 quit 버튼 존재)
window1.title("Restaurant Recommendation")
window1.configure(background='#3c4f55')
window1.geometry("500x400")


lbl = Label(window1,text="CAU Restaurant\n Recommendation ",font=("Arial Bold",40), bg='#8bcbc8',fg='#ffffff')
lbl.place(x=11, y=70)

startbtn = Button(window1, text=" START!", font=("Arial Bold",33), bg='#3c4f55',fg='#ffffff', command=Start)
startbtn.place(x=145,y=235) #스타트버튼
quitbtn = Button(window1,text="Quit",font=("Arial Bold",20), width=12, bg='#3c4f55',fg='#ffffff', command=Bye)
quitbtn.place(x=145,y=330) #종료버튼


window2 = Toplevel() #두 번째 윈도우 (음식 장르 선택)
window2.title("Food Preference")
window2.withdraw() #감춰두었다가 버튼 클릭시 동작
window2.configure(background='#3c4f55')
window2.geometry("500x400")

lb2=Label(window2, text="What do you want to eat?", font=("Arial Bold", 20), bg='#3c4f55',fg='#ebeced')
meal = Button(window2, text="Meal",width=30,  font=("Arial Bold",15), bd=5, bg='#dae9e4', command=Meal)
dessert = Button(window2, text="Dessert", width=30, font=("Arial Bold",15), bd=5, bg='#8bcbc8', command=Dessert)
drink = Button(window2, text="Drink",width=30, font=("Arial Bold",15), bd=5, bg='#ecc7c0', command=Drink)
vege= Button(window2, text="Vegeterian", width=30, font=("Arial Bold",15), bd=5, bg='#fdae84', command=Vege)

lb2.place(x=10, y=10)
meal.place(x=70,y=100)
dessert.place(x=70,y=170)
drink.place(x=70,y=240)
vege.place(x=70, y=310)


window3 = Toplevel() # Meal을 선택했을 때 나오는 윈도우 (체크버튼)
window3.title("pg2")
window3.withdraw() #감춰두었다가 버튼 클릭 시 동작
window3.geometry("500x400")
window3.configure(background='#3c4f55')


lb2=Label(window3, text="What do you want to eat?", font=("Arial Bold", 20), bg='#3c4f55',fg='#cbc5c1')
mealtype1 = IntVar() # 체크버튼 카운트를 위해 사용
mealtype2 = IntVar()
mealtype3 = IntVar()
korean = Checkbutton(window3, text="Korean food", font=("Arial Bold",20), bg='#e7baa0', variable=mealtype1)
chinese = Checkbutton(window3, text="Chinese food", font=("Arial Bold",20), bg='#e7baa0', variable=mealtype2)
japanese = Checkbutton(window3, text="Japanese food", font=("Arial Bold",20), bg='#e7baa0', variable=mealtype3)
completebtn = Button(window3, text="Done", width=20, font=("Arial Bold",15), bg='#e7baa0', command=Meallist)

lb2.place(x=10, y=10)
korean.place(x=150, y=70)
chinese.place(x=143, y=140)
japanese.place(x=135, y=210)
completebtn.place(x=125, y=300)


meallist = [] #사용되는 리스트들
dessertlist = []
drinklist = []
vegelist=[]
doublelist=[]

window1.mainloop()
