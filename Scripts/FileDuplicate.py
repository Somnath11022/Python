#It is an autoomation script which displays Duplicate files using Checksum of file on console
import os
from sys import *
import hashlib
import time


def hashfile(path , blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()

    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    print("----------Inside Duplicate Finder ----------")
    print("Name of input directory : ",path)

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    dups = {}
    if exists:

        for foldername, subfolder, filename in os.walk(path):
            print("Current Folder is "+foldername)
            for fnames in filename :
                path = os.path.join(foldername,fnames)
                file_hash = hashfile(path)
                if file_hash in dups :
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]
           
        return dups
    else:
        print("Invalid Path")

def PrintDuplicate(dict1):
        results = list(filter(lambda x : len(x)>1,dict1.values()))

        if len(results)>0:
            print("Duplicates Found ")

            print("The Following Files are identical ")

            icnt = 0
            for result in results:
                for subresults in result:
                    icnt += 1
                    if icnt >=2:
                        print("\t\t%s"%subresults)
                        print("--------------------------------------------------")

        else:
            print("No Duplicates found ")



        
def main():
    print("----------Directory CheckSum reader--------")
    print("Application name :"+argv[0])

    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    if(len(argv) != 2):
        print("Insufficient arguments")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)
    except ValueError:
        print("Error : Invalid datatype of input")
if(__name__ =="__main__"):
    start_time = time.time()
    main()
    end_time = time.time()
    print("Total time required is :",int(end_time))