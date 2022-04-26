from email import message
import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
    keyboard = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text="Туры", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Достопримечательности", callback_data="button2")
    button3 = types.InlineKeyboardButton(text="Отели", callback_data="button3")
    button4 = types.InlineKeyboardButton(text="Кафе", callback_data="button4")
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)

    bot.send_message(message.chat.id, text = "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот - Путеводитель. Выбери, то что тебя  интересует".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup = keyboard )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    kb = types.InlineKeyboardMarkup()  
    if call.message:
# Программа      
        if call.data == "mainmenu":
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(text="Туры", callback_data="button1")
            button2 = types.InlineKeyboardButton(text="Достопримечательности", callback_data="button2")
            button3 = types.InlineKeyboardButton(text="Отели", callback_data="button3")
            button4 = types.InlineKeyboardButton(text="Кафе", callback_data="button4")
            keyboard.add(button1)
            keyboard.add(button2)
            keyboard.add(button3)
            keyboard.add(button4)
            bot.send_message(call.message.chat.id, text="Меню",reply_markup=keyboard)

        if call.data == "button1":
            kb.add(
                types.InlineKeyboardButton(text="Культурные туры", callback_data="tur0")
            )
            kb.add(
                types.InlineKeyboardButton(text="Горные туры/Тарекинг🌄", callback_data="tur1"),
                types.InlineKeyboardButton(text="Конные туры🐎", callback_data="tur2")
            )
            kb.add(
                types.InlineKeyboardButton(text="Лыжные туры🎿", callback_data="tur3"),
                types.InlineKeyboardButton(text="Авто туры🚗", callback_data="tur4")
            )
            kb.add(
                types.InlineKeyboardButton(text="Каякинг⛵", callback_data="tur6")
            )
            kb.add(
                types.InlineKeyboardButton(text="Велотур🚴‍♂️", callback_data="tur7"),
                
            )
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Виды туров", reply_markup=kb)
  

        if call.data == "button2":
            kb.add(types.InlineKeyboardButton(text="Собор Святой Троицы - церковь🛕", callback_data="dost1"))
            kb.add(types.InlineKeyboardButton(text="Дунганская мечеть🕌", callback_data="dost2"))
            kb.add(types.InlineKeyboardButton(text="Исторический музей г.Каракол", callback_data="dost5"))
            kb.add(types.InlineKeyboardButton(text="Мемориальный музей Н.М.Пржевальского", callback_data="dost6"))
            kb.add(types.InlineKeyboardButton(text="Еще больше достопримечательностей➕", url="https://www.ski-karakol.com/karakol/dostoprimechatel6nosti.aspx"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))

            bot.send_message(call.message.chat.id, "Виды Достопримечательностей", reply_markup=kb)

        if call.data == "button3":
            kb.add(
                types.InlineKeyboardButton(text="Отели", callback_data="hotel1"),
                types.InlineKeyboardButton(text="Гостевые Дома", callback_data="hotel2")
            )
            kb.add(
                types.InlineKeyboardButton(text="Хостелы", callback_data="hotel3"),
                types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu")
            )

            bot.send_message(call.message.chat.id, "Где можно остановиться 😴?", reply_markup=kb)

        if call.data == "button4":
            kb.add(types.InlineKeyboardButton(text="Кафе", callback_data="kafe1"))
            kb.add(types.InlineKeyboardButton(text="Кафейня", callback_data="kafe2"))
            kb.add(types.InlineKeyboardButton(text="Ашлянфу", callback_data="kafe3"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))

            bot.send_message(call.message.chat.id, "Где можно поесть😋?", reply_markup=kb)



