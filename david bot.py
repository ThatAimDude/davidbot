
import discord
import asyncio
from discord.ext import commands
from discord.utils import get


TOKEN = 'MTA5OTMxMDA2OTc2MzU1MTM2Mg.GPnv87.esZJ4CwuulbrmhKlkjpd3DADWU-N16qs--xj38'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

#restricted_user_id = "687685540346331195"


#def check_user(ctx):
#    return str(ctx.message.author.id) != restricted_user_id



@bot.command()
#@commands.check(check_user)
async def david(message):
    ctx = await bot.get_context(message)
    embed = discord.Embed(
        colour=discord.Colour.dark_blue(),
        description="Davids fat ahh",
        title="🤫"
    )

    embed.set_image(url="https://cdn.discordapp.com/attachments/1060890325238939668/1099080259908931614/Untitled-1.png")

    messages_to_delete = []
    counter = 0
    while counter < 3:
        print("asd")
        sent_message = await ctx.send(embed=embed)
        messages_to_delete.append(sent_message)
        counter += 1
        await asyncio.sleep(1)

    await asyncio.sleep(5)
    for message in messages_to_delete:
        await message.delete()

    await asyncio.sleep(30)

    for message in messages_to_delete:
        await message.delete()




@bot.event
async def on_message(message):

    david_name = ['<@687685540346331195>', 'david', 'davids', 'davdis', 'dvadis', 'davide', '@david', '@scorpion']
    if "jamal" in message.content:
        await message.delete()

    if message.content.startswith('!david'):
        await david(message)
    elif david_name in message.content.lower():
        embed = discord.Embed(title='David Detected')
        embed.set_image(url='https://cdn.discordapp.com/attachments/811365671794638848/1099074339959210135/nerd-emoji-nerd.gif')
        sent_message = await message.channel.send(embed=embed)

        await asyncio.sleep(6)

        await sent_message.delete()


    elif message.content == '!goofy':
        user_id = 666675859532546048
        guild = message.guild
        user = guild.get_member(user_id)
        role = discord.utils.get(guild.roles, name='Goofy')

        await user.add_roles(role)

        await asyncio.sleep(30)  # 5 minutes

        await user.remove_roles(role)



# Doesnt work idk why

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == '!goofy':
        user_id = 666675859532546048
        guild = message.guild
        user = guild.get_member(user_id)
        role = discord.utils.get(guild.roles, name='Goofy')


        await user.add_roles(role)

        await asyncio.sleep(30)  # 5 minutes

        await user.remove_roles(role)

#@bot.event
#async def on_message(message):
 #   if message.content.startswith('!david1'):
#        channel = message.channel
 #       messages = []
#        async for message in channel.history(limit=50):
##            messages.append(message)
#        await channel.send("50 messages deleted")




bot.run(TOKEN)
