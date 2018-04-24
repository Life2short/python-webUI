import os
import CommonLibrary.CommonConfiguration as cc

def GetRunDirectory():
    allRunFolders = []
    for fd in os.listdir(cc.Logs_PATH):
        if fd.startswith("TestRun"):
            fd = cc.Logs_PATH + "\\" + fd
            if os.path.isdir(fd):
                allRunFolders.append(fd)
    latestFolder = max(allRunFolders, key=os.path.getmtime)
    return latestFolder

