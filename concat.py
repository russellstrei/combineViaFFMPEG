import PySimpleGUI as sg
import glob
import pathlib
import os

### ----------------------------------------------------------------------
### Lots of Credit goes to Googling.  Hope this helps.
### Basically alot of Google, Copy Paste and glueing everything together.
### ----------------------------------------------------------------------

processList = "" 
dir = ""
def scanDir(directory):
    ###Walk Directory and find all mp4 videos, add to processList.txt
    chkDir(directory.replace('/','\\'))
    print(processList)
    for name in glob.glob(directory +"\\"+ '*.mp4'):
        print(name)
        file1 = open(processList, "a")  # append mode
        file1.write("file '" + name + "'\n")
        file1.close()
    execute()

def chkDir(directory):
    ###Check Directory for existing processList.txt file, delete if found + outputfile
    global processList
    global dir
    dir = directory + "\\"
    file = pathlib.Path(directory + "\\processList.txt")
    processList = directory + "\\processList.txt"
    output = directory + "\\output.mp4"
    outputFile = pathlib.Path(directory + "\\output.mp4")
    if file.exists ():
        print ("Process File exist, deleting...\n\n")
        os.remove(processList)
        if outputFile.exists ():
            os.remove(output)

def execute():
    ###Building ffmpeg command + executing it
    cmd = "ffmpeg -f concat -safe 0 -i " + processList + " -c copy "+ dir + "output.mp4"
    print ("\n\n====================================\nExecuting Command: " + cmd)
    print ("====================================\n\n")
    os.system(cmd)

def start():
    ###Setting Dialog Box
    sg.theme("DarkTeal2")
    layout = [[sg.T("")], [sg.Text("Choose a folder: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],[sg.Button("Submit")],[sg.Button("Exit")]]

    ###Building Window
    window = sg.Window('My File Browser', layout, size=(600,150))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            exit()
        elif event == "Submit":
            directory = values["-IN-"]
            print("Directory Selected: " + directory + ":\n\n")
            scanDir(directory)

start()
