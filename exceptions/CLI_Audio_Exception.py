


class CLI_Audio_Exception(Exception):
    """Parent exception for CLI-audio app"""
    pass

class CLI_Audio_File_Exception(CLI_Audio_Exception):
    """Trouble opening a file"""
    pass

class CLI_Audio_Screen_Size_Exception(CLI_Audio_Exception):
    """Screen size too small"""
    pass



#https://www.programiz.com/python-programming/user-defined-exception
