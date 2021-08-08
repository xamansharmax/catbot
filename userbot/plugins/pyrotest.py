from pyrogram import filters

from userbot.core.session import catbot




@catbot.on_message(filters.command("test"))
async def let_me_check(_, m: Message):
	try:
		await catbot.send_message(
			m.chat.id,
				f"Hey {m.from_user.mention}, How are you ?"
			)
	except Exception as e:
		print(e)