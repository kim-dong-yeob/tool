import zipfile

def crackzip(zfile, passwd):
    try:
        zfile.extractall(pwd=passwd)
        print('ZIP file extractall successfully! PASS=[%s]' %passwd.decode())
        return True
    
    except:
        pass
    
    return False

if __name__=="__main__":
    
    dicstr = input("dictionaryName : ")
    zipfilename = input("zipfileName : ")
    
    zfile = zipfile.ZipFile(zipfilename, 'r')
    pfile = open(dicstr, 'r')

    for line in pfile.readlines():
        passwd = line.strip('\n')
        crackzip(zfile, passwd.encode("utf-8"))
    
