""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="ihelp$")
async def usit(event):
    await edit_or_reply(
        event,
        f"**Hai {owner} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"β£ **Group Support :** [πππΆπΆπ» π¨ππ²πΏπ―πΌπ](t.me/AyiinXdSupport)\n"
        f"β£ **Channel Ayiin :** [πππΆπΆπ»π¦ππ½π½πΌπΏπ](t.me/AyiinSupport)\n"
        f"β£ **Owner Repo :** [ΚΙͺΙ΄s-α΄x](t.me/Contoldisini)\n"
        f"β£ **Repo :** [πππΆπΆπ»-π¨ππ²πΏπ―πΌπ](https://github.com/AyiinXd/Ayiin-Userbot)\n",
    )


@man_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Ayiin-Userbot:** [KLIK DISINI](https://telegra.ph/List-Variabel-Heroku-untuk-Man-Userbot-09-22)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  β’  **Syntax :** `{cmd}ihelp`\
        \n  β’  **Function : **Bantuan Untuk Ayiin-Userbot.\
        \n\n  β’  **Syntax :** `{cmd}listvar`\
        \n  β’  **Function : **Melihat Daftar Vars.\
        \n\n  β’  **Syntax :** `{cmd}repo`\
        \n  β’  **Function : **Melihat Repository Ayiin-Userbot.\
        \n\n  β’  **Syntax :** `{cmd}string`\
        \n  β’  **Function : **Link untuk mengambil String Ayiin-Userbot.\
    "
    }
)
