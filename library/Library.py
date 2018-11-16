import os
import sys

class Library:
    
    def __init__(self):
        self.folderPath = os.getcwd() + "/media/"
        self.updateLibrary()

    '''change folder path'''    
    def setPath(self,path):
        self.folderPath = path
        self.updateLibrary()
        
    '''return the value in the song dictionary'''
    def getSong(self,num):
        return self.folderContents[num]

    '''return size of the library'''
    def getNumFiles(self):
        return self.numFiles

    '''return full path to this library'''
    def getPath(self):
        return self.folderPath

    def getFolderName(self):
        return self.folderName

    '''change all the data associated with the path'''
    def updateLibrary(self):
        #slicey slicey to get the name of the directory
        #https://stackoverflow.com/questions/7253803/how-to-get-everything-after-last-slash-in-a-url
        self.folderName = self.folderPath.rsplit('/',1)[-1]
        self.folderContents = {}
        self.numFiles = 0
        
        #sift through the directory for wave files
        for item in os.listdir(self.folderPath):
            
            #file extension is for wave
            if item[-4:] == '.wav':
                self.numFiles = self.numFiles + 1
                self.folderContents[self.numFiles] = item




