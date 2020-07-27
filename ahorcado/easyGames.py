#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:45:10 2020.

@author: martinxubuntu
"""
import tkinter as tk


## Jueguito del ahorcado

class Ahorcado:
    """Logica del juego."""
    
    lifesLeft = int
    wordToGuess = str
    letters = ''
    hashWord = list
    
    
    def __init__(self):
        """Valores iniciales del juego."""
        self.hashWord = []
        self.lifesLeft = 3
        
    def chooseWord(self):
        """Definicion de la palabra."""
        self.wordToGuess = window.letterTxt.get().lower()
        if self.wordToGuess == '':
            window.letterLbl.config(text='Asshole, a WORD')
            return 0
        for i in range(0,len(self.wordToGuess)):
            self.hashWord += '-'        
        window.letterCount.config(text='The word that you have to guess has {} letters'.format(len(self.wordToGuess)))
        window.wordLbl.config(text=''.join(self.hashWord))
        window.letterLbl.config(text='Choose a letter')
        window.btnLetter.config(text='Try this letter',command=window.juego.tryALetter)
        window.letterTxt.config(show='')
        window.letterTxt.delete(0,len(self.wordToGuess))
        window.chk.pack()

    def loseALife(self):
        """Rest one life."""
        self.lifesLeft -= 1
        window.statusLbl.config(text='WROOONG, you lose one life')        
        if self.lifesLeft == 0:
            window.lifes.config(text='You have no more lifes,{} lifes, you lose the game bro'.format(self.lifesLeft))
        else:
            window.lifes.config(text='Now you have {} lifes left'.format(self.lifesLeft))
         
    def tryALetter(self):
        """Player trys a letter."""
        letter = window.letterTxt.get().lower()
        window.letterTxt.delete(0,len(self.wordToGuess))
        if (letter in self.letters):
            if self.lifesLeft<0:
                window.statusLbl.config(text='You lose bro, click Reset button to play again')
            else:
                window.statusLbl.config(text='You have already use that letter, try again')
        elif (letter in self.wordToGuess):
            self.letters += letter
            for i in range(0,len(self.wordToGuess)):
                if letter == self.wordToGuess[i]:
                    self.hashWord[i] = letter
                else:
                    continue
            if self.lifesLeft<0:
                window.statusLbl.config(text='You lose bro, click Reset button to play again')
            else:
                window.statusLbl.config(text='The letter \"{}\" is in the word! Well done'.format(letter))
                window.wordLbl.config(text=''.join(self.hashWord))
            if (self.wordToGuess == ''.join(self.hashWord)):
                        window.statusLbl.config(text='You win!!!!!!!! Congrats')
        else:
            if self.lifesLeft<0:
                window.statusLbl.config(text='You lose bro, click Reset button to play again')
            else: 
                self.letters += letter
                self.loseALife()
        window.lettersTry.config(text='You try {}'.format(self.letters))
            
    def tryAWord(self):
        """Try a final answ."""
        if self.lifesLeft<0:
            window.statusLbl.config(text='You lose bro, click Reset button to play again')
        else:
            answ = window.letterTxt.get().lower()
            if answ == self.wordToGuess:
                window.statusLbl.config(text='You win!!!!!!!! Congrats, the word was {}'.format(self.wordToGuess))
                window.wordLbl.config(text='{}'.format(self.wordToGuess))
            else:
                self.loseALife()
                window.letterTxt.delete(0,len(self.letterTxt.get()))






# El Ahorcado esta listo en consola, se necesita adaptar a la tkinter
class MainWindow:
    """Armo la GUI."""
    
    # juego = Ahorcado()
    
    def __init__(self,window,width=400,height=300):
        """Init."""
        # Defino el tama;o de la ventana
        self.juego = Ahorcado()
        window.geometry('{}x{}'.format(width,height))
        self.btnReset = tk.Button(window,text='Reset',command=self.reset)
        # self.btnReset.grid(column=3,row=8)
        self.btnReset.pack(side=tk.BOTTOM)
        self.lblro = tk.Label(window,text='Lowers and Capitals are the same')
        self.lblro.pack(side=tk.BOTTOM)
        self.letterLbl = tk.Label(window,text='Choose a word')
        # self.letterLbl.grid(column=2,row=2)
        self.letterLbl.pack(pady=5)
        self.letterTxt = tk.Entry(window,width=10,show="*")
        # self.letterTxt.grid(column=3,row=2)
        self.letterTxt.pack(pady=5)
        self.btnLetter = tk.Button(window,text='Done',command=self.juego.chooseWord)
        # self.btnLetter.grid(column=4,row=2)
        self.btnLetter.pack(pady=5)
        self.lifes = tk.Label(window,text='You have {} lifes'.format(self.juego.lifesLeft))
        # self.lifes.grid(column=3,row=5)
        self.lifes.pack(pady=5)
        self.statusLbl = tk.Label(window,text='')
        # self.statusLbl.grid(column=3,row=4)
        self.statusLbl.pack(pady=5)
        self.wordLbl = tk.Label(text='')
        # self.wordLbl.grid(column=3,row=1)
        self.wordLbl.pack(pady=5)
        self.letterCount = tk.Label(text='')
        # self.letterCount.grid(column=3,row=20)
        self.letterCount.pack(pady=5)
        self.lettersTry = tk.Label(text='')
        # self.lettersTry.grid(column=3,row=6)wordLbl
        self.lettersTry.pack(pady=5)
        self.chk_state = tk.BooleanVar()
        self.chk_state.set(False)
        self.chk = tk.Checkbutton(window, text='Choose mode', var=self.chk_state, command=self.changeStyle)
        
        
    def reset(self):
        """Resetea el juego."""
        self.juego = Ahorcado()
        self.letterLbl.config(text='Choose a word')
        self.letterTxt.config(show="*")
        self.letterTxt.delete(0,len(self.letterTxt.get()))
        self.btnLetter.config(text='Done',command=self.juego.chooseWord)
        self.lifes.config(text='You have {} lifes'.format(self.juego.lifesLeft))
        self.statusLbl.config(text='')
        self.wordLbl.config(text='')
        self.letterCount.config(text='')
        self.lettersTry.config(text='')
        
    def changeStyle(self):
        """Change from word to letter and viceversa."""
        if (self.chk_state.get()):
            self.letterLbl.config(text = 'Try a word')
            self.btnLetter.config(text= 'Try this word', command=self.juego.tryAWord)
            self.letterTxt.delete(0,len(self.letterTxt.get()))
        else:
            self.letterLbl.config(text = 'Try a letter')
            self.btnLetter.config(text='Try this letter', command=self.juego.tryALetter)
            self.letterTxt.delete(0,len(self.letterTxt.get()))

        
        
                
app = tk.Tk()
#app.iconbitmap(default="/home/martinxubuntu/Desktop/pythonProjects/ahorcado/ahorcado.ico")
#app.iconphoto(False,tk.PhotoImage(file='./ahorcado.png'))
#app.iconphoto(False,tk.PhotoImage(file='ahorcado.ico'))
app.title('Ahorcado!!!')
window = MainWindow(app)
app.mainloop()
        

