import os
import gits

#you need to put this file at your project management folder and create React and Angular folders

currentPath = os.getcwd()
print(currentPath)
frameWork = 0
name = input('Project Name : ').lower()

while(1):
    try:
        print("what FrameWork you wanna use (react/angular) : \n")
        print("1-React.\n")
        print("2-Angular.\n")
        frameWork = int(input("Chose : "))
    except:
        print("check the frameWork Name again !")

    if(  ( frameWork == 1 or frameWork == 2  ) ):
        break

if(frameWork == 1 ):
    if(frameWork == 1 ):
        while (1):
            choice = 0
            try:
                print("you are using vanilla react or ?\n")
                print("1-Vanilla react . \n")
                print("2-GatsbyJS . \n")
                choice =int(input("Chose : "))
            except :
                print("Choise should be 1 or 2")

            if(choice==1):
                os.chdir(f"{currentPath}/React")
                currentPath = os.getcwd()
                print("changed path to : ", os.getcwd())

                print(f"We are using React now Let's role !")
                os.system(f"npx create-react-app {name}")
                os.chdir(f"{currentPath}/{name}")
                print("changed path to : ", os.getcwd())

                gits.giting(name)
                #os.system("code .")
                os.system("code-insiders .")
                os.system("npm start")
                break

            elif(choice==2):
                currentPath = os.getcwd()
                url=input("Url of the starter Template :\n")
                os.system(f"gatsby new {name}")

                os.chdir(f"{currentPath}/{name}")
                print("changed path to : ", os.getcwd())
                gits.giting(name)
                #os.system("code .")
                os.system("code-insiders .")
                os.system("npm start")

                break

elif (frameWork == 2 ):
    os.chdir(f"{currentPath}/Angular")
    currentPath = os.getcwd()
    print("We are using Angular now Let's role!")

    os.system(f"ng new {name}")
    os.chdir(f"{currentPath}/{name}")
    print("changed path to : ", os.getcwd())

    gits.giting(name)
    #os.system("code .")
    os.system("code-insiders .")
    os.system("ng serve --open")

#if you use vs code the blue one activate the os.system("code .")


input("Press any key to quit console!")

