words = str(input("Введите строку: ")) #Запрос строки от пользователя
words = words.lower() #Нижний регистр
for i in range(len(words)):  #Цикл
    if words[i]=="е": #Цикл
        print(i) #Вывод на экран