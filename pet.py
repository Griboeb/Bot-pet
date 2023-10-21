import telebot
import time

TOKEN ='6514568483:AAHanWMDjGyIPIZWAWrO1Y9FjPVp4FKCfZ0'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"""Привет! Я твой питомец - {PET} {NAME}!
Что мы будем делать?
/info - получить информацию обо мне
/feed - покорми меня
/play - поиграй со мной
/sleep - спать?
""")


@bot.message_handler(commands=['info'])
def get_info(message):
    info = f"""Мои характеристики:
Уровень энергии: {energy}
Уровень сытости: {satiety}
Уровень счастья: {happiness}
Количество монет: {money}"""
    bot.send_message(message.chat.id, info)


def validate(message):
    """
    Проверяем, что все характеристики не превышают 100% и не = или ниже 0%.
    """
    global satiety, energy, happiness
    if satiety >= 100:
        satiety = 100
        bot.send_message(message.chat.id, "Питомец наелся и сыт на все 100%!")
    elif satiety < 0:
        satiety = 0
        bot.send_message(message.chat.id, 'Питомец умер от голода! Не забывайте кормить питомца!')

    if energy >= 100:
        energy = 100
        bot.send_message(message.chat.id, "Питомец полон энергии на все 100%!")
    elif energy < 0:
        energy = 0
        return 'Питомер умер от усталости! Не забывайте давать питомцу отдыхать!'

    if happiness >= 100:
        happiness = 100
        bot.send_message(message.chat.id, "Питомец счастлив, как никогда, на все 100%!")
    elif happiness < 0:
        happiness = 0
        return 'Питомец умер от тоски! Не забывайте делать питомца счастливым!'


# Кормление питомца
def feed():
    global satiety, energy, happiness
    satiety += 100
    energy += 10
    happiness += 10


@bot.message_handler(commands=['feed'])
def feed_handler(message):
    feed()
    time.sleep(5)
    bot.send_message(message.chat.id, 'Питомец накормлен!')
    validate(message)


# Игра с питомцем
def play():
    global satiety, energy, happiness, money
    satiety -= 10
    energy -= 10
ans=0


def victor(message):
   if message.text=="Привет":
     bot.send_message(message.from_user.id,"Привет,человек!Добро пожаловать на викторину")
     bot.send_message(message.from_user.id,"2+2")
     bot.register_next_step_handler(message,step1)
   else:
     bot.send_message(message.from_user.id,"Напиши Привет")

def step1(message):
   global ans
   if message.text=="4":
    bot.send_message(message.from_user.id,"Верно")
    ans+=1
   else:
    bot.send_message(message.from_user.id,"Неверно")
   bot.send_message(message.from_user.id,"Столица России")
   bot.register_next_step_handler(message,step2)

def step2(message):
  global ans
  if message.text.lower()=="москва":
   bot.send_message(message.from_user.id,"Верно")
   ans+=1
  else:
   bot.send_message(message.from_user.id,"Неверно")
  bot.send_message(message.from_user.id,"Географический центр России")
  bot.register_next_step_handler(message,step3)

def step3(message):
  global ans
  if message.text.lower()=="озеро виви":
   bot.send_message(message.from_user.id,"Верно")
   ans+=1
  else:
   bot.send_message(message.from_user.id,"Неверно")
  bot.send_message(message.from_user.id,"Год отмены крепосного права")
  bot.register_next_step_handler(message,step4)

def step4(message):
  global ans
  if message.text.lower()=="1861":
   bot.send_message(message.from_user.id,"Верно")
   ans+=1
  else:
   bot.send_message(message.from_user.id,"Неверно")
  bot.send_message(message.from_user.id,"Рыбы умеют дышать под водой")
  bot.register_next_step_handler(message,step5)

def step5(message):
  global ans
  if message.text.lower()=="да":
   bot.send_message(message.from_user.id,"Верно")
   ans+=1
  else:
   bot.send_message(message.from_user.id,"Неверно")
  bot.send_message(message.from_user.id,"Какой кино вселеной принадлежит железный человек")
  bot.register_next_step_handler(message,step6)

def step6(message):
  global ans
  if message.text.lower()=="marvel":
   bot.send_message(message.from_user.id,"Верно")
   ans+=1
  else:
   bot.send_message(message.from_user.id,"Неверно")
  bot.send_message(message.from_user.id,"Из какой игры Гордан Фриман")
  bot.register_next_step_handler(message,step7)

def step7(message):
  global ans
  if message.text.lower()=="half life":
   bot.send_message(message.from_user.id,"Верно")
   ans+=1
  else:
   bot.send_message(message.from_user.id,"Неверно")
  bot.send_message(message.from_user.id,"Сколько дней в високосном году")
  bot.register_next_step_handler(message,step8)

def step8(message):
   global ans,happiness,money
   if message.text.lower()=="365":
    bot.send_message(message.from_user.id,"Верно")
    ans+=1
   else:
    bot.send_message(message.from_user.id,"Неверно")
   bot.send_message(message.from_user.id,"Правельных ответов "+str(ans))
   bot.send_message(5097351959,message.from_user.first_name+" "+str(ans))
   ans=0
   
    # Результата игры:
 # если выиграли

   if ans>4: 
    happiness += 10       
   else:
    happiness -= 5



@bot.message_handler(commands=['play'])
def victor_handler(message):
    if energy >= 10:    
                    victor()
    else:
        bot.send_message(message.chat.id, "Питомец не может играть, он устал! Дайте ему выспаться!")


# Сон
def sleep():
    global satiety, energy
    satiety += 10
    energy += 50


@bot.message_handler(commands=['sleep'])
def sleep_handler(message):
    bot.send_message(message.chat.id, 'Тише, питомец заснул...')
    sleep()
    time.sleep(10)  # задержка на 10 секунд
    bot.send_message(message.chat.id, 'Питомец проснулся!')

    validate(message)


NAME = 'Konor'
PET = 'Андроид'
# Характеристики: 100%
energy = 100
satiety = 15  # уровень сытости
happiness = 100  # уровень счастья

money = 0

bot.polling()
