from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.teemo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`šššš¢š¢š¤š¤ ššŖš”šŖ ššŖ š`")
    sleep(2)
    await typew.edit("`šššššš£ ššŖšš ššššš  š`")
    sleep(1)
    await typew.edit("`ššš„š ššš”š¤ ššŖ šššššš£, šššŖš£š-šššŖš£šš£š®š ššŖšš ššš£š ššš¤šØš©šš£š š¤£`")


@register(outgoing=True, pattern='^.give(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`šš®šš§šš© šš šŖš© ššš„ššš¬šš®`")
    sleep(2)
    await typew.edit("`ššššØš© ššš£šš¢šš” 10 šš§šŖš„`")
    sleep(1)
    await typew.edit("`šššš  ššØ, šæšš£ ššØ š½šŖš š©š ššššØš©`")


@register(outgoing=True, pattern='^.uno(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`ššš š š  šš`")
    sleep(2)
    await typew.edit("`š½šš¬šš£ šš£š¤ š®šŖš  š`")
    sleep(1)
    await typew.edit("`ššš£š ššš”šš ššš£ššš š¼ššš¢š š`")


CMD_HELP.update({
    "gabut": "š¾š¤š¢š¢šš£š: `.tmo`\
    \nā³ : Cobain Sendiri\
    \n\nš¾š¤š¢š¢šš£š: `.give`\
    \nā³ : Cobain Sendiri`\
    \n\nš¾š¤š¢š¢šš£š: `.uno`\
    \nā³ : Cobain Sendiri."
})
