from email import message
from config import TOKEN 
import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from button import *
from aiogram.types import Message,CallbackQuery
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="nazarov_7788",
  port="3306",
  database="youtube"
)

cursor = db.cursor()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



# sql = "SELECT * FROM korzina_bot WHERE user_id ='{}'".format(276482229)
# cursor.execute(sql)
# myresult = cursor.fetchall()
# result_bot = {}
# for result in myresult:
#     my_dict = {"name": result[1], "value":result[3], "price":result[2]}
#     a = my_dict["price"]
#     result_bot[my_dict["name"]] = result_bot.get(my_dict["name"], 0) + int(my_dict["value"])
# result_bot = [{"name": my_dict, "value": result_bot[my_dict], "price": a} for my_dict in result_bot]
# # print(result_bot)
# for k in result_bot:
#     print(k)




# print(result_bot)
# for k in result_bot:
#     print(k)
# [ 
#     ('276482229', 'Jaguar', '12000', 1), 
#     ('276482229', 'Flash', '16000', 2), 
#     ('276482229', 'Flash', '16000', 8)
# ]


# sql = "INSERT INTO products_bot (category, phota,  product_name, description, price) VALUES (%s, %s, %s, %s, %s)"
# val = ("Pizza", "pizza3", f"Pishloqli Pizza", "Pishloqli Pizza", "77000")
# cursor.execute(sql, val)
# db.commit()
# print("muvaffaqyatli qo'shildi!")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer_photo(
        photo = open('images/menu2.jpg','rb'),
        caption = "<b>Menyudan birortasini tanlang</b>" , parse_mode = 'HTML',reply_markup = bosh_sahifa)
    await message.delete()
    print(message['chat']['id'])

@dp.message_handler(text="🛍Buyurtma berish")
async def buyurtma_berish(message: types.Message):
    await message.answer_photo(
        photo = open('images/pizza4.jpg', 'rb'),
        caption = "<b>Menyudan birortasini tanlang</b>" , parse_mode = 'HTML',reply_markup = bosh_sahifa_buyurtma_berish)

@dp.message_handler(text="📥 Savatcha")
async def savatcha(message: types.Message):
    sql = "SELECT * FROM korzina_bot WHERE user_id ='{}'".format(f"{message['chat']['id']}")
    cursor.execute(sql)
    myresult = cursor.fetchall()
    result_bot = {}
    for result in myresult:
        my_dict = {"name": result[1], "value":result[3], "price":result[2]}
        a = my_dict["price"]
        result_bot[my_dict["name"]] = result_bot.get(my_dict["name"], 0) + int(my_dict["value"])
    result_bot = [{"name": my_dict, "value": result_bot[my_dict], "price": a} for my_dict in result_bot]
    # print(result_bot)
    res = 'Korzina\n\n'
    for k in result_bot:
        print(k)
        res += f'nomi: <b>{k["name"]}</b>\nnarxi: <b>{k["price"]}</b>\nsoni: <b>{k["value"]}</b>\n\n'
    await message.answer(res, parse_mode="HTML", reply_markup=bosh_sahifa_buyurtma_berish_tozalash)
    
@dp.message_handler(text="❌ Tozalash")
async def buyurtma_berish(message: types.Message):
    sql = "DELETE FROM korzina_bot WHERE user_id ='{}'".format(f"{message['chat']['id']}")
    cursor.execute(sql)
    db.commit()
    await message.answer("<b>Korzina Bo'sh</b>" , parse_mode = 'HTML',reply_markup = bosh_sahifa_buyurtma_berish)




@dp.message_handler(text="Pizza")
async def buyurtma_berish_ichimliklar(message: types.Message):
    await message.answer_photo(
        photo = open('images/menu.jpg', 'rb'),
        caption = "<b>Menyudan birortasini tanlang</b>" , parse_mode = 'HTML',reply_markup = bosh_sahifa_buyurtma_berish_pizza)
    await message.delete()

@dp.message_handler(text="Donar Pizza")
async def buyurtma_berish_ichimliklar_donar_pizza(message: types.Message):
    await message.answer_photo(
        photo = open('images/pizza1.jpg','rb'),
        caption = """
<b>💚 |<b>Maxsulot: </b></b><i>"Donar Pizza"</i>
<b>💰 |Narxi: </b><i>99 000</i><b> So'm</b>

<b>⬇ |Sonini kiriting!</b>
        
        """ , parse_mode = 'HTML',reply_markup = bosh_sahifa_buyurtma_berish_ichimliklar_donar_pizza)

