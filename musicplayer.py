import pygame
import os

root=Tk()
root.title("music player")
root.wm_iconbitmap("tic-tac-toe_39453.ico")

root.geometry("450x150")

pygame.mixer.init()

n=0

def start_stop():
	global n
	n=n+1

	if n==1:
		song_name=songs_listbox.get()
		pygame.mixer.music.load(song_name)
		pygame.mixer.music.play(0)
		print("music started ")
	elif (n%2)==0:
 		pygame.mixer.music.pause()
 		print("paused ")

	elif (n%2)!=0:
		pygame.mixer.music.unpause()
		print("unPaused")




l1=Label(root,text="MUSIC PLAYER",font="times 20")
l1.grid(row=1,column=1)

b2=Button(root,text='start/stop',width=20,command=start_stop)
b2.grid(row=4,column=1)


songs_list=os.listdir()
songs_listbox=StringVar(root)
songs_listbox.set("select songs")
menu=OptionMenu(root,songs_listbox,*songs_list)
menu.grid(row=4,column=4)



root.mainloop()
