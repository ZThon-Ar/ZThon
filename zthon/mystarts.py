#ignore this file

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.url("قنـاة السـورس", url="t.me/ZThon")],
                              [Button.url("مطـور البـوت", url="t.me/zzzzl1l")]])
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="t.me/zzzzl1l")]])
    
