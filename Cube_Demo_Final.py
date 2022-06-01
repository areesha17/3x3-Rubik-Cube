from tkinter import *
#from tkinter.ttk import*
from time import strftime


master = Tk()
frame1 = Frame(master)
frame1.grid()
master.title('Cube')

master.state('zoomed')


def change_color():
    pass
#########RED################################

Button_left = Button(master, text = '',height = 4, width = 3, background = 'Green', bd = 4)
Button_left.grid(row=2, column = 0)

Button_right = Button(master, text = '', height = 4, width = 3, bg = 'Blue', bd = 4)
Button_right.grid(row =2, column = 4)

Button_top = Button(master, text = '', height = 1, width = 10, bg = 'White', bd = 4)
Button_top.grid(row = 0, column = 2)

Button_bottom = Button(master, text = '', height = 1, width = 10, bg = 'Yellow', bd = 4)
Button_bottom.grid(row = 4, column = 2)

Button_dist = Button(master, text = '', height = 0, width = 10, bd = 0)
Button_dist.grid(row = 2, column = 5)

Button1 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = 'Red', bd = 7)
Button1.grid(row=1, column=1)

Button2 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Red", bd = 7)
Button2.grid(row=1, column=2)

Button3 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Red", bd = 7)
Button3.grid(row=1, column=3)


Button4 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Red", bd = 7)
Button4.grid(row=2, column=1)

Button5 = Button(master, text="FRONT",height = 4 ,width = 10, command=change_color,fg = 'Black', bg = "Red", bd = 7)
Button5.grid(row=2, column=2)

Button6 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Red", bd = 7)
Button6.grid(row=2, column=3)

Button7 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Red", bd = 7)
Button7.grid(row=3, column=1)

Button8 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Red", bd = 7)
Button8.grid(row=3, column=2)

Button9 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Red", bd = 7)
Button9.grid(row=3, column=3)


#################BLUE#########################

Button_left1 = Button(master, text = '', height = 4, width = 3, bg = 'Red', bd = 4)
Button_left1.grid(row=2, column = 6)

Button_right1 = Button(master, text = '', height = 4, width = 3, bg = 'Orange', bd = 4)
Button_right1.grid(row =2, column = 10)

Button_top1 = Button(master, text = '', height = 1, width = 10, bg = 'White', bd = 4)
Button_top1.grid(row = 0, column = 8)

Button_bottom1 = Button(master, text = '', height = 1, width = 10, bg = 'Yellow', bd = 4)
Button_bottom1.grid(row = 4, column = 8)

Button10 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Blue", bd = 7)
Button10.grid(row=1, column=7)

Button11 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Blue", bd = 7)
Button11.grid(row=1, column=8)

Button12 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Blue", bd = 7)
Button12.grid(row=1, column=9)


Button13 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Blue", bd = 7)
Button13.grid(row=2, column=7)

Button14 = Button(master, text="RIGHT",height = 4 ,width = 10, fg = 'Black', command=change_color, bg = "Blue", bd = 7)
Button14.grid(row=2, column=8)

Button15 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Blue", bd = 7)
Button15.grid(row=2, column=9)

Button16 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Blue", bd = 7)
Button16.grid(row=3, column=7)

Button17 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Blue", bd = 7)
Button17.grid(row=3, column=8)

Button18 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Blue", bd = 7)
Button18.grid(row=3, column=9)

Button_dist1 = Button(master, text = '', height = 0, width = 10, bd = 0)
Button_dist1.grid(row = 2, column = 11)


########################


Button_dist2 = Button(master, height = 5, width = 0, bd = 0)
Button_dist2.grid(row = 5, column = 1)

########################GREEN###########################


Button_left2 = Button(master, text = '', height = 4, width = 3, bg = 'Orange', bd = 4)
Button_left2.grid(row=2, column = 13)

Button_right2 = Button(master, text = '', height = 4, width = 3, bg = 'Red', bd = 4)
Button_right2.grid(row =2, column = 17)

Button_top2 = Button(master, text = '', height = 1, width = 10, bg = 'White', bd = 4)
Button_top2.grid(row = 0, column = 15)

Button_bottom2 = Button(master, text = '', height = 1, width = 10, bg = 'Yellow', bd = 4)
Button_bottom2.grid(row = 4, column = 15)

Button19 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Green", bd = 7)
Button19.grid(row=1, column=14)

Button20 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Green", bd = 7)
Button20.grid(row=1, column=15)

Button21 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Green", bd = 7)
Button21.grid(row=1, column=16)


Button22 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Green", bd = 7)
Button22.grid(row=2, column=14)

Button23 = Button(master, text="LEFT",fg = 'Black', height = 4 ,width = 10, command=change_color, bg = "Green", bd = 7)
Button23.grid(row=2, column=15)

Button24 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Green", bd = 7)
Button24.grid(row=2, column=16)

Button25 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Green", bd = 7)
Button25.grid(row=3, column=14)

Button26 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Green", bd = 7)
Button26.grid(row=3, column=15)

Button27 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Green", bd = 7)
Button27.grid(row=3, column=16)


########################ORANGE###################

Button_left3 = Button(master, text = '', height = 4, width = 3, bg = 'Blue', bd = 4)
Button_left3.grid(row=8, column = 0)

Button_right3 = Button(master, text = '', height = 4, width = 3, bg = 'Green', bd = 4)
Button_right3.grid(row =8, column = 4)

Button_top3 = Button(master, text = '', height = 1, width = 10, bg = 'White', bd = 4)
Button_top3.grid(row = 6, column = 2)

Button_bottom3 = Button(master, text = '', height = 1, width = 10, bg = 'Yellow', bd = 4)
Button_bottom3.grid(row = 10, column = 2)

Button28 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Orange", bd = 7)
Button28.grid(row=7, column=1)

Button29 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Orange", bd = 7)
Button29.grid(row=7, column=2)

Button30 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Orange", bd = 7)
Button30.grid(row=7, column=3)


Button31 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Orange", bd = 7)
Button31.grid(row=8, column=1)

Button32 = Button(master, text="BACK", fg = 'Black', height = 4 ,width = 10, command=change_color, bg = "Orange", bd = 7)
Button32.grid(row=8, column=2)

Button33 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Orange", bd = 7)
Button33.grid(row=8, column=3)

Button34 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Orange", bd = 7)
Button34.grid(row=9, column=1)

Button35 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Orange", bd = 7)
Button35.grid(row=9, column=2)

Button36 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Orange", bd = 7)
Button36.grid(row=9, column=3)

#############################WHITE###############################


Button_left4 = Button(master, text = '', height = 4, width = 3, bg = 'Green', bd = 4)
Button_left4.grid(row=8, column = 6)

Button_right4 = Button(master, text = '', height = 4, width = 4, bg = 'Blue', bd = 4)
Button_right4.grid(row =8, column = 10)

Button_top4 = Button(master, text = '', height = 1, width = 10, bg = 'Orange', bd = 4)
Button_top4.grid(row = 6, column = 8)

Button_bottom4 = Button(master, text = '', height = 1, width = 10, bg = 'Red', bd = 4)
Button_bottom4.grid(row = 10, column = 8)

Button37 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "White", bd = 7)
Button37.grid(row=7, column=7)

Button38 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "White", bd = 7)
Button38.grid(row=7, column=8)

Button39 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "White", bd = 7)
Button39.grid(row=7, column=9)


Button40 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "White", bd = 7)
Button40.grid(row=8, column=7)

Button41 = Button(master, text="TOP",height = 4 ,width = 10, fg = 'Black', command = change_color, bg = "White", bd = 7)
Button41.grid(row=8, column=8)

Button42 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "White", bd = 7)
Button42.grid(row=8, column=9)

Button43 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "White", bd = 7)
Button43.grid(row=9, column=7)

Button44 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "White", bd = 7)
Button44.grid(row=9, column=8)

Button45 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "White", bd = 7)
Button45.grid(row=9, column=9)

############################YELLOW######################


Button_left5 = Button(master, text = '', height = 4, width = 3, bg = 'Green', bd = 4)
Button_left5.grid(row=8, column = 13)

Button_right5 = Button(master, text = '', height = 4, width = 3, bg = 'Blue', bd = 4)
Button_right5.grid(row =8, column = 17)

Button_top5 = Button(master, text = '', height = 1, width = 10, bg = 'Red', bd = 4)
Button_top5.grid(row = 6, column = 15)

Button_bottom5 = Button(master, text = '', height = 1, width = 10, bg = 'Orange', bd = 4)
Button_bottom5.grid(row = 10, column = 15)

Button46 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Yellow", bd = 7)
Button46.grid(row=7, column=14)

Button47 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Yellow", bd = 7)
Button47.grid(row=7, column=15)

Button48 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Yellow", bd = 7)
Button48.grid(row=7, column=16)


Button49 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Yellow", bd = 7)
Button49.grid(row=8, column=14)

Button50 = Button(master, text="BOTTOM", fg = 'Black', height = 4 ,width = 10, command=change_color, bg = "Yellow", bd = 7)
Button50.grid(row=8, column=15)

Button51 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Yellow", bd = 7)
Button51.grid(row=8, column=16)

Button52 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Yellow", bd = 7)
Button52.grid(row=9, column=14)

Button53 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Yellow", bd = 7)
Button53.grid(row=9, column=15)

Button54 = Button(master, text="",height = 4 ,width = 10, command=change_color, bg = "Yellow", bd = 7)
Button54.grid(row=9, column=16)


##########################THIS IS FOR COLOR CHANGING LABEL WHICH IS ON EVERY BUTTON##########################

