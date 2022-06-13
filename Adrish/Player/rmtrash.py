import os
from pyrogram import Client, filters
from pyrogram.types import Message
from Adrish.filters import command, other_filters
from Adrish.decorators import sudo_users_only, errors

downloads = os.path.realpath("Adrish/downloads")
raw = os.path.realpath(".")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **𝐃𝐄𝐋𝐄𝐓𝐄𝐃 𝐀𝐋𝐋 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐃 𝐅𝐈𝐋𝐄𝐒**")
    else:
        await message.reply_text("❌ **𝐍𝐎 𝐅𝐈𝐋𝐄𝐒 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐄𝐃**")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw)
    if ls_dir:
        for file in os.listdir(raw):
            if file.endswith('.raw'):
                os.remove(os.path.join(raw, file))
        await message.reply_text("✅ **𝐃𝐄𝐋𝐄𝐓𝐄𝐃 𝐀𝐋𝐋 𝐑𝐀𝐖 𝐅𝐈𝐋𝐄𝐒**")
    else:
        await message.reply_text("❌ **𝐍𝐎 𝐑𝐀𝐖 𝐅𝐈𝐋𝐄𝐒 𝐅𝐎𝐔𝐍𝐃**")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.raw *.jpg")
        await message.reply_text("✅ **𝐂𝐋𝐄𝐀𝐍𝐄𝐃**")
    else:
        await message.reply_text("✅ **𝐀𝐋𝐑𝐄𝐀𝐃𝐘 𝐂𝐋𝐄𝐀𝐍𝐄𝐃**")
