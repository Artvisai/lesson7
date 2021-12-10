from os import name, listdir, getcwd, getlogin

print("Имя операционной системы: {}".format(name))
print("Имя пользователя: {}".format(getlogin()))
print("Список файлов и директорий в папке: {}".format(listdir(getcwd())))