color_list = Listbox(master, height = 1, width = 7)
color_list.insert(1, 'Red')
color_list.insert(2,'Yellow')
color_list.insert(3,'Blue')
color_list.insert(4,'Green')
color_list.insert(5,'White')
color_list.insert(6,'Orange')
color_list.grid(row = 1, column = 1)


color_list1 = Listbox(master, height = 1, width = 7)
color_list1.insert(1, 'Red')
color_list1.insert(2,'Yellow')
color_list1.insert(3,'Blue')
color_list1.insert(4,'Green')
color_list1.insert(5,'White')
color_list1.insert(6,'Orange')
color_list1.grid(row = 1, column = 2)


color_list2 = Listbox(master, height = 1, width = 7)
color_list2.insert(1, 'Red')
color_list2.insert(2,'Yellow')
color_list2.insert(3,'Blue')
color_list2.insert(4,'Green')
color_list2.insert(5,'White')
color_list2.insert(6,'Orange')
color_list2.grid(row = 1, column = 3)


color_list3 = Listbox(master, height = 1, width = 7)
color_list3.insert(1, 'Red')
color_list3.insert(2,'Yellow')
color_list3.insert(3,'Blue')
color_list3.insert(4,'Green')
color_list3.insert(5,'White')
color_list3.insert(6,'Orange')
color_list3.grid(row = 2, column = 1)

color_list4 = Listbox(master, height = 1, width = 7)
color_list4.insert(1, 'Red')
color_list4.insert(2,'Yellow')
color_list4.insert(3,'Blue')
color_list4.insert(4,'Green')
color_list4.insert(5,'White')
color_list4.insert(6,'Orange')
color_list4.grid(row = 2, column = 3)


color_list5 = Listbox(master, height = 1, width = 7)
color_list5.insert(1, 'Red')
color_list5.insert(2,'Yellow')
color_list5.insert(3,'Blue')
color_list5.insert(4,'Green')
color_list5.insert(5,'White')
color_list5.insert(6,'Orange')
color_list5.grid(row = 3, column = 1)


color_list6 = Listbox(master, height = 1, width = 7)
color_list6.insert(1, 'Red')
color_list6.insert(2,'Yellow')
color_list6.insert(3,'Blue')
color_list6.insert(4,'Green')
color_list6.insert(5,'White')
color_list6.insert(6,'Orange')
color_list6.grid(row = 3, column = 2)


color_list7 = Listbox(master, height = 1, width = 7)
color_list7.insert(1, 'Red')
color_list7.insert(2,'Yellow')
color_list7.insert(3,'Blue')
color_list7.insert(4,'Green')
color_list7.insert(5,'White')
color_list7.insert(6,'Orange')
color_list7.grid(row = 3, column = 3)


color_list8 = Listbox(master, height = 1, width = 7)
color_list8.insert(3,'Blue')
color_list8.insert(1, 'Red')
color_list8.insert(2,'Yellow')
color_list8.insert(4,'Green')
color_list8.insert(5,'White')
color_list8.insert(6,'Orange')
color_list8.grid(row = 1, column = 7)


color_list9 = Listbox(master, height = 1, width = 7)
color_list9.insert(3,'Blue')
color_list9.insert(1, 'Red')
color_list9.insert(2,'Yellow')
color_list9.insert(4,'Green')
color_list9.insert(5,'White')
color_list9.insert(6,'Orange')
color_list9.grid(row = 1, column = 8)


color_list10 = Listbox(master, height = 1, width = 7)
color_list10.insert(3,'Blue')
color_list10.insert(1, 'Red')
color_list10.insert(2,'Yellow')
color_list10.insert(4,'Green')
color_list10.insert(5,'White')
color_list10.insert(6,'Orange')
color_list10.grid(row = 1, column = 9)


color_list11 = Listbox(master, height = 1, width = 7)
color_list11.insert(3,'Blue')
color_list11.insert(1, 'Red')
color_list11.insert(2,'Yellow')
color_list11.insert(4,'Green')
color_list11.insert(5,'White')
color_list11.insert(6,'Orange')
color_list11.grid(row = 2, column = 7)


color_list12 = Listbox(master, height = 1, width = 7)
color_list12.insert(3,'Blue')
color_list12.insert(1, 'Red')
color_list12.insert(2,'Yellow')
color_list12.insert(4,'Green')
color_list12.insert(5,'White')
color_list12.insert(6,'Orange')
color_list12.grid(row = 2, column = 9)


color_list13 = Listbox(master, height = 1, width = 7)
color_list13.insert(3,'Blue')
color_list13.insert(1, 'Red')
color_list13.insert(2,'Yellow')
color_list13.insert(4,'Green')
color_list13.insert(5,'White')
color_list13.insert(6,'Orange')
color_list13.grid(row = 3, column = 7)


color_list14 = Listbox(master, height = 1, width = 7)
color_list14.insert(3,'Blue')
color_list14.insert(1, 'Red')
color_list14.insert(2,'Yellow')
color_list14.insert(4,'Green')
color_list14.insert(5,'White')
color_list14.insert(6,'Orange')
color_list14.grid(row = 3, column = 8)


color_list15 = Listbox(master, height = 1, width = 7)
color_list15.insert(3,'Blue')
color_list15.insert(1, 'Red')
color_list15.insert(2,'Yellow')
color_list15.insert(4,'Green')
color_list15.insert(5,'White')
color_list15.insert(6,'Orange')
color_list15.grid(row = 3, column = 9)

color_list18 = Listbox(master, height = 1, width = 7)
color_list18.insert(4,'Green')
color_list18.insert(1, 'Red')
color_list18.insert(2,'Yellow')
color_list18.insert(3,'Blue')
color_list18.insert(5,'White')
color_list18.insert(6,'Orange')
color_list18.grid(row = 1, column = 14)


color_list19 = Listbox(master, height = 1, width = 7)
color_list19.insert(4,'Green')
color_list19.insert(1, 'Red')
color_list19.insert(2,'Yellow')
color_list19.insert(3,'Blue')
color_list19.insert(5,'White')
color_list19.insert(6,'Orange')
color_list19.grid(row = 1, column = 15)


color_list20 = Listbox(master, height = 1, width = 7)
color_list20.insert(4,'Green')
color_list20.insert(1, 'Red')
color_list20.insert(2,'Yellow')
color_list20.insert(3,'Blue')
color_list20.insert(5,'White')
color_list20.insert(6,'Orange')
color_list20.grid(row = 1, column = 16)

color_list22 = Listbox(master, height = 1, width = 7)
color_list22.insert(4,'Green')
color_list22.insert(1, 'Red')
color_list22.insert(2,'Yellow')
color_list22.insert(3,'Blue')
color_list22.insert(5,'White')
color_list22.insert(6,'Orange')
color_list22.grid(row = 2, column = 14)


color_list23 = Listbox(master, height = 1, width = 7)
color_list23.insert(4,'Green')
color_list23.insert(1, 'Red')
color_list23.insert(2,'Yellow')
color_list23.insert(3,'Blue')
color_list23.insert(5,'White')
color_list23.insert(6,'Orange')
color_list23.grid(row = 2, column = 16)


color_list24 = Listbox(master, height = 1, width = 7)
color_list24.insert(4,'Green')
color_list24.insert(1, 'Red')
color_list24.insert(2,'Yellow')
color_list24.insert(3,'Blue')
color_list24.insert(5,'White')
color_list24.insert(6,'Orange')
color_list24.grid(row = 3, column = 14)


color_list25 = Listbox(master, height = 1, width = 7)
color_list25.insert(4,'Green')
color_list25.insert(1, 'Red')
color_list25.insert(2,'Yellow')
color_list25.insert(3,'Blue')
color_list25.insert(5,'White')
color_list25.insert(6,'Orange')
color_list25.grid(row = 3, column = 15)


color_list26 = Listbox(master, height = 1, width = 7)
color_list26.insert(4,'Green')
color_list26.insert(1, 'Red')
color_list26.insert(2,'Yellow')
color_list26.insert(3,'Blue')
color_list26.insert(5,'White')
color_list26.insert(6,'Orange')
color_list26.grid(row = 3, column = 16)


color_list27 = Listbox(master, height = 1, width = 7)
color_list27.insert(6,'Orange')
color_list27.insert(1, 'Red')
color_list27.insert(2,'Yellow')
color_list27.insert(3,'Blue')
color_list27.insert(4,'Green')
color_list27.insert(5,'White')
color_list27.grid(row = 7, column = 1)


color_list28 = Listbox(master, height = 1, width = 7)
color_list28.insert(6,'Orange')
color_list28.insert(1, 'Red')
color_list28.insert(2,'Yellow')
color_list28.insert(3,'Blue')
color_list28.insert(4,'Green')
color_list28.insert(5,'White')
color_list28.grid(row = 7, column = 2)


color_list30 = Listbox(master, height = 1, width = 7)
color_list30.insert(6,'Orange')
color_list30.insert(1, 'Red')
color_list30.insert(2,'Yellow')
color_list30.insert(3,'Blue')
color_list30.insert(4,'Green')
color_list30.insert(5,'White')
color_list30.grid(row = 7, column = 3)


color_list31 = Listbox(master, height = 1, width =7)
color_list31.insert(6,'Orange')
color_list31.insert(1, 'Red')
color_list31.insert(2,'Yellow')
color_list31.insert(3,'Blue')
color_list31.insert(4,'Green')
color_list31.insert(5,'White')
color_list31.grid(row = 8, column = 1)


color_list32 = Listbox(master, height = 1, width = 7)
color_list32.insert(6,'Orange')
color_list32.insert(1, 'Red')
color_list32.insert(2,'Yellow')
color_list32.insert(3,'Blue')
color_list32.insert(4,'Green')
color_list32.insert(5,'White')
color_list32.grid(row = 8, column = 3)


