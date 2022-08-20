from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup


bosh_sahifa = ReplyKeyboardMarkup(
	keyboard = [
		[
				KeyboardButton(text="🛍Buyurtma berish")
		],
		[
				KeyboardButton(text="📦 Buyurtmalarim"),KeyboardButton(text="⚙️ Sozlamalar")
		],
        		[
				KeyboardButton(text="ℹ️ Biz haqimizda"),KeyboardButton(text="✍️ Fikr qoldirish")
		],

	],
	resize_keyboard = True
)

bosh_sahifa_buyurtma_berish = ReplyKeyboardMarkup(
	keyboard = [
		[
				KeyboardButton(text="🏠 Bosh sahifa"), KeyboardButton(text="📥 Savatcha")
		],
		[
				KeyboardButton(text="Pizza"),KeyboardButton(text="Lavash")
		],
        		[
				KeyboardButton(text="Salat"),KeyboardButton(text="Desert")
		],

	],
	resize_keyboard = True
)

bosh_sahifa_buyurtma_berish_pizza = ReplyKeyboardMarkup(
	keyboard = [
		[
				KeyboardButton(text="🏠 Bosh sahifa")
		],
		[
				KeyboardButton(text="Donar Pizza")
		],
    	[
				KeyboardButton(text="Pishloqli Pizza")
		],
        [
				KeyboardButton(text="Go'shtli Pizza")
		],
	],
	resize_keyboard = True
)

bosh_sahifa_buyurtma_berish_ichimliklar_donar_pizza = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1", callback_data = "donar_pizza_1"), InlineKeyboardButton(text = "2",callback_data = "donar_pizza_2"), InlineKeyboardButton(text = "3", callback_data = "donar_pizza_3")
		],
		[
				InlineKeyboardButton(text = "4", callback_data = "donar_pizza_4"), InlineKeyboardButton(text = "5",callback_data = "donar_pizza_5"), InlineKeyboardButton(text = "6", callback_data = "donar_pizza_6")
		],
        [
				InlineKeyboardButton(text = "7", callback_data = "donar_pizza_7"), InlineKeyboardButton(text = "8",callback_data = "donar_pizza_8"), InlineKeyboardButton(text = "9", callback_data = "donar_pizza_9")
		],
	],
)

bosh_sahifa_buyurtma_berish_ichimliklar_pishloqli_pizza = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1", callback_data = "pishloqli_pizza_1"), InlineKeyboardButton(text = "2",callback_data = "pishloqli_pizza_2"), InlineKeyboardButton(text = "3", callback_data = "pishloqli_pizza_3")
		],
		[
				InlineKeyboardButton(text = "4", callback_data = "pishloqli_pizza_4"), InlineKeyboardButton(text = "5",callback_data = "pishloqli_pizza_5"), InlineKeyboardButton(text = "6", callback_data = "pishloqli_pizza_6")
		],
        [
				InlineKeyboardButton(text = "7", callback_data = "pishloqli_pizza_7"), InlineKeyboardButton(text = "8",callback_data = "pishloqli_pizza_8"), InlineKeyboardButton(text = "9", callback_data = "pishloqli_pizza_9")
		],
	],
)

bosh_sahifa_buyurtma_berish_goshtli_pizza = InlineKeyboardMarkup(
		inline_keyboard = [
		[
				InlineKeyboardButton(text = "1", callback_data = "goshtli_pizza_1"), InlineKeyboardButton(text = "2",callback_data = "goshtli_pizza_2"), InlineKeyboardButton(text = "3", callback_data = "goshtli_pizza_3")
		],
		[
				InlineKeyboardButton(text = "4", callback_data = "goshtli_pizza_4"), InlineKeyboardButton(text = "5",callback_data = "goshtli_pizza_5"), InlineKeyboardButton(text = "6", callback_data = "goshtli_pizza_6")
		],
        [
				InlineKeyboardButton(text = "7", callback_data = "goshtli_pizza_7"), InlineKeyboardButton(text = "8",callback_data = "goshtli_pizza_8"), InlineKeyboardButton(text = "9", callback_data = "goshtli_pizza_9")
		],
	],
)

bosh_sahifa_buyurtma_berish_tozalash = ReplyKeyboardMarkup(
	keyboard = [
		[
				KeyboardButton(text="🏠 Bosh sahifa"), KeyboardButton(text="🛍Buyurtma berish")
		],
		[
				KeyboardButton(text="❌ Tozalash")
		],


	],
	resize_keyboard = True
)


