from Extre.utils import admin_cmd
@client.on(admin_cmd(pattern='chutia'))
async def chutie(e):
  await e.edit("hehe ye chutia h ")