color_list33 = Listbox(master, height = 1, width = 7)
color_list33.insert(6,'Orange')
color_list33.insert(1, 'Red')
color_list33.insert(2,'Yellow')
color_list33.insert(3,'Blue')
color_list33.insert(4,'Green')
color_list33.insert(5,'White')
color_list33.grid(row = 9, column = 1)


color_list34 = Listbox(master, height = 1, width = 7)
color_list34.insert(6,'Orange')
color_list34.insert(1, 'Red')
color_list34.insert(2,'Yellow')
color_list34.insert(3,'Blue')
color_list34.insert(4,'Green')
color_list34.insert(5,'White')
color_list34.grid(row = 9, column = 2)


color_list35 = Listbox(master, height = 1, width = 7)
color_list35.insert(6,'Orange')
color_list35.insert(1, 'Red')
color_list35.insert(2,'Yellow')
color_list35.insert(3,'Blue')
color_list35.insert(4,'Green')
color_list35.insert(5,'White')
color_list35.grid(row = 9, column = 3)


color_list36 = Listbox(master, height = 1, width = 7)
color_list36.insert(5,'White')
color_list36.insert(1, 'Red')
color_list36.insert(2,'Yellow')
color_list36.insert(3,'Blue')
color_list36.insert(4,'Green')
color_list36.insert(6,'Orange')
color_list36.grid(row = 7, column = 7)


color_list37 = Listbox(master, height = 1, width = 7)
color_list37.insert(5,'White')
color_list37.insert(1, 'Red')
color_list37.insert(2,'Yellow')
color_list37.insert(3,'Blue')
color_list37.insert(4,'Green')
color_list37.insert(6,'Orange')
color_list37.grid(row = 7, column = 8)


color_list38 = Listbox(master, height = 1, width = 7)
color_list38.insert(5,'White')
color_list38.insert(1, 'Red')
color_list38.insert(2,'Yellow')
color_list38.insert(3,'Blue')
color_list38.insert(4,'Green')
color_list38.insert(6,'Orange')
color_list38.grid(row = 7, column = 9)


color_list39 = Listbox(master, height = 1, width = 7)
color_list39.insert(5,'White')
color_list39.insert(1, 'Red')
color_list39.insert(2,'Yellow')
color_list39.insert(3,'Blue')
color_list39.insert(4,'Green')
color_list39.insert(6,'Orange')
color_list39.grid(row = 8, column = 7)


color_list40 = Listbox(master, height = 1, width = 7)
color_list40.insert(5,'White')
color_list40.insert(1, 'Red')
color_list40.insert(2,'Yellow')
color_list40.insert(3,'Blue')
color_list40.insert(4,'Green')
color_list40.insert(6,'Orange')
color_list40.grid(row = 8, column = 9)


color_list41 = Listbox(master, height = 1, width = 7)
color_list41.insert(5,'White')
color_list41.insert(1, 'Red')
color_list41.insert(2,'Yellow')
color_list41.insert(3,'Blue')
color_list41.insert(4,'Green')
color_list41.insert(6,'Orange')
color_list41.grid(row = 9, column = 7)


color_list42 = Listbox(master, height = 1, width = 7)
color_list42.insert(5,'White')
color_list42.insert(1, 'Red')
color_list42.insert(2,'Yellow')
color_list42.insert(3,'Blue')
color_list42.insert(4,'Green')
color_list42.insert(6,'Orange')
color_list42.grid(row = 9, column = 8)


color_list43 = Listbox(master, height = 1, width = 7)
color_list43.insert(5,'White')
color_list43.insert(1, 'Red')
color_list43.insert(2,'Yellow')
color_list43.insert(3,'Blue')
color_list43.insert(4,'Green')
color_list43.insert(6,'Orange')
color_list43.grid(row = 9, column = 9)


color_list44 = Listbox(master, height = 1, width = 7)
color_list44.insert(2,'Yellow')
color_list44.insert(1, 'Red')
color_list44.insert(3,'Blue')
color_list44.insert(4,'Green')
color_list44.insert(5,'White')
color_list44.insert(6,'Orange')
color_list44.grid(row = 7, column = 14)


color_list45 = Listbox(master, height = 1, width = 7)
color_list45.insert(2,'Yellow')
color_list45.insert(1, 'Red')
color_list45.insert(3,'Blue')
color_list45.insert(4,'Green')
color_list45.insert(5,'White')
color_list45.insert(6,'Orange')
color_list45.grid(row = 7, column = 15)


color_list46 = Listbox(master, height = 1, width = 7)
color_list46.insert(2,'Yellow')
color_list46.insert(1, 'Red')
color_list46.insert(3,'Blue')
color_list46.insert(4,'Green')
color_list46.insert(5,'White')
color_list46.insert(6,'Orange')
color_list46.grid(row = 7, column = 16)


color_list47 = Listbox(master, height = 1, width = 7)
color_list47.insert(2,'Yellow')
color_list47.insert(1, 'Red')
color_list47.insert(3,'Blue')
color_list47.insert(4,'Green')
color_list47.insert(5,'White')
color_list47.insert(6,'Orange')
color_list47.grid(row = 8, column = 14)


color_list48 = Listbox(master, height = 1, width = 7)
color_list48.insert(2,'Yellow')
color_list48.insert(1, 'Red')
color_list48.insert(3,'Blue')
color_list48.insert(4,'Green')
color_list48.insert(5,'White')
color_list48.insert(6,'Orange')
color_list48.grid(row = 8, column = 16)


color_list49 = Listbox(master, height = 1, width = 7)
color_list49.insert(2,'Yellow')
color_list49.insert(1, 'Red')
color_list49.insert(3,'Blue')
color_list49.insert(4,'Green')
color_list49.insert(5,'White')
color_list49.insert(6,'Orange')
color_list49.grid(row = 9, column = 14)


color_list50 = Listbox(master, height = 1, width = 7)
color_list50.insert(2,'Yellow')
color_list50.insert(1, 'Red')
color_list50.insert(3,'Blue')
color_list50.insert(4,'Green')
color_list50.insert(5,'White')
color_list50.insert(6,'Orange')
color_list50.grid(row = 9, column = 15)


color_list51 = Listbox(master, height = 1, width = 7)
color_list51.insert(2,'Yellow')
color_list51.insert(1, 'Red')
color_list51.insert(3,'Blue')
color_list51.insert(4,'Green')
color_list51.insert(5,'White')
color_list51.insert(6,'Orange')
color_list51.grid(row = 9, column = 16)

########################################


def read_colors():
    top_face = [value36, value37, value38, value39, 'White', value40, value41, value42, value43]
    right_face = [value8, value9, value10, value11, 'Blue', value12, value13, value14, value15]
    left_face = [value18, value19, value20, value22, 'Green', value23, value24, value25, value26]
    bottom_face = [value44, value45, value46, value47, 'Yellow', value48, value49, value50, value51]
    front_face = [value, value1, value2, value3, 'Red', value4, value5, value6, value7]
    back_face = [value27,value28,value30,value31,'Orange',value32,value33,value34,value35]

    global final_string
    final_string = ''
    final_list = [top_face, left_face[:3], front_face[:3], right_face[:3], back_face[:3], left_face[3:6], front_face[3:6], right_face[3:6],back_face[3:6], left_face[6:], front_face[6:], right_face[6:],back_face[6:], bottom_face]
    for a in final_list:
        for b in a:
            final_string += b[0].lower()
    master.destroy()


close_button = Button(master, text = 'DONE', command = read_colors, width = 10, bd = 6, height = 2 )###Done button
close_button.grid(row = 5, column = 8)


###############################THIS CHANGES THE COLOR OF THE BOX WHEN WE ARE SELECTING DIFFERENT COLORS#############################


while True:
    try:
        value = color_list.get('active')
        value1 = color_list1.get('active')
        value2 = color_list2.get('active')
        value3 = color_list3.get('active')
        value4 = color_list4.get('active')
        value5 = color_list5.get('active')
        value6 = color_list6.get('active')
        value7 = color_list7.get('active')
        value8 = color_list8.get('active')
        value9 = color_list9.get('active')
        value10 = color_list10.get('active')
        value11 = color_list11.get('active')
        value12 = color_list12.get('active')
        value13 = color_list13.get('active')
        value14 = color_list14.get('active')
        value15 = color_list15.get('active')
        # value16 = color_list16.get('active')
        # value17 = color_list17.get('active')
        value18 = color_list18.get('active')
        value19 = color_list19.get('active')
        value20 = color_list20.get('active')
        # value21 = color_list21.get('active')
        value22 = color_list22.get('active')
        value23 = color_list23.get('active')
        value24 = color_list24.get('active')
        value25 = color_list25.get('active')
        value26 = color_list26.get('active')
        value27 = color_list27.get('active')
        value28 = color_list28.get('active')
        # value29 = color_list29.get('active')
        value30 = color_list30.get('active')
        value31 = color_list31.get('active')
        value32 = color_list32.get('active')
        value33 = color_list33.get('active')
        value34 = color_list34.get('active')
        value35 = color_list35.get('active')
        value36 = color_list36.get('active')
        value37 = color_list37.get('active')
        value38 = color_list38.get('active')
        value39 = color_list39.get('active')
        value40 = color_list40.get('active')
        value41 = color_list41.get('active')
        value42 = color_list42.get('active')
        value43 = color_list43.get('active')
        value44 = color_list44.get('active')
        value45 = color_list45.get('active')
        value46 = color_list46.get('active')
        value47 = color_list47.get('active')
        value48 = color_list48.get('active')
        value49 = color_list49.get('active')
        value50 = color_list50.get('active')
        value51 = color_list51.get('active')

        Button1.config(bg = value)
        Button2.config(bg= value1)
        Button3.config(bg= value2)
        Button4.config(bg= value3)

        Button6.config(bg= value4)
        Button7.config(bg= value5)
        Button8.config(bg= value6)
        Button9.config(bg= value7)

        Button10.config(bg=value8)
        Button11.config(bg=value9)
        Button12.config(bg=value10)
        Button13.config(bg=value11)

        Button15.config(bg=value12)
        Button16.config(bg=value13)
        Button17.config(bg=value14)
        Button18.config(bg=value15)

        Button19.config(bg=value18) ## 16 and 17 are faulty
        Button20.config(bg=value19)
        Button21.config(bg=value20)
        Button22.config(bg=value22)

        Button24.config(bg=value23)
        Button25.config(bg=value24)
        Button26.config(bg=value25)
        Button27.config(bg=value26)

        Button28.config(bg=value27)
        Button29.config(bg=value28)
        Button30.config(bg=value30)
        Button31.config(bg=value31)

        Button33.config(bg=value32)
        Button34.config(bg=value33)
        Button35.config(bg=value34)
        Button36.config(bg=value35)

        Button37.config(bg=value36)
        Button38.config(bg=value37)
        Button39.config(bg=value38)
        Button40.config(bg=value39)

        Button42.config(bg=value40)
        Button43.config(bg=value41)
        Button44.config(bg=value42)
        Button45.config(bg=value43)

        Button46.config(bg=value44)
        Button47.config(bg=value45)
        Button48.config(bg=value46)
        Button49.config(bg=value47)

        Button51.config(bg=value48)
        Button52.config(bg=value49)
        Button53.config(bg=value50)
        Button54.config(bg=value51)


        master.update_idletasks()
        master.update()

    except:
        break


