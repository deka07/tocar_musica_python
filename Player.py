import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory # Biblioteca para abrir diretorio do sistema

class App:
    def __init__(self):
        self.win = Tk()
        self.win.geometry('550x250')
        self.win.title('Cactus Player')

        pygame.init()

        # Importando as imagens do programa
        self.img_folder = PhotoImage(file='icon/folder.png')
        self.img_play = PhotoImage(file='icon/play.png')
        self.img_pouse = PhotoImage(file='icon/pause.png')
        self.img_stop = PhotoImage(file='icon/stop.png')
        self.img_next = PhotoImage(file='icon/next.png')
        self.img_prev = PhotoImage(file='icon/previous.png')

        # Botoes do programas. -----------------------------------------------------
        self.bnt_pasta = Button(self.win, image=self.img_folder, command=self.folder)
        self.bnt_pasta.place(x=500, y=100)

        self.bnt_play = Button(self.win, image=self.img_play, command=self.play)
        self.bnt_play.place(x=230, y=25)

        self.bnt_pause = Button(self.win, image=self.img_pouse, command=self.pause)
        self.bnt_pause.place(x=192, y=40)

        self.bnt_stop = Button(self.win, image=self.img_stop, command=self.stop)
        self.bnt_stop.place(x=300, y=40)

        self.bnt_prev = Button(self.win, image=self.img_prev, command=self.anterior)
        self.bnt_prev.place(x=154, y=40)

        self.bnt_next = Button(self.win, image=self.img_next, command=self.proximo)
        self.bnt_next.place(x=338, y=40)

        # Caixa de lIsta ------------------------------------
        self.play_list = Listbox(self.win, width=63, height=5)
        self.play_list.place(x=20, y=140)

        self.win.mainloop()
    
    def folder(self, *args):
        self.pasta = askdirectory()
        os.chdir(self.pasta) # Permite alterar o diretório atual
        self.faixas = os.listdir() # Retorna a lista de arquivos de música
        
        for self.musica in self.faixas:
            self.play_list.insert(0, self.musica)

    def play(self, *args):
        self.play_list.bind("<<ListboxSelect>>", self.OnSelect) # Seleciona um item da lista
        pygame.mixer.music.load(self.value)
        pygame.mixer.music.play()
        
        # Nomas das musicas
        Label(self.win, text='Tocando: {}').place(x=100, y=100).format(self.value)

    def stop(self, *args):
        pygame.mixer.music.stop()
    
    def stop(self, *args):
        pygame.mixer.music.stop()

    def pause(self, *args):
        pygame.mixer.music.pause()

    def unpause(self, *args):
        pygame.mixer.music.unpause()

    def proximo(self, *args):
        pygame.mixer.music.load(self.musica)
        pygame.mixer.music.play()

    def anterior(self, *args):
        pygame.mixer.music.load(self.musica)
        pygame.mixer.music.play()

    # Função que permite selecionar um item da lista para ser reproduzido.
    def OnSelect(self, event):
        widget = event.widget
        self.value = widget.get(widget.curselection()[0])
        print(self.value)

App()