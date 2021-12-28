import sys

def isFile():
    try:
        file = open("TOKEN.txt", "r")
        if file == "Siia 1. reale kleepida kausta path (Selle teksti asemele)":
            print("Puudub muusika failide path. Loodi .txt fail nimega 'path', lisage sinna kausta path, kus on muusika failid")
            sys.exit()
        return file.read()
    except:
        print("Puudub muusika failide path. Loodi .txt fail nimega 'path', lisage sinna kausta path, kus on muusika failid")
        file = open("TOKEN.txt", "w")
        file.write("Siia 1. reale kleepida kausta path (Selle teksti asemele)")
        file.close()
        sys.exit()

#Kontrollib kas faili nimi on õpitud nimede listis
def isLearned(name, learned):
    if name in learned:
        return True
    else:
        return False

if __name__ == "__main__":
    print("K2ivita main fail")
    sys.exit()