@dp.message_handler(text="Pishloqli Pizza")
async def buyurtma_berish_ichimliklar_pishloqli_pizza(message: types.Message):
    await message.answer_photo(
        photo = open('images/pizza2.jpg','rb'),
        caption = """
<b>💚 |<b>Maxsulot: </b></b><i>"Pishloqli Pizza"</i>
<b>💰 |Narxi: </b><i>77 000</i><b> So'm</b>

<b>⬇ |Sonini kiriting!</b>
        
        """ , parse_mode = 'HTML',reply_markup = bosh_sahifa_buyurtma_berish_ichimliklar_pishloqli_pizza)

@dp.message_handler(text="Go'shtli Pizza")
async def buyurtma_berish_ichimliklar_goshtli_pizza(message: types.Message):
    await message.answer_photo(
        photo = open('images/pizza3.jpg','rb'),
        caption = """
<b>💚 |<b>Maxsulot: </b></b><i>"Go'shtli Pizza"</i>
<b>💰 |Narxi: </b><i>84 000</i><b> So'm</b>

<b>⬇ |Sonini kiriting!</b>
        
        """ , parse_mode = 'HTML',reply_markup = bosh_sahifa_buyurtma_berish_ichimliklar_pishloqli_pizza)





@dp.callback_query_handler(text="donar_pizza_1")
async def donar_pizza_1(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Donar pizza", "99000", 1)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Donar pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="donar_pizza_2")
async def donar_pizza_2(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Donar pizza", "99000", 2)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Donar pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="donar_pizza_3")
async def donar_pizza_3(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Donar pizza", "99000", 3)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Donar pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="donar_pizza_4")
async def donar_pizza_4(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Donar pizza", "99000", 4)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Donar pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="donar_pizza_5")
async def donar_pizza_5(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Donar pizza", "99000", 5)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Donar pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="donar_pizza_6")
async def donar_pizza_6(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Donar pizza", "99000", 6)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Donar pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="donar_pizza_7")
async def donar_pizza_7(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Donar pizza", "99000", 7)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Donar pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="donar_pizza_8")
async def donar_pizza_8(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Donar pizza", "99000", 8)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Donar pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="donar_pizza_9")
async def donar_pizza_9(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Donar pizza", "99000", 9)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Donar pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

    print("muvaffaqyatli qo'shildi!")




@dp.callback_query_handler(text="pishloqli_pizza_1")
async def pishloqli_pizza_1(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Pishloqli pizza", "77000", 1)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Pishloqli pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="pishloqli_pizza_2")
async def pishloqli_pizza_2(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Pishloqli pizza", "77000", 2)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Pishloqli pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="pishloqli_pizza_3")
async def pishloqli_pizza_3(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Pishloqli pizza", "77000", 3)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Pishloqli pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="pishloqli_pizza_4")
async def pishloqli_pizza_4(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Pishloqli pizza", "77000", 4)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Pishloqli pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="pishloqli_pizza_5")
async def pishloqli_pizza_5(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Pishloqli pizza", "77000", 5)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Pishloqli pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="pishloqli_pizza_6")
async def pishloqli_pizza_5(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Pishloqli pizza", "77000", 6)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Pishloqli pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="pishloqli_pizza_7")
async def pishloqli_pizza_7(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Pishloqli pizza", "77000", 7)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Pishloqli pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="pishloqli_pizza_8")
async def pishloqli_pizza_8(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Pishloqli pizza", "77000", 8)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Pishloqli pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

@dp.callback_query_handler(text="pishloqli_pizza_9")
async def pishloqli_pizza_9(call:CallbackQuery):

    sql = "INSERT INTO korzina_bot (user_id, product_name, price, quantity_product) VALUES (%s, %s, %s, %s)"
    val = (f"{call.message['chat']['id']}", f"Pishloqli pizza", "99000", 9)
    cursor.execute(sql, val)
    db.commit()
    await call.message.answer("<b>'Pishloqli pizza' Muvaffaqyatli qo'shildi!</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)
    await call.message.answer("<b>Yana biror narsa buyurtma berishni hohlaysizmi?</b>" , parse_mode = 'HTML', reply_markup=bosh_sahifa_buyurtma_berish)

    print("muvaffaqyatli qo'shildi!")







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)