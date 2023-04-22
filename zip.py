import subprocess

import shutil
def zip():
    user_input = input("You want unzip or zip:")
    if user_input == "zip":
        subprocess.Popen(r'explorer "C:\Users\Administrator\PycharmProjects\idk man\put_files_to_be_zipped"')
        path_to_the_file = input("Whats the path of the file?\n")

        b = input("The name of the zip:")

        shutil.make_archive(r"C:/" + b, "zip", path_to_the_file)
    elif user_input == "unzip":
        c = input("Path of the file:\n")
        d = input("The name of file ")
        shutil.unpack_archive( c + ".zip","C:/" + d , "zip")





