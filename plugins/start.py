from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    joinButton = InlineKeyboardMarkup([[
         InlineKeyboardButton("📢 Official Channel 📢", url="https://t.me/CinemaCompanyofficials"),
         InlineKeyboardButton("☺️ Updates ☺️", url="https://t.me/Tiyaan_bots")]
    ])
    thumbnail_url = config.SPIC
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(thumbnail_url, welcomed, reply_markup=joinButton)
    raise StopPropagation
