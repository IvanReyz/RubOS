while True:

    import socket

    f = open('usr/usr.txt');

    com = input(f.read() + "@" + socket.gethostname() + ":~# ")

    if com == "rbs file":

        namefile = input("Select a name for file: ");
        f = open("usr/files/" + namefile, 'x');
        textfile = input("Write the text of file: ");
        f.write(textfile);
        f.close();
        print("");
        print('File ' + namefile + ' saved!');
        print("");

    if com == "rbs version":

        f = open('usr/usr.txt');
        print("");
        print("RubOS v0.0.1 Alpha.");
        print("License owner: " + f.read()); 
        print("All Rights Reserved.");
        print("");

    if com == "rbs thanks":

        print("");
        print("Max Salzberg - Design group");
        print("");

    if com == "rbs exit":

        import exiter

    if com == "rbs calculator":

        select = input("Select calculator type: Multiplication(1), Division(2), Addition(3), Subtraction (4): ");

        if select == "1":

            input_1 = int(input("First number: "));
            input_2 = int(input("Second number: "));
            res = input_1 * input_2
            print("");
            print('Result is:', res);

        if select == "2":

            input_1 = int(input("First number: "));
            input_2 = int(input("Second number: "));
            res = input_1 / input_2
            print("");
            print('Result is:', res);

        if select == "3":

            input_1 = int(input("First number: "));
            input_2 = int(input("Second number: "));
            res = input_1 + input_2
            print("");
            print('Result is:', res);

        if select == "4":

            input_1 = int(input("First number: "));
            input_2 = int(input("Second number: "));
            res = input_1 - input_2
            print("");
            print('Result is:', res);

    if com == "rbs help":

        print("");
        print("rbs version - RubOS version");
        print("rbs file - Create file");
        print("rbs exit - Exit system");
        print("rbs calculator - RubOS calculator");
        print("rbs thanks - RubOS thanks");
        print("");

    if com == "rbs update":

        import zipfile
        import os

        from subprocess import call

        call(["wget", "http://colorfull.host/dnttch/update.zip"]) 
        fantasy_zip = zipfile.ZipFile('update.zip')
        fantasy_zip.extractall(os.getcwd())
 
        fantasy_zip.close()
        os.remove("update.zip")
        
        clear = lambda: os.system('cls')
        clear()
        exit(0)   