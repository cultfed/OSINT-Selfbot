import re
import telnyx
import discord, requests
from discord.ext import commands

client = commands.Bot(',', self_bot = True)
token = ""
client.remove_command('help')
@client.command()
async def email(ctx, emailsearch):
    api = f"https://emailrep.io/{emailsearch}"
    headers = {"Accept": "application/json"}
    returnn = requests.get(api, headers=headers)
    await ctx.send(f"```{returnn.text}```")
    print(returnn.status_code)

@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
async def number(ctx, query):
    api2 = f"https://api.telnyx.com/v2/number_lookup/{query}"
    telnyx.api_key = "YOUR TELNYX API KEY"
    telnyx.NumberLookup.retrieve(f"{query}")
    headers = {"Authorization": "Bearer YOUR TELNYX API KEY"}
    numberreturn = requests.get(api2, headers=headers)
    await ctx.send(f"```{numberreturn.text}```")
    print(numberreturn.status_code)

@client.command()
async def ip(ctx, query):
    api3 = f"https://ipapi.co/{query}/json/"
    ipreturn = requests.get(api3)
    await ctx.send(f"```{ipreturn.text}```")

@client.command()
async def help(ctx):
    await ctx.send("""```
================================
1) email | ,email {email}
2) number| ,number {number}
3) ip    | ,ip {ip}
4) purge | ,purge {amount} ```
https://t.me/cultfed
""")


client.run(token, bot = False)