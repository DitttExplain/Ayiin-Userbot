from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, man_cmd


@man_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**πΌπ¨π¨ππ‘ππ’πͺππ‘πππ πͺπ’ πΏπͺπ‘πͺ ππ€π π½πππ§ ππ€π₯ππ£**")


@man_cmd(pattern="pe(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**πΌπ¨π¨ππ‘ππ’πͺππ‘ππ πͺπ’ πππ§πππ’ππ©πͺπ‘π‘πππ πππππ§ππ ππ©πͺπ**")


@man_cmd(pattern="P(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**ππππ πππ‘π ππ£ ππͺπ {owner}**")
    sleep(2)
    await xx.edit("**πΌπ¨π¨ππ‘ππ’πͺππ‘πππ πͺπ’...**")


@man_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await edit_or_reply(event, "**ππ'ππ‘πππ πͺπ’π¨ππ‘ππ’**")


@man_cmd(pattern="a(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**ππππ πππ‘π ππ£ ππͺπ {owner}**")
    sleep(2)
    await xx.edit("**πΌπ¨π¨ππ‘ππ’πͺππ‘πππ πͺπ’**")


@man_cmd(pattern="j(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**ππΌππΌ ππππ½πππ π½πΌππΌ πππππ**")
    sleep(3)
    await xx.edit("**ππππ½ππππ πππ½πππ!!!π₯**")


@man_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**ππΌπππ ππππππ πππΌ {owner}**")
    sleep(2)
    await xx.edit("**ππ πππππΌ πππππππΏ π₯**")


@man_cmd(pattern="ass(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**πππ‘ππ’ πΏπͺπ‘πͺ ππ€π π½πππ§ ππ€π₯ππ£**")
    sleep(2)
    await xx.edit("**Ψ§ΩΨ³ΩΩΩΨ§ΩΩΩ ΨΉΩΩΩΩΩΩΩΩΩ ΩΩΨ±ΩΨ­ΩΩΩΨ©Ω Ψ§ΩΩΩΩ ΩΩΨ¨ΩΨ±ΩΩΩΨ§ΨͺΩΩΩ**")


CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  β’  **Syntax :** `{cmd}p`\
        \n  β’  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  β’  **Syntax :** `{cmd}pe`\
        \n  β’  **Function : **salam Kenal dan salam\
        \n\n  β’  **Syntax :** `{cmd}l`\
        \n  β’  **Function : **Untuk Menjawab salam\
        \n\n  β’  **Syntax :** `{cmd}ass`\
        \n  β’  **Function : **Salam Bahas arab\
        \n\n  β’  **Syntax :** `{cmd}semangat`\
        \n  β’  **Function : **Memberikan Semangat.\
        \n\n  β’  **Syntax :** `{cmd}ywc`\
        \n  β’  **Function : **nMenampilkan Sama sama\
        \n\n  β’  **Syntax :** `{cmd}sayang`\
        \n  β’  **Function : **Kata I Love You.\
        \n\n  β’  **Syntax :** `{cmd}k`\
        \n  β’  **Function : **LU SEMUA NGENTOT π₯\
        \n\n  β’  **Syntax :** `{cmd}j`\
        \n  β’  **Function : **NIMBRUNG GOBLOKK!!!π₯\
    "
    }
)
