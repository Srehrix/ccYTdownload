from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
import config

@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("Developer", url="https://t.me/Tiyaan_bots")]
                ])
  
  help_image = config.HPIC
	await message.reply_photo(help_image,  caption="\n__• Just Send your Youtube video url 🌟__ \n__• And i will give Method list to select your choice 😋__\n \n======================\n • 😊 This bot is fully free.__\n`•⚙ Powered by @Tiyaan_bots`\n\n",reply_markup=alpha2)