########## Layer By Layer Implementation ######

###Rotation_Functions###

def rotation(matrix, clockwise=True):
    m = [[None, None, None], [None, None, None], [None, None, None]]
    for x in range(3):
        for y in range(3):
            m[y][x] = matrix[x][y]
    if clockwise == True:
        for x in range(3):
            m[x] = m[x][::-1]
    else:
        m = m[::-1]
    return m


def U(matrix, ind, reverse=False):
    if ind == 0:
        s = 0
    elif ind == 2:
        s = 5
    if reverse == False:
        matrix[1][ind], matrix[2][ind], matrix[3][ind], matrix[4][ind] = matrix[4][ind], matrix[1][ind], matrix[2][ind], \
                                                                         matrix[3][ind]
    else:
        matrix[1][ind], matrix[2][ind], matrix[3][ind], matrix[4][ind] = matrix[2][ind], matrix[3][ind], matrix[4][ind], \
                                                                         matrix[1][ind]
    if (ind == 0 and reverse == False) or (ind == 2 and reverse == True):
        matrix[s] = rotation(matrix[s], False)
    elif (ind == 0 and reverse == True) or (ind == 2 and reverse == False):
        matrix[s] = rotation(matrix[s], True)
    return matrix


def V(matrix, ind, reverse=False):
    if ind == 0:
        s = 1
    elif ind == 2:
        s = 3
    for x in range(3):
        if reverse == True:
            matrix[0][x][ind], matrix[2][x][ind], matrix[5][x][ind], matrix[4][2 - x][2 - ind] = matrix[2][x][ind], \
                                                                                                 matrix[5][x][ind], \
                                                                                                 matrix[4][2 - x][
                                                                                                     2 - ind], \
                                                                                                 matrix[0][x][ind]
        else:
            matrix[0][x][ind], matrix[2][x][ind], matrix[5][x][ind], matrix[4][2 - x][2 - ind] = matrix[4][2 - x][
                                                                                                     2 - ind], \
                                                                                                 matrix[0][x][ind], \
                                                                                                 matrix[2][x][ind], \
                                                                                                 matrix[5][x][ind]
    if (ind == 0 and reverse == False) or (ind == 2 and reverse == True):
        matrix[s] = rotation(matrix[s], True)
    elif (ind == 0 and reverse == True) or (ind == 2 and reverse == False):
        matrix[s] = rotation(matrix[s], False)
    return matrix


def W(matrix, ind, reverse=False):  # ind is the index of row of white face which is rotating
    ind = 2 - ind
    if ind == 0:
        s = 4
    elif ind == 2:
        s = 2
    for x in range(3):
        if reverse == True:
            matrix[0][ind][x], matrix[3][x][2 - ind], matrix[5][2 - ind][2 - x], matrix[1][2 - x][ind] = \
            matrix[1][2 - x][ind], matrix[0][ind][x], matrix[3][x][2 - ind], matrix[5][2 - ind][2 - x]
        else:
            matrix[0][ind][x], matrix[3][x][2 - ind], matrix[5][2 - ind][2 - x], matrix[1][2 - x][ind] = matrix[3][x][
                                                                                                             2 - ind], \
                                                                                                         matrix[5][
                                                                                                             2 - ind][
                                                                                                             2 - x], \
                                                                                                         matrix[1][
                                                                                                             2 - x][
                                                                                                             ind], \
                                                                                                         matrix[0][ind][
                                                                                                             x]
    if (ind == 0 and reverse == False) or (ind == 2 and reverse == True):
        matrix[s] = rotation(matrix[s], True)
    elif (ind == 0 and reverse == True) or (ind == 2 and reverse == False):
        matrix[s] = rotation(matrix[s], False)
    return matrix


###Cube_Input_and_Formation###
import copy


def validity_formation(cube, cube_input, moves, states,indi):
    color_check = []
    for color in cube_input:
        if color not in color_check:
            color_check.append(color)
    indicator = True
    for each_color in color_check:
        if cube_input.count(each_color) == 9:
            pass
        else:
            indicator = False
            break
    if indicator:
        top_1_white = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        left_2_green = [9, 10, 11, 21, 22, 23, 33, 34, 35]
        front_3_red = [12, 13, 14, 24, 25, 26, 36, 37, 38]
        right_4_blue = [15, 16, 17, 27, 28, 29, 39, 40, 41]
        back_5_orange = [18, 19, 20, 30, 31, 32, 42, 43, 44]
        bottom_6_yellow = [45, 46, 47, 48, 49, 50, 51, 52, 53]
        initial_state = []
        initial_state.append(top_1_white)
        initial_state.append(left_2_green)
        initial_state.append(front_3_red)
        initial_state.append(right_4_blue)
        initial_state.append(back_5_orange)
        initial_state.append(bottom_6_yellow)
        ###
        temp1 = []
        temp2 = []
        count = 0
        for each_side in initial_state:
            for indexes in each_side:
                temp1.append(cube_input[indexes])
                count += 1
                if count == 3:
                    temp2.append(temp1)
                    count = 0
                    temp1 = []
            cube.append(temp2)
            temp2 = []
        states.append(copy.deepcopy(cube))
        moves.append('Initial State')
        return (cube, moves, states, indi)
    else:
        top_1_white = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        left_2_green = [9, 10, 11, 21, 22, 23, 33, 34, 35]
        front_3_red = [12, 13, 14, 24, 25, 26, 36, 37, 38]
        right_4_blue = [15, 16, 17, 27, 28, 29, 39, 40, 41]
        back_5_orange = [18, 19, 20, 30, 31, 32, 42, 43, 44]
        bottom_6_yellow = [45, 46, 47, 48, 49, 50, 51, 52, 53]
        initial_state = []
        initial_state.append(top_1_white)
        initial_state.append(left_2_green)
        initial_state.append(front_3_red)
        initial_state.append(right_4_blue)
        initial_state.append(back_5_orange)
        initial_state.append(bottom_6_yellow)
        ###
        temp1 = []
        temp2 = []
        count = 0
        for each_side in initial_state:
            for indexes in each_side:
                temp1.append(cube_input[indexes])
                count += 1
                if count == 3:
                    temp2.append(temp1)
                    count = 0
                    temp1 = []
            cube.append(temp2)
            temp2 = []
        indi=False
        moves.append('Invalid State')
        states.append(cube)
        return (cube, moves, states, indi)


#################
###First_layer###
#################

