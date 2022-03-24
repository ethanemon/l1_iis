cat = input ("Любите котиков?")
if cat =="нет":
    print ("Пшел вон")
elif cat == "да":
    ans1 = input ("Ты богач или хочешь взять из приюта?(Богач/приют)")
    if ans1 == "богач":
        choose = input("Какие котики тебе больше нравятся? (Вислоухие/с прямыми ушками)")
        if choose == "вислоухие":
            wool = input ("Короткая шерсть или длинная?")
            if wool == "короткая шерсть":
                print ("скоттиш-фолд ваш вариант")
            else: print ("хайленд-фолд ")
        elif choose == "с прямыми ушками":
            wool = print ("Короткая шерсть или длинная?")
            if wool == "длинная шерсть":
                print("хайленд-страйт  ваш вариант")
            else: print ("скоттиш-страйт")
    elif ans1 == "приют":
        location = input ("В каком ты городе? (Москва, Питер, Екб)")
        if location == "Москва":
            print ("Вот несколько ссылок: https://murkosha.ru/; https://www.friendforpet.ru/pets/cats; https://izpriuta.ru/vzyat-koshku")
        elif location == "Питер":
            print ("Вот несколько ссылок: http://newdomcat.ru/; https://kudago.com/spb/list/bratya-nashi-menshie-koshachi-priyuty/")
        elif location == "Екб":
            print ("Вот несколько ссылок: https://vk.com/leopold_ekb")