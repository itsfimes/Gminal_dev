import tkinter
from tkinter import *
from tkinter import messagebox
import time
from typing import MutableSequence
import time

from pygame.constants import K_ESCAPE
MenuOn = True
def game():
    MenuOn = False
    import tkinter
    import tk
    import pygame
    from sys import exit
    g = Tk()
    g.geometry("1200x1200")
    
    pygame.init()
    screen = pygame.display.set_mode((1200,1200),pygame.FULLSCREEN)
    pygame.display.set_caption("Game -BETA")
    GameOn = True
    def game_exit():
        pygame.event = pygame.QUIT
    while GameOn == True:
        
        #Gexit = Button(g, text="Exit",command=game_exit)
        #GexitImg = PhotoImage(file="Assets\Menu\ExitButton.png") 
        #Gexit.config(image=GexitImg)
        #Gexit.place(x=5,y=700)
        playerImg = pygame.image.load ("Assets\Game\Player.png")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GameON = False
                    MenuOn = False                                                                                                                                                         
                    exit()
                    pygame.QUIT
                    GameOn = False
        pygame.display.update()

 
def menu():

        m = Tk()
        m.geometry("1200x1200")


        mtX=450
        mtY=10

        mm=5

        #Text v menu

        Txt1 = Label(m, text="Window of milk",font = ("Kalam", 50))
        Txt1.place(x=mtX,y=mtY)
        
        Txt2 = Label(m, text="Thicc edition™", font=("Kalam",10))
        Txt2.place(x=890,y=25)
        

        #Mlíko v menu
        milkMenu = Canvas(m, width =2000, height =2000)      
        milkMenu.place(x=230,y=100)
        milkMenuIMG = PhotoImage(file="Assets\Menu\WindowOfMilk.png")    
        milkMenu.create_image(0,0, anchor=NW, image=milkMenuIMG)

        #WeirdUI
        UIMenu = Canvas(m, width =186, height =159)      
        UIMenu.place(x=1150,y=50)
        UIMenuIMG = PhotoImage(file="Assets\Menu\WeirdUI.png")    
        UIMenu.create_image(0,0, anchor=NW, image=UIMenuIMG)    
        #funkce na exit
        def Mexit():
            m.destroy()
        #Tlačítko exitu
        Bexit = Button(m, text="Exit",command=Mexit)
        ExitImg = PhotoImage(file="Assets\Menu\ExitButton.png") 
        Bexit.config(image=ExitImg)
        Bexit.place(x=5,y=700)
        def info():
            messagebox.showinfo("Oh, so", "This is my first game so it's very bad.")
            messagebox.showinfo("You don't know what Karlson is?", "Developed by: Fimes (With help of StackOverflow and GitHub)")
            messagebox.showinfo("Its just a little game","UI Designers: Everyone in my class")
            messagebox.showinfo("That Dani is working on","Special thanks to: David, Avast team, Wexi, Dani, Martin")
            messagebox.showinfo("So wishlist it now","@wecodeinpython, @3coder")
            messagebox.showinfo("Gamers and Boners!", "This game is fangame for Dani")
            messagebox.showinfo("Info about mine english","I am sorry if there are errors in the text but I am not from England or America")
        #Tlačítko infa
        Binfo = Button(m,text="Info",command=info)
        InfoImg = PhotoImage(file="Assets\Menu\InfoButton.png")
        Binfo.config(image=InfoImg)
        Binfo.place(x=1250,y=700)
        #Funkce exitu hry
        def Mexit():
            MenuOn = False
            m.destroy()
            
        #Funkce exitu menu
        def Mplay():
            MenuOn = False
            game()
        #Tlačítko play
        Bplay = Button(m,text="Play!",command=Mplay)
        PlayImg = PhotoImage(file="Assets\Menu\PlayButton.png")
        Bplay.config(image=PlayImg)
        Bplay.place(x=600,y=500)
        m.attributes("-fullscreen", True)
        m.mainloop()
menu()
