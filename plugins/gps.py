

"""
Syntax : .gps <location name>
"""
# Made by @mrconfused
# help from @sunda005 and @SpEcHIDe
# don't edit credits 

from geopy.geocoders import Nominatim
from Extre.utils import admin_cmd
from telethon.tl import types



@client.on(admin_cmd(pattern="gps ?(.*)"))
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("What should i find? Give me location.🤨")

    await event.edit("Finding😁")

    geolocator = Nominatim(user_agent="catExtre.)
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(
                    lat, lon
                )
            )
        )
        await event.delete()
    else:
        await event.edit("I coudn't find it😫")
