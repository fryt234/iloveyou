from pyrogram import Client, filters
import time
import asyncio
import async_timeout

api_id = "22420294"
api_hash = "4e82424ae1a3744580c3daee7f2cb27f"
text = "привет"
app = Client("account", api_id, api_hash)
@app.on_message(filters.regex("сердечко"))
async def heart(client, message):

    await asyncio.sleep(1)
    await message.edit_text("🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)

    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)

    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️‍🩹❤️‍🩹🤍❤️‍🩹❤️‍🩹🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️‍🩹❤️‍🩹🤍❤️‍🩹❤️‍🩹🤍🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️‍🩹❤️‍🩹🤍❤️‍🩹❤️‍🩹🤍🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)

    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️‍🩹❤️‍🩹🤍❤️‍🩹❤️‍🩹🤍🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍🤍\n🤍🤍🤍❤️‍🩹❤️‍🩹❤️‍🩹🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️‍🩹❤️‍🩹🤍❤️‍🩹❤️‍🩹🤍🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍🤍\n🤍🤍🤍❤️‍🩹❤️‍🩹❤️‍🩹🤍🤍🤍\n🤍🤍🤍🤍❤️‍🩹🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)





    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)

    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.09)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🐼🐼🐼🐼🐼🌴🌴\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🐼🐼🐼🐼🐼🌴🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🐼🐼🐼🐼🐼🌴🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🐼🐼🐼🐼🐼🌴🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)

    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.09)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)


    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)

    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(1.5)


    await message.edit_text("❤️❤️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.3)
    await message.edit_text("❤️❤️❤️❤️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.3)
    await message.edit_text("❤️❤️i❤️❤️❤️❤️☁️☁️☁️☁️")
    await asyncio.sleep(0.3)
    await message.edit_text("❤️❤️❤️❤️love❤️❤️❤️❤️☁️☁️")
    await asyncio.sleep(0.3)
    await message.edit_text("❤️❤️i❤️❤️love❤️❤️you❤️❤️❤️❤️", "@Aryt7777777")















app.run()