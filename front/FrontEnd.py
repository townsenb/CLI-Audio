import curses
import curses.textpad
import os
import sys

class FrontEnd:

    def __init__(self, player,library):
        self.player = player
        self.library = library
        self.player.play(sys.argv[1])
        curses.wrapper(self.menu)

    def menu(self, args):
        self.stdscr = curses.initscr()
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "f - Switch folder")
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
            elif c == ord('f'):
                self.switchFolder()

    '''change the directory for songs'''
    def switchFolder(self):
        dirWindow = curses.newwin(4,50,5,35)
        dirWindow.border()
        dirWindow.addstr(0,0,"Enter library path", curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = dirWindow.getstr(1,1,96)
        curses.noecho()
        del dirWindow
        self.stdscr.refresh()
        self.library.setPath(path)       
        self.stdscr.addstr(20,10,"                                     ")
        self.stdscr.addstr(20,10,"Active library: " + self.library.getFolderName())



    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())


    '''Made changing songs easier? '''
    def changeSong(self):
        songWindow = curses.newwin(20,30,10,40)
        songWindow.border()
        songWindow.addstr(0,0,"Type song number:", curses.A_REVERSE)
       
        path = self.library.getPath()

        #list songs in the media directory
        numFiles = self.library.getNumFiles()
        for key in range(1,numFiles+1):
            song = ""
            try:
                song = self.library.getSong(key)
            except KeyError:
                print("*Key Error*")
            songStr = str(key) + ": " +  song
            songWindow.addstr(key,1,songStr,curses.A_DIM)
        songWindow.addstr(numFiles + 1, 1, "------------------",curses.A_DIM)

        
        self.stdscr.refresh()
        curses.echo()
        num = int(songWindow.getstr(numFiles + 2,1,5))
        curses.noecho()
        del songWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop()
        
        songPath = path + "/" + self.library.getSong(num)
        self.player.play(songPath.decode(encoding="utf-8"))
    

    def quit(self):
        self.player.stop()
        exit()
