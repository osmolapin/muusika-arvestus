import sys, os, random

#Suvalise faili valimine pathist
#Tagastab faili nime koos faili tüübiga (.mp3, .wav)
def randomFile(directory):
    filename = random.choice(os.listdir(directory))
    return filename

#Valib suvalise arvu ning jagab selle 10-ga et saada float
#Kasutatakse faili selleks, et faili keskelt alustada
def randomTimestamp():
    randomInt = random.randint(3,7)
    return randomInt/10

if __name__ == "__main__":
    print("K2ivita main fail")
    sys.exit()