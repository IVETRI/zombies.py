import datetime

from telethon import events

from telethon.errors.rpcerrorlist import YouBlockedUserError

from telethon.tl.functions.account import UpdateNotifySettingsRequest

from AsunaRobot.events import register 

from AsunaRobot.services.telethonuserbot import ubot 

from time import sleep

@register(outgoing=True, pattern="^.sg(?: |$)(.*)")

async def _(event):

    if event.fwd_from:

        return

    if not event.reply_to_msg_id:

       await event.edit("`Herhangi bir kullanıcı mesajına cevap verin.`")

       return

    reply_message = await event.get_reply_message()

    if not reply_message.text:

       await event.edit("`Mesaja cevap verin.`")

       return

    chat = "@SangMataInfo_bot"

    sender = reply_message.sender

    if reply_message.sender.bot:

       await event.edit("`Botlara cevap veremezsiniz.`")

       return

    await event.edit("`İşleniyor...`")

    async with bot.conversation(chat, exclusive=False) as conv:

          response = None

          try:

              msg = await reply_message.forward_to(chat)

              response = await conv.get_response(message=msg, timeout=5)

          except YouBlockedUserError:

              await event.edit(f"`Lütfen {chat} engelini kaldırın ve tekrar deneyin`")

              return

          except Exception as e:

              print(e.__class__)

          if not response:

              await event.edit("`Botdan cevap alamadım!`")

          elif response.text.startswith("Forward"):

             await event.edit("`Gizlilik ayarları yüzenden alıntı yapamadım`")

          else:

             await event.edit(response.text)

          sleep(1)

          await bot.send_read_acknowledge(chat, max_id=(response.id+3))

          await conv.cancel_all()

help = """

  • /sg*:* Get A Name History Of User

"""

mod_name = "Sang Mata"
