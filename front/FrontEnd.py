import curses
import curses.textpad
import os
import sys

class FrontEnd:

    def __init__(self, player):
        self.player = player
        self.player.play(sys.argv[1])
        curses.wrapper(self.menu)

    def menu(self, args):
        self.stdscr = curses.initscr()
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - playList")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                self.openPlaylist()


    def openPlaylist(self):
        changeWindow = curses.newwin(5, 60, 5, 40)
        changeWindow.border()
        changeWindow.addstr(0,0,"Path to playlist directory?",curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1,50)
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop() 
        

    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())


    '''Made changing songs easier? '''
    def changeSong(self):
        songWindow = curses.newwin(20,30,5,40)
        songWindow.border()
        songWindow.addstr(0,0,"Type song number:", curses.A_REVERSE)
        
        path = os.getcwd() + "/media/"    
        count = 0
        songNumPair = {}
        for song in os.listdir(path):
            count = count + 1
            songNumPair[count] = song

            songStr = str(count) + ": " +  song
            songWindow.addstr(count,1,songStr,curses.A_DIM)
        songWindow.addstr(count + 1,1,"------------------",curses.A_DIM)
        
        self.stdscr.refresh()
        curses.echo()
        num = int(songWindow.getstr(count + 2,1,5))
        curses.noecho()
        del songWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop
    
        songPath = path + songNumPair[num]
        self.player.play(songPath.decode(encoding="utf-8"))
    

    def quit(self):
        self.player.stop()
        exit()