# Под программа ТУРЫ

        #КУЛЬТУРНЫЕ ТУРЫ
        af = types.InlineKeyboardMarkup()  
        aff = types.InlineKeyboardMarkup()  
        if call.data == "tur0":
            af.add(types.InlineKeyboardButton(text="Visit Karakol", callback_data="culturetourvisit"))
            af.add(types.InlineKeyboardButton(text="ECOTREK", callback_data="culturetoureco"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают <b>Культурные</b> туры:", parse_mode='html', reply_markup=af)

        if call.data == 'culturetourvisit':
            aff.add(types.InlineKeyboardButton(text="Сайт", url="https://visitkarakol.com/nomads_way"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            photo = open('static/cultureTour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Этот тур создан для людей, которые заинтересованы в знакомстве с основными достопримечательностями, культурой и любят делать удивительные фотографии живописных пейзажей без больших физических нагрузок. Подробности про тур вы можете узнать на сайте",  reply_markup=aff)

        if call.data == 'culturetoureco':
            aff.add(types.InlineKeyboardButton(text="Сайт", url="https://visitkarakol.com/nomads_way"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            photo = open('static/ecotrekTour1.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "В этом туре вы познакомитесь с культурой, традициями и бытом кочевников, бытом и развлечениями крупных городов, а также посетите живописные природные места, которыми славится Кыргызстан. Верховая езда, покорение горных вершин, пикники и охота, а также пляжный отдых на берегу озера Иссык-Куль – все это входит в программы кыргызского культурного тура. Подробности про тур вы можете узнать на сайте", reply_markup=aff)

            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))

        #ГОРНЫЕ ТУРЫ
        ae = types.InlineKeyboardMarkup()  
        aee = types.InlineKeyboardMarkup()  
        if call.data == "tur1":
            ab.add(types.InlineKeyboardButton(text="Bulak Say", callback_data="trekkingtour"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают <b>горные</b> туры:", parse_mode='html', reply_markup=ae)

        if call.data == 'trekkingtour':
            abb.add(types.InlineKeyboardButton(text="Сайт", url="http://karakoltour.kg/index.php/ru/kayaking"))
            photo = open('static/horsebackTour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Bulak Say Horseback and Trekking — это семейный туроператор, базирующийся в селе Жолголот, недалеко от города горных походов Каракол. Наша конная база расположена у подножия пастбища между Караколом и хребтом Терскей Ала-Тоо в 10 минутах езды на такси от центра города. Мы предлагаем конные и пешие туры от 1 до 10 дней по красивым долинам и перевалам Тянь-Шаня и ночевки в юртах с традиционной кыргызской едой и свежими молочными продуктами с нашей фермы.", parse_mode='html', reply_markup=aee)

            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))


        #АВТО ТУР
        ad = types.InlineKeyboardMarkup()  
        add = types.InlineKeyboardMarkup()  
        if call.data == "tur2":
            ad.add(types.InlineKeyboardButton(text="Visit Karakol", callback_data="horsbacktour"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают <b>авто</b> туры:", parse_mode='html', reply_markup=ad)

        if call.data == 'horsbacktour':
            abb.add(types.InlineKeyboardButton(text="Сайт", url="https://visitkarakol.com/"))
            photo = open('static/avtoTour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Мы рассказываем о Караколе, Кыргызстане все, что вы хотите знать! Взгляните на страну глазами туристов и самих жителей! Это идеальное место для внедорожных туров с посещением живописных ущелий и каньонов, долин и рек, гор и озер! Подробности про тур вы можете узнать на сайте", parse_mode='html', reply_markup=add)

            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))


        #ГОРНЫЕ ТУРЫ
        ae = types.InlineKeyboardMarkup()  
        aee = types.InlineKeyboardMarkup()  
        if call.data == "tur3":
            ab.add(types.InlineKeyboardButton(text="VISIT KARAKOL ", callback_data="skitour"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают <b>Лыжные</b> туры:", parse_mode='html', reply_markup=ae)

        if call.data == 'skitour':
            abb.add(types.InlineKeyboardButton(text="Сайт", url="https://visitkarakol.com/freeride_and_ski_tours_in_kyrgyzstan"))
            photo = open('static/skytour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Здесь у вас будет возможность отлично провести время, занимаясь фрирайдом и скитуром по Кыргызстану. Наши снежные горы относятся к горам Тянь-Шаня, географически обособленной стране с хорошо сохранившейся кочевой культурой. Подробности про тур вы можете узнать на сайте", parse_mode='html', reply_markup=aee)

            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))


        #Конные туры
        aс = types.InlineKeyboardMarkup()  
        aсс = types.InlineKeyboardMarkup()  
        if call.data == "tur4":
            aс.add(types.InlineKeyboardButton(text="Bulak Say", callback_data="horsbacktour"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают тууры <b>верховых езд:</b>", parse_mode='html', reply_markup=aс)

        if call.data == 'horsbacktour':
            aсс.add(types.InlineKeyboardButton(text="Сайт", url="http://karakoltour.kg/index.php/ru/kayaking"))
            photo = open('static/horsebackTour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Bulak Say Horseback and Trekking — это семейный туроператор, базирующийся в селе Жолголот, недалеко от города горных походов Каракол. Наша конная база расположена у подножия пастбища между Караколом и хребтом Терскей Ала-Тоо в 10 минутах езды на такси от центра города. Мы предлагаем конные и пешие туры от 1 до 10 дней по красивым долинам и перевалам Тянь-Шаня и ночевки в юртах с традиционной кыргызской едой и свежими молочными продуктами с нашей фермы. Подробности про тур вы можете узнать на сайте", parse_mode='html', reply_markup=aсс)

            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))


        #КАЯККИНГ
        ab = types.InlineKeyboardMarkup()  
        abb = types.InlineKeyboardMarkup()  
        if call.data == "tur6":
            ab.add(types.InlineKeyboardButton(text="Issyk-Kul Kayaking", callback_data="kayaking"))
            bot.send_message(call.message.chat.id, "Тур.компании, которые предлогают <b>каяккинг</b> туры: ", parse_mode='html', reply_markup=ab)

        if call.data == 'kayaking':
            abb.add(types.InlineKeyboardButton(text="Сайт", url="http://karakolhorsetrekking.blogspot.com/"))
            photo = open('static/kayakingTour.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Каякинг тур по озеру Иссык-Куль Предлагаем каякинг тур по озеру Иссык-Куль продолжительностью до 5 часов. Подробности про тур вы можете узнать на сайте", parse_mode='html', reply_markup=abb)

            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))


        #ВЕЛОТУР 
        if call.data == "tur7":
            bot.send_message(call.message.chat.id, "Пока что в разделе 'Велотур' отсуствует туры")

            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))



# Под программа ДОСТОПРИМЕЧАТЕЛЬНОСТЕЙ
        if call.data == "dost1":
            kb.add(types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/AHY9ZdA2nUJeDayMA"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/karakolcathedral.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Свято-Троицкая православная церковь🛕.  Это сооружение – классический пример Русской Православной Церкви XIX века. Изящное здание с деревянными стенами и причудливым орнаментом прочно стоит на каменном фундаменте. Пять золотых куполов украшают крышу Собора, внутри которого находится множество икон, в том числе и копия иконы Андрея Рублева «Святая Троица».", reply_markup=kb)

        if call.data == "dost2":
            kb.add(types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/fGuhF9crif9WYCyq9"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/karakoldunganmosque.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Дунганская мечеть🕌 - одна из самых интересных достопримечательностей города Каракол. Дизайн и проект мечети выдержаны согласно принципам китайской архитектуры времен империи Цин. Мечеть без единого гвоздя", reply_markup=kb)

        if call.data == "dost5":
            kb.add(types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/ceYRFM4w3FJV16UA7"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/museum.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Каракольский историко-краеведческий музей был основан в 1948 году. Экспонаты музея отражают историю развития края, его природные богатства, развитие промышленности, сельского хозяйства, культуры, образования, здравоохранения и рассказывают об известных людях области.", reply_markup=kb)

        if call.data == "dost6":
            kb.add(types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/6CHQKMpCD6BovG286"))
            kb.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/mermalnyimusei.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Главной достопримечательностью Каракола конечно же является парк-заповедник с могилой и мемориалом Н.М.Пржевальского . В 9 км к северу от города, недалеко от пристани в Каракольском заливе среди парка находятся музей, памятник и могила Н. М. Пржевальского. На пути в свое 5-е путешествие Пржевальский умирает в городе Каракол и по его желанию он похоронен на берегу Иссык-Куля. Он находится на самой высокой точке восточной части Иссык-Кульского побережья. Так что вид отсюда открывается просто необыкновенный: величественная панорама озера и голубые шапки гор. Как бы охраняя вход в парк, по бокам ворот на высоких постаментах застыли козероги-тэке", reply_markup=kb)





# Под программа Отели    
        if call.data == "hotel1":
            #1
            kk = types.InlineKeyboardMarkup()
            kk.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/REUP3jyqLVLpy22K8"),
                types.InlineKeyboardButton(text="Бронирование", url="https://karagat-hotel-karakol.nochi.com/")
            )
            ll.add(
                types.InlineKeyboardButton(text="Контакты: +996776677777", callback_data="contacty")
            )
            photo = open('static/karagat-hotel.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Карагат",parse_mode='html', reply_markup=kk)

            #2
            ll = types.InlineKeyboardMarkup()

            ll.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/aYhP5k9dQhwCK3cQA"),
                types.InlineKeyboardButton(text="Бронирование", url="https://www.booking.com/hotel/kg/dd1-4d-n.ru.html?aid=318615&label=Russian_Kyrgyzstan_RU_KG_29377901185-_LNFadyyFJxSoSSqNZCUlQS111450060385%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi10638584468%3Atiaud-294889297133%3Adsa-320367708406%3Alp9070442%3Ali%3Adec%3Adm&sid=f173aeeb6b0ef9b7a21bba06597de56d&dest_id=-2331996;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1650787367;srpvid=ad5a3893cdd500f9;type=total;ucfs=1&#hotelTmpl")
            )
            ll.add(
                types.InlineKeyboardButton(text="Контакты: +996776677777", callback_data="contacty")
            )

            photo = open('static/amir-hotel.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>2)</b>Амир",parse_mode='html', reply_markup=ll)

            #3
            mm = types.InlineKeyboardMarkup()
            mm.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.booking.com/city/kg/karakol.ru.html?aid=319915;label=karakol-nsIDLr0ukzAYECiYwmobWgS275096107816:pl:ta:p1:p2:ac:ap:neg:fi:tikwd-39720801976:lp9070442:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YdQLqCSGZAFDHKNAytkZCCU;ws=&gclid=Cj0KCQjw6pOTBhCTARIsAHF23fJZ2p28EMP5Kb4YUk9rXgp35NrKvEPBCMn2hqqn6ODDm9yHw-AG-ZcaAsBkEALw_wcB"))
            mm.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/hotels.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше Отелей по ссылке👇",parse_mode='html', reply_markup=mm)



# Под программа Гостевой Дом    
        if call.data == "hotel2":
            #1
            nn = types.InlineKeyboardMarkup()
            nn.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/hotel-altai-kg?share"),
                types.InlineKeyboardButton(text="Бронирование", url="https://www.booking.com/hotel/kg/guest-house-altay.ru.html?aid=315714&label=guest-house-altay-PntHSJ7WT4xWLwJVVPgLeQS442453470933%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-180775626966%3Alp9070442%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YQB9rNbOPxnnhY6p2cOLx0E&sid=f173aeeb6b0ef9b7a21bba06597de56d&dest_id=-2331996;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1650787955;srpvid=6f7c39b8c6500068;type=total;ucfs=1&#hotelTmpl")
            )
            nn.add(
                types.InlineKeyboardButton(text="Контакты: +996776677777", callback_data="contacty")
            )
            photo = open('static/altay-guesthouse.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Гостевой Дом Altay",parse_mode='html', reply_markup=nn)

            #2
            oo = types.InlineKeyboardMarkup()
            oo.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/aYhP5k9dQhwCK3cQA"),
                types.InlineKeyboardButton(text="Бронирование", url="https://www.booking.com/hotel/kg/tikhii-ugholok.ru.html?aid=1149971&label=karakol-PPCTJg56Fs1W3eKyi%2A9UIgS390176536984%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565747%3Akwd-66950393424%3Alp9070442%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YXL5GV3cgz10S2LDvGAHUOI&sid=f173aeeb6b0ef9b7a21bba06597de56d")
            )
            oo.add(
                types.InlineKeyboardButton(text="Контакты: +996776677777", callback_data="contacty")
            )
            photo = open('static/gueshouseeles.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Гостевой Дом Eles",parse_mode='html', reply_markup=oo)

            #3
            mm = types.InlineKeyboardMarkup()
            mm.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.booking.com/guest-house/city/kg/karakol.ru.html?aid=1149971&label=karakol-PPCTJg56Fs1W3eKyi%2A9UIgS390176536984%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atiaud-1110454565747%3Akwd-66950393424%3Alp9070442%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YXL5GV3cgz10S2LDvGAHUOI&sid=f173aeeb6b0ef9b7a21bba06597de56d&keep_landing=1&gclid=Cj0KCQjw6pOTBhCTARIsAHF23fLIEDEbnC2BNuqenj1QivuwpYkHl6DWvLMte56tOh48-OCwUp3oBQgaAgK2EALw_wcB&"))
            mm.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/guest_house.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше Гостевых домов по ссылке👇",parse_mode='html', reply_markup=mm)



# Под программа Хостелы   
        if call.data == "hotel3":
            #1
            pp = types.InlineKeyboardMarkup()
            pp.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/duethostel?share"),
                types.InlineKeyboardButton(text="Бронирование", url="https://www.russian.hostelworld.com/hosteldetails.php/Snow-Leopard-Hostel/Karakol/299894")
            )
            pp.add(
                types.InlineKeyboardButton(text="Контакты: +996776677777", callback_data="contacty")
            )
            photo = open('static/showleopardHostel.webp', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Хостел Snow Leopard", parse_mode='html', reply_markup=pp)

            #2
            qq = types.InlineKeyboardMarkup()
            qq.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/duethostel?share"),
                types.InlineKeyboardButton(text="Бронирование", url="https://www.russian.hostelworld.com/hosteldetails.php/Duet-Hostel/Karakol/272558")
            )
            qq.add(
                types.InlineKeyboardButton(text="Контакты: +996776677777", callback_data="contacty")
            )

            photo = open('static/duetHostel.webp', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Duet hostel",parse_mode='html', reply_markup=qq)

            #3
            rr = types.InlineKeyboardMarkup()
            rr.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.russian.hostelworld.com/khostely/Karakol/Kirgizia?source=ppc_gooads_nonbrand_dsk_search_ds_ru_row&network=g&campaign_id=15296631596&adgroup_id=128648200054&criteria_id=kwd-844803786662&creative_id=571201068429&location_physical_id=9070442&location_interest_id=&adposition=&uniqueclickID=1270539567961807976&sub_keyword=hostel%2520karakol&sub_ad=e&sub_publisher=ADW&gclsrc=aw.ds&gclid=Cj0KCQjw6pOTBhCTARIsAHF23fKr6vpeJVQR3pbJE7FRUXLQoudQ0je6jvtloGOWqjzh-Bu4fh-5tCMaAgmfEALw_wcB")),
            rr.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/guest_house.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше Хостелов по ссылке👇",parse_mode='html', reply_markup=rr)



# Под программа КАФЕЩЕК: Кафе
        if call.data == "kafe1":
            #1
            kb.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/WmqDi9pM4Mca4jX67"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://www.tripadvisor.ru/ShowUserReviews-g815340-d3952646-r190813567-Cafe_Zarina-Karakol_Issyk_Kul_Province.html")
            )
            kb.add(
                types.InlineKeyboardButton(text="Меню", url="https://media-cdn.tripadvisor.com/media/photo-s/10/16/df/c6/cafe-zarina.jpg"),
                types.InlineKeyboardButton(text="Контакты: +996777777777", callback_data="contacty")
            )
            
            photo = open('static/zarinKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b> кафе Зарина",parse_mode='html', reply_markup=kb)

            #2
            aa = types.InlineKeyboardMarkup()
            photo = open('static/altynkumaraKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            aa.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/n2aZ2Bi7NkE88fLm6"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://www.tripadvisor.ru/Restaurant_Review-g815340-d13313936-Reviews-Altyn_Kumara-Karakol_Issyk_Kul_Province.html")
            )
            aa.add(
                types.InlineKeyboardButton(text="Меню", url="https://www.instagram.com/stories/highlights/17903538839038951/"),
                types.InlineKeyboardButton(text="Контакты: +996777777777", callback_data="cont")
            )

            bot.send_message(call.message.chat.id, "<b>2)</b> кафе Алтын Кумара",parse_mode='html', reply_markup=aa)

            #3
            bb = types.InlineKeyboardMarkup()
            bb.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/cafe_dastorkon?share"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://www.tripadvisor.ru/Restaurant_Review-g815340-d6481971-Reviews-Ethnic_Cafe_Dastorkon-Karakol_Issyk_Kul_Province.html")
            )
            bb.add(
                types.InlineKeyboardButton(text="Меню", url="https://www.instagram.com/stories/highlights/17882963158335616/"),
                types.InlineKeyboardButton(text="Контакты: +996777777777", callback_data="coпаntacty")
            )
            
            photo = open('static/dastarkonKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>3)</b> кафе Дастаркон",parse_mode='html', reply_markup=bb)

            #4
            cc = types.InlineKeyboardMarkup()
            cc.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.tripadvisor.ru/Search?q=%D0%BA%D0%B0%D1%84%D0%B5&searchSessionId=496BF566B033821C632CE1B21ED455D41650760078349ssid&searchNearby=false&geo=815340&sid=D0B03FB321A0422180BFF0D3F6956E3A1650760305616&blockRedirect=true"))
            cc.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/foodKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше кафе по ссылке👇",parse_mode='html', reply_markup=cc)     


# Под программа КАФЕЩЕК: Кафейня
        if call.data == "kafe2":
            #1
            dd = types.InlineKeyboardMarkup()
            dd.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/sierra-coffee-karakol?share"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://sierra.madanur.com/")
            )
            dd.add(
                types.InlineKeyboardButton(text="Меню", url="https://sierra.madanur.com/shop-2/"),
                types.InlineKeyboardButton(text="Контакты: +996777677777", callback_data="contacty")
            )
            
            photo = open('static/sierraCoffee.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b> Кофейня SIERRA Coffee Karakol",parse_mode='html', reply_markup=dd)

            #2
            ee = types.InlineKeyboardMarkup()
            photo = open('static/lighthouseCoffee.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            ee.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://goo.gl/maps/QzDeWcYmWSyBegsK7"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://www.tripadvisor.ru/Restaurant_Review-g815340-d12941444-Reviews-Lighthouse_Coffee_Tea-Karakol_Issyk_Kul_Province.html")
            )
            ee.add(
                types.InlineKeyboardButton(text="Меню", url="https://www.instagram.com/stories/highlights/17917457425550379/"),
                types.InlineKeyboardButton(text="Контакты: +996587777777", callback_data="cont")
            )

            bot.send_message(call.message.chat.id, "<b>2)</b> Кофейня Karakol Lighthouse",parse_mode='html', reply_markup=ee)

            #3
            ff = types.InlineKeyboardMarkup()
            ff.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://g.page/meetingpoint-karakol?share"),
                types.InlineKeyboardButton(text="Ссылка на сайт", url="https://duetkarakol.wordpress.com/meeting-point/")
            )
            ff.add(
                types.InlineKeyboardButton(text="Меню", url="https://www.instagram.com/stories/highlights/17901924169981459/"),
                types.InlineKeyboardButton(text="Контакты: +996777777777", callback_data="coпаntacty")
            )
            
            photo = open('static/meetingpointCoffee.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>3)</b> Кофейня Meeting Point",parse_mode='html', reply_markup=ff)

            #4
            gg = types.InlineKeyboardMarkup()
            gg.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.tripadvisor.ru/Search?q=%D0%9A%D0%BE%D1%84%D0%B5%D0%B9%D0%BD%D1%8F&searchSessionId=E1F43A879460082504B36AB7B431BD701650761090729ssid&searchNearby=false&geo=12257498&sid=D0B03FB321A0422180BFF0D3F6956E3A1650761097726&blockRedirect=true&rf=1"))
            gg.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/cupofcoffee.JPG', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше Кофейни по ссылке👇",parse_mode='html', reply_markup=gg)    

# Под программа КАФЕЩЕК: Ашлянфу    
        if call.data == "kafe3":
            #1
            hh = types.InlineKeyboardMarkup()
            hh.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://go.2gis.com/qkr9f"),
                types.InlineKeyboardButton(text="Контакты: +996776677777", callback_data="contacty")
            )
            
            photo = open('static/ashlianySaidyfuKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "<b>1)</b>Ашлянфу у Саиды",parse_mode='html', reply_markup=hh)

            #2
            ii = types.InlineKeyboardMarkup()
            photo = open('static/ashlianfuKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            ii.add(
                types.InlineKeyboardButton(text="Ссылка на карту", url="https://go.2gis.com/qkr9f"),
                types.InlineKeyboardButton(text="Контакты: +996774677777", callback_data="contacty")
            )

            bot.send_message(call.message.chat.id, "<b>2)</b>Ашлянфу",parse_mode='html', reply_markup=ii)

            #3
            jj = types.InlineKeyboardMarkup()
            jj.add(types.InlineKeyboardButton(text="Ссылка", url="https://www.tripadvisor.ru/Search?q=%D0%9A%D0%BE%D1%84%D0%B5%D0%B9%D0%BD%D1%8F&searchSessionId=E1F43A879460082504B36AB7B431BD701650761090729ssid&searchNearby=false&geo=12257498&sid=D0B03FB321A0422180BFF0D3F6956E3A1650761097726&blockRedirect=true&rf=1"))
            jj.add(types.InlineKeyboardButton(text="Назад в меню⏪", callback_data="mainmenu"))
            
            photo = open('static/ashlianfuгKafe.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)

            bot.send_message(call.message.chat.id, "Еще больше Ашлянфу по ссылке👇",parse_mode='html', reply_markup=jj) 

        # if call.message.data == "menu":
        # bot.send_message(call.message.message.id, '''\n\n✅ Вы в главном меню\n\n''', parse_mode='HTML', reply_markup=keyboard())    
bot.polling(none_stop=True)