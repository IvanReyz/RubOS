import os
import sys
import datetime

clear = lambda: os.system('cls')
clear()

usr = "usr/usr.txt";

if os.path.exists(usr):
    if os.path.isfile(usr):

        f = open('usr/usr.txt');
        print("");
        print("");
        print("Welcome to RubOS, " + f.read() + "!");
        print("");
        print("Commands:    rbs help");
        print("Update:      rbs update");
        print("");

        updated = "usr/updated.txt";

        if os.path.exists(updated):
            if os.path.isfile(updated):

                print("RubOS successful updated!");

        print("");
        from modules import commander

else:

    f = open("usr/usr.txt", 'x');
    print("");
    textfile = input("Write your name or nickname: ");
    f.write(textfile);
    f.close();

    clear()
    f = open('usr/usr.txt');
    print("");
    print("Welcome to RubOS, " + f.read() + "!");
    print("");
    print("Commands:    rbs help");
    print("Update:      rbs update");
    print("");
    from modules import commander