# First_layer_cross#
def top_layer_middle_piece(cube, moves, states, first_color, second_color):
    if cube[0][2][1] == first_color and cube[2][0][1] == second_color:
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[0][2][1] == second_color and cube[2][0][1] == first_color:
        # REQUIRED_ORIENTATION
        pass
    elif cube[0][1][0] == first_color and cube[1][0][1] == second_color:
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[0][1][0] == second_color and cube[1][0][1] == first_color:
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[0][0][1] == first_color and cube[4][0][1] == second_color:
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
    elif cube[0][0][1] == second_color and cube[4][0][1] == first_color:
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[0][1][2] == first_color and cube[3][0][1] == second_color:
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
    elif cube[0][1][2] == second_color and cube[3][0][1] == first_color:
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[2][1][0] == first_color and cube[1][1][2] == second_color:
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[2][1][0] == second_color and cube[1][1][2] == first_color:
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[1][1][0] == first_color and cube[4][1][2] == second_color:
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = W(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('W2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
    elif cube[1][1][0] == second_color and cube[4][1][2] == first_color:
        cube = W(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('W2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[4][1][0] == first_color and cube[3][1][2] == second_color:
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
    elif cube[4][1][0] == second_color and cube[3][1][2] == first_color:
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[3][1][0] == first_color and cube[2][1][2] == second_color:
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[3][1][0] == second_color and cube[2][1][2] == first_color:
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
    elif cube[5][0][1] == first_color and cube[2][2][1] == second_color:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
    elif cube[5][0][1] == second_color and cube[2][2][1] == first_color:
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[5][1][0] == first_color and cube[1][2][1] == second_color:
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
    elif cube[5][1][0] == second_color and cube[1][2][1] == first_color:
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[5][2][1] == first_color and cube[4][2][1] == second_color:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
    elif cube[5][2][1] == second_color and cube[4][2][1] == first_color:
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[5][1][2] == first_color and cube[3][2][1] == second_color:
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
    elif cube[5][1][2] == second_color and cube[3][2][1] == first_color:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    return (cube, moves, states)


def top_layer_cross(cube, moves, states):
    # For_red_white_piece_first
    cube, moves, states = top_layer_middle_piece(cube, moves, states, 'r', 'w')
    # For_green_white_piece_second
    moves.append('Rotate the Cube and Make the GREEN Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    cube, moves, states = top_layer_middle_piece(cube, moves, states, 'g', 'w')
    # For_orange_white_piece_third
    moves.append('Rotate the Cube and Make the ORANGE Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    cube, moves, states = top_layer_middle_piece(cube, moves, states, 'o', 'w')
    # For_blue_white_piece_fourth
    moves.append('Rotate the Cube and Make the BLUE Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    cube, moves, states = top_layer_middle_piece(cube, moves, states, 'b', 'w')
    #####
    moves.append('Rotate the Cube and Make the RED Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    moves.append('The Top-Layer-Cross should be complete')
    states.append(copy.deepcopy(cube))
    return (cube, moves, states)


# First_layer_corners#

def top_layer_corners_solver(cube, moves, states, color_1, color_2, color_3):
    if cube[0][2][0] == color_1 and cube[2][0][0] == color_2 and cube[1][0][2] == color_3:
        # REQUIRED_ORIENTATION
        pass
    elif cube[0][2][0] == color_3 and cube[2][0][0] == color_1 and cube[1][0][2] == color_2:
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[0][2][0] == color_2 and cube[2][0][0] == color_3 and cube[1][0][2] == color_1:
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[0][0][0] == color_1 and cube[1][0][0] == color_2 and cube[4][0][2] == color_3:
        cube = W(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('W2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[0][0][0] == color_3 and cube[1][0][0] == color_1 and cube[4][0][2] == color_2:
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[0][0][0] == color_2 and cube[1][0][0] == color_3 and cube[4][0][2] == color_1:
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[0][0][2] == color_1 and cube[4][0][0] == color_2 and cube[3][0][2] == color_3:
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('W2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[0][0][2] == color_3 and cube[4][0][0] == color_1 and cube[3][0][2] == color_2:
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[0][0][2] == color_2 and cube[4][0][0] == color_3 and cube[3][0][2] == color_1:
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[0][2][2] == color_1 and cube[3][0][0] == color_2 and cube[2][0][2] == color_3:
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[0][2][2] == color_3 and cube[3][0][0] == color_1 and cube[2][0][2] == color_2:
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
    elif cube[0][2][2] == color_2 and cube[3][0][0] == color_3 and cube[2][0][2] == color_1:
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[2][2][0] == color_1 and cube[5][0][0] == color_2 and cube[1][2][2] == color_3:
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[2][2][0] == color_3 and cube[5][0][0] == color_1 and cube[1][2][2] == color_2:
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[2][2][0] == color_2 and cube[5][0][0] == color_3 and cube[1][2][2] == color_1:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[1][2][0] == color_1 and cube[5][2][0] == color_2 and cube[4][2][2] == color_3:
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[1][2][0] == color_3 and cube[5][2][0] == color_1 and cube[4][2][2] == color_2:
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[1][2][0] == color_2 and cube[5][2][0] == color_3 and cube[4][2][2] == color_1:
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[4][2][0] == color_1 and cube[5][2][2] == color_2 and cube[3][2][2] == color_3:
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[4][2][0] == color_3 and cube[5][2][2] == color_1 and cube[3][2][2] == color_2:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[4][2][0] == color_2 and cube[5][2][2] == color_3 and cube[3][2][2] == color_1:
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[3][2][0] == color_1 and cube[5][0][2] == color_2 and cube[2][2][2] == color_3:
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[3][2][0] == color_3 and cube[5][0][2] == color_1 and cube[2][2][2] == color_2:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[3][2][0] == color_2 and cube[5][0][2] == color_3 and cube[2][2][2] == color_1:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    return (cube, moves, states)


def top_layer_corners(cube, moves, states):
    #####
    # For_white_red_green_piece_first
    cube, moves, states = top_layer_corners_solver(cube, moves, states, 'w', 'r', 'g')
    # For_white_green_orange_piece_second
    moves.append('Rotate the Cube and Make the GREEN Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    cube, moves, states = top_layer_corners_solver(cube, moves, states, 'w', 'g', 'o')
    # For_white_orange_blue_piece_third
    moves.append('Rotate the Cube and Make the ORANGE Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    cube, moves, states = top_layer_corners_solver(cube, moves, states, 'w', 'o', 'b')
    # For_white_blue_red_fourth
    moves.append('Rotate the Cube and Make the BLUE Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    cube, moves, states = top_layer_corners_solver(cube, moves, states, 'w', 'b', 'r')
    #####
    moves.append('Rotate the Cube and Make the RED face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    #####
    moves.append('The Top-Layer must be complete')
    states.append(copy.deepcopy(cube))
    return (cube, moves, states)


###Second_Layer###

def second_layer_edges_solver(cube, moves, states, color_1, color_2):
    if cube[2][1][0] == color_1 and cube[1][1][2] == color_2:
        # REQUIRED_ORIENTATION
        pass
    elif cube[2][1][0] == color_2 and cube[1][1][2] == color_1:
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[1][1][0] == color_1 and cube[4][1][2] == color_2:
        cube = W(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('W2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[1][1][0] == color_2 and cube[4][1][2] == color_1:
        cube = W(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('W2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[4][1][0] == color_1 and cube[3][1][2] == color_2:
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('W2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[4][1][0] == color_2 and cube[3][1][2] == color_1:
        cube = W(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('W2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[3][1][0] == color_1 and cube[2][1][2] == color_2:
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[3][1][0] == color_2 and cube[2][1][2] == color_1:
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(ccopy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[2][2][1] == color_1 and cube[5][0][1] == color_2:
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[2][2][1] == color_2 and cube[5][0][1] == color_1:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[1][2][1] == color_1 and cube[5][1][0] == color_2:
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[1][2][1] == color_2 and cube[5][1][0] == color_1:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[4][2][1] == color_1 and cube[5][2][1] == color_2:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[4][2][1] == color_2 and cube[5][2][1] == color_1:
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    elif cube[3][2][1] == color_1 and cube[5][1][2] == color_2:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
    elif cube[3][2][1] == color_2 and cube[5][1][2] == color_1:
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = W(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('W1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = W(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('W`1')
        cube = U(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('U2')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`2')
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
    return (cube, moves, states)


#############################

def second_layer_edges(cube, moves, states):
    #####
    # For_red_green_secondlayer_piece_first
    cube, moves, states = second_layer_edges_solver(cube, moves, states, 'r', 'g')
    # For_green_orange_secondlayer_piece_second
    moves.append('Make the GREEN Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    cube, moves, states = second_layer_edges_solver(cube, moves, states, 'g', 'o')
    # For_orange_blue_secondlayer_piece_third
    moves.append('Make the ORANGE Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    cube, moves, states = second_layer_edges_solver(cube, moves, states, 'o', 'b')
    # For_blue_red_secondlayer_fourth
    moves.append('Make the BLUE Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    cube, moves, states = second_layer_edges_solver(cube, moves, states, 'b', 'r')
    #####
    moves.append('Make the RED Face front')
    cube = U(cube, 0, False)
    cube = U(cube, 1, False)
    cube = U(cube, 2, False)
    states.append(copy.deepcopy(cube))
    #####
    moves.append('Second-Layer should be complete')
    states.append(copy.deepcopy(cube))
    return (cube, moves, states)


###Last_Layer###

def last_layer_cross_helper_1(cube, moves, states):
    cube = W(cube, 0, True)
    states.append(copy.deepcopy(cube))
    moves.append('W`1')
    cube = V(cube, 2, True)
    states.append(copy.deepcopy(cube))
    moves.append('V`2')
    cube = U(cube, 0, True)
    states.append(copy.deepcopy(cube))
    moves.append('U`1')
    cube = V(cube, 2, False)
    states.append(copy.deepcopy(cube))
    moves.append('V2')
    cube = U(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('U1')
    cube = W(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('W1')
    return (cube, moves, states)


def last_layer_cross_helper_2(cube, moves, states):
    cube = V(cube, 2, True)
    states.append(copy.deepcopy(cube))
    moves.append('V`2')
    cube = U(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('U1')
    cube = U(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('U1')
    cube = V(cube, 2, False)
    states.append(copy.deepcopy(cube))
    moves.append('V2')
    cube = U(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('U1')
    cube = V(cube, 2, True)
    states.append(copy.deepcopy(cube))
    moves.append('V`2')
    cube = U(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('U1')
    cube = V(cube, 2, False)
    states.append(copy.deepcopy(cube))
    moves.append('V2')
    cube = cube = U(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('U1')
    return (cube, moves, states)


def last_layer_corners_helper_1(cube, moves, states):
    cube = V(cube, 2, True)
    states.append(copy.deepcopy(cube))
    moves.append('V`2')
    cube = U(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('U1')
    cube = U(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('U1')
    cube = V(cube, 2, False)
    states.append(copy.deepcopy(cube))
    moves.append('V2')
    cube = U(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('U1')
    cube = V(cube, 2, True)
    states.append(copy.deepcopy(cube))
    moves.append('V`2')
    cube = U(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('U1')
    cube = V(cube, 2, False)
    states.append(copy.deepcopy(cube))
    moves.append('V2')
    return (cube, moves, states)


def last_layer_corners_helper_2(cube, moves, states):
    cube = V(cube, 0, True)
    states.append(copy.deepcopy(cube))
    moves.append('V`1')
    cube = U(cube, 0, True)
    states.append(copy.deepcopy(cube))
    moves.append('U`1')
    cube = U(cube, 0, True)
    states.append(copy.deepcopy(cube))
    moves.append('U`1')
    cube = V(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('V1')
    cube = U(cube, 0, True)
    states.append(copy.deepcopy(cube))
    moves.append('U`1')
    cube = V(cube, 0, True)
    states.append(copy.deepcopy(cube))
    moves.append('V`1')
    cube = U(cube, 0, True)
    states.append(copy.deepcopy(cube))
    moves.append('U`1')
    cube = V(cube, 0, False)
    states.append(copy.deepcopy(cube))
    moves.append('V1')
    return (cube, moves, states)


def last_layer_orientation(cube, moves, states):
    moves.append('Invert the Cube such that WHITE Face\nis on bottom and\nYELLOW Face \
on TOP with RED Face at front')
    for _ in range(2):
        cube = W(cube, 2, True)
        cube = W(cube, 1, True)
        cube = W(cube, 0, True)
    states.append(copy.deepcopy(cube))
    return (cube, moves, states)


def last_layer_cross_placement(cube, moves, states):
    if cube[0][0][1] == cube[0][1][1] and cube[0][1][0] == cube[0][1][1] and \
            cube[0][1][2] == cube[0][1][1] and cube[0][2][1] == cube[0][1][1]:
        pass
    elif cube[0][0][1] != cube[0][1][1] and cube[0][1][0] != cube[0][1][1] and \
            cube[0][1][2] != cube[0][1][1] and cube[0][2][1] != cube[0][1][1]:
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
    elif cube[0][0][1] == cube[0][1][1] and cube[0][2][1] == cube[0][1][1]:
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
    elif cube[0][1][0] == cube[0][1][1] and cube[0][1][2] == cube[0][1][1]:
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
    elif cube[0][0][1] == cube[0][1][1] and cube[0][1][0] == cube[0][1][1]:
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
    elif cube[0][0][1] == cube[0][1][1] and cube[0][1][2] == cube[0][1][1]:
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
    elif cube[0][1][0] == cube[0][1][1] and cube[0][2][1] == cube[0][1][1]:
        cube = U(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('U1')
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
    elif cube[0][1][2] == cube[0][1][1] and cube[0][2][1] == cube[0][1][1]:
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube, moves, states = last_layer_cross_helper_1(cube, moves, states)
    ########################################
    moves.append('YELLOW-Cross is formed')
    states.append(copy.deepcopy(cube))
    return (cube, moves, states)


def last_layer_cross_completion(cube, moves, states):
    # At this point top cross must have formed with yellow on top ONLY
    ########################################
    indicator = [(cube[2][0][1] == cube[2][1][1] and cube[4][0][1] == cube[4][1][1]), \
                 (cube[1][0][1] == cube[1][1][1] and cube[3][0][1] == cube[3][1][1]), \
                 (cube[2][0][1] == cube[2][1][1] and cube[1][0][1] == cube[1][1][1]), \
                 (cube[1][0][1] == cube[1][1][1] and cube[4][0][1] == cube[4][1][1]), \
                 (cube[4][0][1] == cube[4][1][1] and cube[3][0][1] == cube[3][1][1]), \
                 (cube[3][0][1] == cube[3][1][1] and cube[2][0][1] == cube[2][1][1])]
    if (cube[2][0][1] != cube[2][1][1] and cube[1][0][1] != cube[1][1][1] \
        and cube[4][0][1] != cube[4][1][1] and cube[3][0][1] != cube[3][1][1]) \
            or (cube[2][0][1] == cube[2][1][1]) or (cube[1][0][1] == cube[1][1][1]) \
            or (cube[4][0][1] == cube[4][1][1]) or (cube[3][0][1] == cube[3][1][1]):
        while not any(indicator):
            cube = U(cube, 0, True)
            states.append(copy.deepcopy(cube))
            moves.append('U`1')
            indicator = [(cube[2][0][1] == cube[2][1][1] and cube[4][0][1] == cube[4][1][1]), \
                         (cube[1][0][1] == cube[1][1][1] and cube[3][0][1] == cube[3][1][1]), \
                         (cube[2][0][1] == cube[2][1][1] and cube[1][0][1] == cube[1][1][1]), \
                         (cube[1][0][1] == cube[1][1][1] and cube[4][0][1] == cube[4][1][1]), \
                         (cube[4][0][1] == cube[4][1][1] and cube[3][0][1] == cube[3][1][1]), \
                         (cube[3][0][1] == cube[3][1][1] and cube[2][0][1] == cube[2][1][1])]
    #####
    final_indicator = [(cube[2][0][1] == cube[2][1][1] and cube[1][0][1] == cube[1][1][1]), \
                       cube[4][0][1] == cube[4][1][1] and cube[3][0][1] == cube[3][1][1]]
    if all(final_indicator):
        pass
    else:
        if (cube[2][0][1] == cube[2][1][1] and cube[4][0][1] == cube[4][1][1]) or \
                (cube[1][0][1] == cube[1][1][1] and cube[3][0][1] == cube[3][1][1]):
            cube, moves, states = last_layer_cross_helper_2(cube, moves, states)
            indicator = [(cube[2][0][1] == cube[2][1][1] and cube[4][0][1] == cube[4][1][1]), \
                         (cube[1][0][1] == cube[1][1][1] and cube[3][0][1] == cube[3][1][1]), \
                         (cube[2][0][1] == cube[2][1][1] and cube[1][0][1] == cube[1][1][1]), \
                         (cube[1][0][1] == cube[1][1][1] and cube[4][0][1] == cube[4][1][1]), \
                         (cube[4][0][1] == cube[4][1][1] and cube[3][0][1] == cube[3][1][1]), \
                         (cube[3][0][1] == cube[3][1][1] and cube[2][0][1] == cube[2][1][1])]
            while not any(indicator):
                cube = U(cube, 0, True)
                states.append(copy.deepcopy(cube))
                moves.append('U`1')
                indicator = [(cube[2][0][1] == cube[2][1][1] and cube[4][0][1] == cube[4][1][1]), \
                             (cube[1][0][1] == cube[1][1][1] and cube[3][0][1] == cube[3][1][1]), \
                             (cube[2][0][1] == cube[2][1][1] and cube[1][0][1] == cube[1][1][1]), \
                             (cube[1][0][1] == cube[1][1][1] and cube[4][0][1] == cube[4][1][1]), \
                             (cube[4][0][1] == cube[4][1][1] and cube[3][0][1] == cube[3][1][1]), \
                             (cube[3][0][1] == cube[3][1][1] and cube[2][0][1] == cube[2][1][1])]
        #####
        if cube[2][0][1] == cube[2][1][1] and cube[1][0][1] == cube[1][1][1]:
            moves.append('Make GREEN Face front')
            for x in range(3):
                cube = U(cube, x, True)
            states.append(copy.deepcopy(cube))
            cube, moves, states = last_layer_cross_helper_2(cube, moves, states)
        elif cube[1][0][1] == cube[1][1][1] and cube[4][0][1] == cube[4][1][1]:
            cube, moves, states = last_layer_cross_helper_2(cube, moves, states)
        elif cube[4][0][1] == cube[4][1][1] and cube[3][0][1] == cube[3][1][1]:
            moves.append('Make BLUE Face front')
            for x in range(3):
                cube = U(cube, x, False)
            states.append(copy.deepcopy(cube))
            cube, moves, states = last_layer_cross_helper_2(cube, moves, states)
        elif cube[3][0][1] == cube[3][1][1] and cube[2][0][1] == cube[2][1][1]:
            moves.append('Make the ORANGE Face front')
            for _ in range(2):
                for x in range(3):
                    cube = U(cube, x, False)
            states.append(copy.deepcopy(cube))
            cube, moves, states = last_layer_cross_helper_2(cube, moves, states)
    moves.append('TOP-CROSS is complete')
    states.append(copy.deepcopy(cube))
    ########################################
    return (cube, moves, states)


def last_layer_corners(cube, moves, states):
    # top_right_line
    indicator1 = [(cube[2][0][2] == cube[0][1][1] and cube[4][0][0] == cube[0][1][1]), \
                  (cube[3][0][0] == cube[0][1][1] and cube[3][0][2] == cube[0][1][1])]
    # top_left_line
    indicator2 = [(cube[2][0][0] == cube[0][1][1] and cube[4][0][2] == cube[0][1][1]), \
                  (cube[1][0][0] == cube[0][1][1] and cube[1][0][2] == cube[0][1][1])]
    # top_upper_line
    indicator3 = [(cube[4][0][0] == cube[0][1][1] and cube[4][0][2] == cube[0][1][1]), \
                  (cube[1][0][0] == cube[0][1][1] and cube[3][0][2] == cube[0][1][1])]
    # top_lower_line
    indicator4 = [(cube[1][0][2] == cube[0][1][1] and cube[3][0][0] == cube[0][1][1]), \
                  (cube[2][0][0] == cube[0][1][1] and cube[2][0][2] == cube[0][1][1])]
    ###
    final_indicator = [cube[0][0][0] == cube[0][1][1], cube[0][0][2] == cube[0][1][1], \
                       cube[0][2][0] == cube[0][1][1], cube[0][2][2] == cube[0][1][1]]
    if all(final_indicator):
        pass
    else:
        while not all(final_indicator):
            if any(indicator1):
                cube, moves, states = last_layer_corners_helper_1(cube, moves, states)
                cube, moves, states = last_layer_corners_helper_2(cube, moves, states)
            elif any(indicator2):
                cube, moves, states = last_layer_corners_helper_2(cube, moves, states)
                cube, moves, states = last_layer_corners_helper_1(cube, moves, states)
            elif any(indicator3):
                if cube[3][1][1] == 'r':
                    moves.append('Make the RED Face front')
                elif cube[3][1][1] == 'g':
                    moves.append('Make the GREEN Face front')
                elif cube[3][1][1] == 'b':
                    moves.append('Make the BLUE Face front')
                elif cube[3][1][1] == 'o':
                    moves.append('Make the ORANGE Face front')
                for x in range(3):
                    cube = U(cube, x, True)
                states.append(copy.deepcopy(cube))
            elif any(indicator4):
                if cube[1][1][1] == 'r':
                    moves.append('Make the RED Face front')
                elif cube[1][1][1] == 'g':
                    moves.append('Make the GREEN Face front')
                elif cube[1][1][1] == 'b':
                    moves.append('Make the BLUE face Front')
                elif cube[1][1][1] == 'o':
                    moves.append('Make the ORANGE face Front')
                for x in range(3):
                    cube = U(cube, x, False)
                states.append(copy.deepcopy(cube))
            elif not any([any(indicator1), any(indicator2), any(indicator3), any(indicator4)]):
                cube, moves, states = last_layer_corners_helper_1(cube, moves, states)
                cube, moves, states = last_layer_corners_helper_2(cube, moves, states)
            indicator1 = [(cube[2][0][2] == cube[0][1][1] and cube[4][0][0] == cube[0][1][1]), \
                          (cube[3][0][0] == cube[0][1][1] and cube[3][0][2] == cube[0][1][1])]
            indicator2 = [(cube[2][0][0] == cube[0][1][1] and cube[4][0][2] == cube[0][1][1]), \
                          (cube[1][0][0] == cube[0][1][1] and cube[1][0][2] == cube[0][1][1])]
            indicator3 = [(cube[4][0][0] == cube[0][1][1] and cube[4][0][2] == cube[0][1][1]), \
                          (cube[1][0][0] == cube[0][1][1] and cube[3][0][2] == cube[0][1][1])]
            indicator4 = [(cube[1][0][2] == cube[0][1][1] and cube[3][0][0] == cube[0][1][1]), \
                          (cube[2][0][0] == cube[0][1][1] and cube[2][0][2] == cube[0][1][1])]
            final_indicator = [cube[0][0][0] == cube[0][1][1], cube[0][0][2] == cube[0][1][1], \
                               cube[0][2][0] == cube[0][1][1], cube[0][2][2] == cube[0][1][1]]
    return (cube, moves, states)


def last_layer_solver(cube, moves, states):
    ###########
    ########################################
    # if no corner is at right place or position
    if not ((cube[0][2][2] == cube[0][1][1] or cube[0][2][2] == cube[2][1][1] or cube[0][2][2] == cube[3][1][1]) \
            and (cube[2][0][2] == cube[0][1][1] or cube[2][0][2] == cube[2][1][1] or cube[2][0][2] == cube[3][1][1]) \
            and (cube[3][0][0] == cube[0][1][1] or cube[3][0][0] == cube[2][1][1] or cube[3][0][0] == cube[3][1][1])):
        for i in range(3):
            if cube[3][1][1] == 'r':
                moves.append('Make the RED Face front')
            elif cube[3][1][1] == 'g':
                moves.append('Make the GREEN Face front')
            elif cube[3][1][1] == 'b':
                moves.append('Make the BLUE Face front')
            elif cube[3][1][1] == 'o':
                moves.append('Make the ORANGE Face front')
            for x in range(3):
                cube = U(cube, x, True)
            states.append(copy.deepcopy(cube))
            if ((cube[0][2][2] == cube[0][1][1] or cube[0][2][2] == cube[2][1][1] or cube[0][2][2] == cube[3][1][1]) \
                    and (cube[2][0][2] == cube[0][1][1] or cube[2][0][2] == cube[2][1][1] or cube[2][0][2] ==
                         cube[3][1][1]) \
                    and (cube[3][0][0] == cube[0][1][1] or cube[3][0][0] == cube[2][1][1] or cube[3][0][0] ==
                         cube[3][1][1])):
                break
        if not ((cube[0][2][2] == cube[0][1][1] or cube[0][2][2] == cube[2][1][1] or cube[0][2][2] == cube[3][1][1]) \
                and (cube[2][0][2] == cube[0][1][1] or cube[2][0][2] == cube[2][1][1] or cube[2][0][2] == cube[3][1][1]) \
                and (cube[3][0][0] == cube[0][1][1] or cube[3][0][0] == cube[2][1][1] or cube[3][0][0] == cube[3][1][
                    1])):
            cube = V(cube, 0, True)
            states.append(copy.deepcopy(cube))
            moves.append('V`1')
            cube = U(cube, 0, True)
            states.append(copy.deepcopy(cube))
            moves.append('U`1')
            cube = V(cube, 2, True)
            states.append(copy.deepcopy(cube))
            moves.append('V`2')
            cube = U(cube, 0, False)
            states.append(copy.deepcopy(cube))
            moves.append('U1')
            cube = V(cube, 0, False)
            states.append(copy.deepcopy(cube))
            moves.append('V1')
            cube = U(cube, 0, True)
            states.append(copy.deepcopy(cube))
            moves.append('U`1')
            cube = V(cube, 2, False)
            states.append(copy.deepcopy(cube))
            moves.append('V2')
            cube = U(cube, 0, False)
            states.append(copy.deepcopy(cube))
            moves.append('U1')
    ########################################
    # now finding corner cube that is at right place but not at right position
    while not ((cube[0][2][2] == cube[0][1][1] or cube[0][2][2] == cube[2][1][1] or cube[0][2][2] == cube[3][1][1]) \
               and (cube[2][0][2] == cube[0][1][1] or cube[2][0][2] == cube[2][1][1] or cube[2][0][2] == cube[3][1][1]) \
               and (cube[3][0][0] == cube[0][1][1] or cube[3][0][0] == cube[2][1][1] or cube[3][0][0] == cube[3][1][
                1])):
        if cube[3][1][1] == 'r':
            moves.append('Make the RED Face front')
        elif cube[3][1][1] == 'g':
            moves.append('Make the GREEN Face front')
        elif cube[3][1][1] == 'b':
            moves.append('Make the BLUE Face front')
        elif cube[3][1][1] == 'o':
            moves.append('Make the ORANGE Face front')
        for x in range(3):
            cube = U(cube, x, True)
        states.append(copy.deepcopy(cube))
    ########################################
    # now putting the left front corner at right place
    moves.append('Front Right corner at right place\nbut wrong orientation')
    states.append(copy.deepcopy(cube))
    while not ((cube[0][2][0] == cube[0][1][1] or cube[0][2][0] == cube[1][1][1] or cube[0][2][0] == cube[2][1][1]) \
               and (cube[1][0][2] == cube[0][1][1] or cube[1][0][2] == cube[1][1][1] or cube[1][0][2] == cube[2][1][1]) \
               and (cube[2][0][0] == cube[0][1][1] or cube[2][0][0] == cube[1][1][1] or cube[2][0][0] == cube[2][1][
                1])):
        cube = V(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`1')
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube = V(cube, 2, True)
        states.append(copy.deepcopy(cube))
        moves.append('V`2')
        cube = U(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('U1')
        cube = V(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('V1')
        cube = U(cube, 0, True)
        states.append(copy.deepcopy(cube))
        moves.append('U`1')
        cube = V(cube, 2, False)
        states.append(copy.deepcopy(cube))
        moves.append('V2')
        cube = U(cube, 0, False)
        states.append(copy.deepcopy(cube))
        moves.append('U1')
    moves.append('All corner at right place \nbut wrong orientation')
    states.append(copy.deepcopy(cube))
    ########################################
    # Finally Putting the corners at right orientation
    cube, moves, states = last_layer_corners(cube, moves, states)
    ########################################
    return (cube, moves, states)


##################################################################

cube_input = final_string
print(cube_input)

def final_solved_cube(cube_input):
    moves = []
    states = []
    cube = []
    indi=True
    cube, moves, states, indi= validity_formation(cube, cube_input, moves, states, indi)
    if indi==True and cube_input=='wwwwwwwwwgggrrrbbbooogggrrrbbbooogggrrrbbboooyyyyyyyyy':
        states.append(cube)
        moves.append('Final State')
        return (cube,moves,states)
    elif indi==True:
        cube, moves, states = top_layer_cross(cube, moves, states)
        cube, moves, states = top_layer_corners(cube, moves, states)
        cube, moves, states = second_layer_edges(cube, moves, states)
        cube, moves, states = last_layer_orientation(cube, moves, states)
        cube, moves, states = last_layer_cross_placement(cube, moves, states)
        cube, moves, states = last_layer_cross_completion(cube, moves, states)
        cube, moves, states = last_layer_solver(cube, moves, states)
        return cube, moves, states
    elif indi==False:
        return (cube, moves, states)


final_cube, moves, states = final_solved_cube(cube_input)
print(moves)
print(final_cube)
#print(states)

#######################################################################




############################### GUI_REST ###############################




master2 = Tk()
frame1 = Frame(master2)
#frame1.grid()
#master2.geometry("400x400")
master2.title('Visualizer')
def time():
    str = strftime("%M:%S")
    label.config(text=str)
    label.after(1000,time)

#label = Label(master2, bg = "black", bd = 60, fg = "white",padx=60,font=("Arial", 30),justify = RIGHT)
    
label = Label(master2, background = "black", foreground = "cyan", padx=90,pady=30, justify = RIGHT,
              relief=RAISED, font=("Arial", 60))
label.place(relx = 1.0,rely = 0.0,anchor ='ne')
time()
master2.state('zoomed')


# LEFT FACE

Button1 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button1.grid(row=15, column=2)

Button2 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button2.grid(row=15, column=3)

Button3 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button3.grid(row=15, column=4)

Button4 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button4.grid(row=16, column=2)

Button5 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button5.grid(row=16, column=3)

Button6 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button6.grid(row=16, column=4)

Button7 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button7.grid(row=17, column=2)

Button8 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button8.grid(row=17, column=3)

Button9 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button9.grid(row=17, column=4)



button_dist1 = Button(master2, height = 1 ,width = 11, bd = 0)
button_dist1.grid(row=14, column=0)

button_dist2 = Button(master2, height = 1 ,width = 2, bd = 0)
button_dist2.grid(row=15, column=5)

button_dist3 = Button(master2, height = 1 ,width = 2, bd = 0)
button_dist3.grid(row=15, column=10)

button_dist4 = Button(master2, height = 1 ,width = 2, bd = 0)
button_dist4.grid(row=15, column=15)

button_dist5 = Button(master2, height = 1 ,width = 1, bd = 0)
button_dist5.grid(row=18, column=0)

button_dist6 = Button(master2, height = 2 ,width = 1, bd = 0)
button_dist6.grid(row=0, column=0)

# FRONT FACE

Button10 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button10.grid(row=15, column=7)

Button11 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button11.grid(row=15, column=8)

Button12 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button12.grid(row=15, column=9)

Button13 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button13.grid(row=16, column=7)

Button14 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button14.grid(row=16, column=8)

Button15 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button15.grid(row=16, column=9)

Button16 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button16.grid(row=17, column=7)

Button17 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button17.grid(row=17, column=8)

Button18 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button18.grid(row=17, column=9)



# RIGHT FACE


Button19 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button19.grid(row=15, column=12)

Button20 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button20.grid(row=15, column=13)

Button21 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button21.grid(row=15, column=14)

Button22 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button22.grid(row=16, column=12)

Button23 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button23.grid(row=16, column=13)

Button24 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button24.grid(row=16, column=14)

Button25 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button25.grid(row=17, column=12)

Button26 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button26.grid(row=17, column=13)

Button27 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button27.grid(row=17, column=14)


# TOP FACE


Button28 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button28.grid(row=11, column=7)

Button29 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button29.grid(row=11, column=8)

Button30 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button30.grid(row=11, column=9)

Button31 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button31.grid(row=12, column=7)

Button32 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button32.grid(row=12, column=8)

Button33 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button33.grid(row=12, column=9)

Button34 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button34.grid(row=13, column=7)

Button35 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button35.grid(row=13, column=8)

Button36 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button36.grid(row=13, column=9)


# BACK FACE


Button37 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button37.grid(row=15, column=17)

Button38 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button38.grid(row=15, column=18)

Button39 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button39.grid(row=15, column=19)

Button40 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button40.grid(row=16, column=17)

Button41 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button41.grid(row=16, column=18)

Button42 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button42.grid(row=16, column=19)

Button43 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button43.grid(row=17, column=17)

Button44 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button44.grid(row=17, column=18)

Button45 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button45.grid(row=17, column=19)



# BOTTOM FACE


Button46 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button46.grid(row=20, column=7)

Button47 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button47.grid(row=20, column=8)

Button48 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button48.grid(row=20, column=9)

Button49 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button49.grid(row=21, column=7)

Button50 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button50.grid(row=21, column=8)

Button51 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button51.grid(row=21, column=9)

Button52 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button52.grid(row=22, column=7)

Button53 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button53.grid(row=22, column=8)

Button54 = Button(master2, text="",height = 3 ,width = 7, bg = 'Grey', bd = 7)
Button54.grid(row=22, column=9)


instruct = Label(master2, text = 'Initial State', font=("Times New Roman", 13, 'bold'))
instruct.grid(row = 16, column = 20)



color_code = {'b': 'Blue', 'y': 'Yellow', 'r': 'Red', 'g': 'Green', 'w': 'White', 'o': 'Orange'}


for faces, instructions in zip(states, moves):

    try:
        [[[a, b, c], [d, e, f], [g, h, i]], [[j, k, l], [m, n, o], [p, q, r]], [[s, t, u], [v, w, x], [y, z, aa]],
         [[bb, cc, dd], [ee, ff, gg], [hh, ii, jj]], [[kk, ll, mm], [nn, oo, pp], [qq, rr, ss]],
         [[tt, uu, vv], [ww, xx, yy], [zz, aaa, bbb]]] = faces
        #### FIRST FACE ####
        a = color_code[a]
        b = color_code[b]
        c = color_code[c]
        d = color_code[d]
        e = color_code[e]
        f = color_code[f]
        g = color_code[g]
        h = color_code[h]
        i = color_code[i]

        #### SECOND FACE ####
        j = color_code[j]
        k = color_code[k]
        l = color_code[l]
        m = color_code[m]
        n = color_code[n]
        o = color_code[o]
        p = color_code[p]
        q = color_code[q]
        r = color_code[r]

        #### THIRD FACE ####
        s = color_code[s]
        t = color_code[t]
        u = color_code[u]
        v = color_code[v]
        w = color_code[w]
        x = color_code[x]
        y = color_code[y]
        z = color_code[z]
        aa = color_code[aa]

        #### FOURTH FACE ####
        bb = color_code[bb]
        cc = color_code[cc]
        dd = color_code[dd]
        ee = color_code[ee]
        ff = color_code[ff]
        gg = color_code[gg]
        hh = color_code[hh]
        ii = color_code[ii]
        jj = color_code[jj]

        #### FIFTH FACE ####
        kk = color_code[kk]
        ll = color_code[ll]
        mm = color_code[mm]
        nn = color_code[nn]
        oo = color_code[oo]
        pp = color_code[pp]
        qq = color_code[qq]
        rr = color_code[rr]
        ss = color_code[ss]

        #### SIXTH FACE ####
        tt = color_code[tt]
        uu = color_code[uu]
        vv = color_code[vv]
        ww = color_code[ww]
        xx = color_code[xx]
        yy = color_code[yy]
        zz = color_code[zz]
        aaa = color_code[aaa]
        bbb = color_code[bbb]




        master2.update_idletasks()
        master2.update()


        ##### FRONT FACE ####


        master2.after(1000, Button10.config(bg=s))
        master2.after(0, Button11.config(bg=t))
        master2.after(0, Button12.config(bg=u))
        master2.after(0, Button13.config(bg=v))
        master2.after(0, Button14.config(bg=w))
        master2.after(0, Button15.config(bg=x))
        master2.after(0, Button16.config(bg=y))
        master2.after(0, Button17.config(bg=z))
        master2.after(0, Button18.config(bg=aa))


        ##### LEFT FACE ####


        master2.after(0, Button1.config(bg=j))
        master2.after(0, Button2.config(bg=k))
        master2.after(0, Button3.config(bg=l))
        master2.after(0, Button4.config(bg=m))
        master2.after(0, Button5.config(bg=n))
        master2.after(0, Button6.config(bg=o))
        master2.after(0, Button7.config(bg=p))
        master2.after(0, Button8.config(bg=q))
        master2.after(0, Button9.config(bg=r))


        ##### RIGHT FACE ####


        master2.after(0, Button19.config(bg=bb))
        master2.after(0, Button20.config(bg=cc))
        master2.after(0, Button21.config(bg=dd))
        master2.after(0, Button22.config(bg=ee))
        master2.after(0, Button23.config(bg=ff))
        master2.after(0, Button24.config(bg=gg))
        master2.after(0, Button25.config(bg=hh))
        master2.after(0, Button26.config(bg=ii))
        master2.after(0, Button27.config(bg=jj))


        ##### BACK FACE ####


        master2.after(0, Button37.config(bg=kk))
        master2.after(0, Button38.config(bg=ll))
        master2.after(0, Button39.config(bg=mm))
        master2.after(0, Button40.config(bg=nn))
        master2.after(0, Button41.config(bg=oo))
        master2.after(0, Button42.config(bg=pp))
        master2.after(0, Button43.config(bg=qq))
        master2.after(0, Button44.config(bg=rr))
        master2.after(0, Button45.config(bg=ss))


        #### TOP FACE ####


        master2.after(0, Button28.config(bg=a))
        master2.after(0, Button29.config(bg=b))
        master2.after(0, Button30.config(bg=c))
        master2.after(0, Button31.config(bg=d))
        master2.after(0, Button32.config(bg=e))
        master2.after(0, Button33.config(bg=f))
        master2.after(0, Button34.config(bg=g))
        master2.after(0, Button35.config(bg=h))
        master2.after(0, Button36.config(bg=i))


        #### BOTTOM FACE ####


        master2.after(0, Button46.config(bg=tt))
        master2.after(0, Button47.config(bg=uu))
        master2.after(0, Button48.config(bg=vv))
        master2.after(0, Button49.config(bg=ww))
        master2.after(0, Button50.config(bg=xx))
        master2.after(0, Button51.config(bg=yy))
        master2.after(0, Button52.config(bg=zz))
        master2.after(0, Button53.config(bg=aaa))
        master2.after(0, Button54.config(bg=bbb))


        #### LABEL UPDATE ####


        master2.after(0, instruct.config(text = instructions))


        master2.update_idletasks()
        master2.update()
    except:
        break

master2.mainloop()


#################__END__################




