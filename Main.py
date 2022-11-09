try:
    from zipfile import ZipFile
except:
    import os
    os.system("pip install ZipFile")
    from zipfile import ZipFile


def hacker_zip():
    def bbzip():
        print('''
    
    
    #$%^&*&^%$#@@   !#$        #$%^&*
             #@     *&!        *&@   #@
           #$       %$!        !@#  #@
          #         #@!        $#!#@
        &$          $#@        !@#
      $@            ^!@        ^%@
    $#*&^%$#@#$%^   #$%        &^%          HACKER
    
    
    ''')
    bbzip()
    zf = input(" Zip File : ")
    passlist = input("\n Password List : ")
    bbzip()
    zf = ZipFile(zf)
    tests = 0
    for password in open(passlist):
        password = password.strip("\n")
        print("Testing : {}".format(password))
        tests += 1
        try:
            zf.extractall(pwd=password.encode())
            print("-"*50)
            print("Password : {}     ||     {} Passwords Tested in {} seconds !".format(password,tests))
            break
        except :
            continue
    input("\n\n\n\n\t  Enter for close ")
# ================================================================

hacker_zip()
