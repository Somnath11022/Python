def main():
    print("Demonstration of sequence Data Types ")

    ldata = [ 10,20,30,40]      #List

    tdata = ( 10,20,30,40)      #Tuple

    sdata = {10,20,30,40}       #Set

    ddata = { "C":400, "C++":550 , "Java":900 , "Python":890}     #Dictinary

    print(ldata)
    print(tdata)
    print(sdata)
    print(ddata)

    print(type(ldata))
    print(type(tdata))
    print(type(sdata))
    print(type(ddata))

if __name__ == "__main__":
    main()