import discord
import asyncio
from discord.ext import commands
from discord.utils import get
from itertools import cycle


# davids user id 687685540346331195


TOKEN = 'MTA5ODkzMjkzOTY2NTk4NTYxOA.GyzIc8.z-5wyPOR4_ZWhXOxpEkja4f0Q50trj14koYVIw'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)


@bot.event
async def on_ready():

    guild = bot.get_guild(1058791543252734044)
    member = guild.get_member(1100523120827318272)
    role = guild.get_role(1100760234433196073)

    red = discord.Colour.red()
    orange = discord.Colour.orange()
    yellow = discord.Colour.yellow()
    green = discord.Colour.green()
    blue = discord.Colour.blue()
    purple = discord.Colour.purple()

    names = ['-----------I', '--------I am', '----I am Gay', '-I am Gay---', '-am Gay-----', '-Gay--------','------------']

    while True:
        await role.edit(colour=red)
        await asyncio.sleep(1.5)
        await role.edit(colour=orange)
        await asyncio.sleep(1.5)
        await role.edit(colour=yellow)
        await asyncio.sleep(1.5)
        await role.edit(colour=green)
        await asyncio.sleep(1.5)
        await role.edit(colour=blue)
        await asyncio.sleep(1.5)
        await role.edit(colour=purple)
        await asyncio.sleep(1.5)


@bot.command()
async def david(message):
    ctx = await bot.get_context(message)
    embed = discord.Embed(
        colour=discord.Colour.dark_blue(),
        description="Davids silly billy",
        title="🤫"
    )

    embed.set_image(url="https://cdn.discordapp.com/attachments/1060890325238939668/1099780120467750922/OTAweDkwMA.png")

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

    david_name = ['<@687685540346331195>', 'david', 'davids', 'davdis', 'dvadis', 'davide', '@david', '@scorpion','scorpion']

    if "!david" in message.content:
        await message.delete()

    if message.content.startswith('!david'):
        await david(message)

    else:
        for name in david_name:
            if name.lower() in message.content.lower():
                embed = discord.Embed(title='David Detected')
                embed.set_image(url='https://cdn.discordapp.com/attachments/1100030470235902013/1100469600531005491/nerd-emoji-nerd_1.gif')
                sent_message = await message.channel.send(embed=embed)
                await asyncio.sleep(6)
                await sent_message.delete()
                break

    if message.content == '!goofy':
        user_id = 687685540346331195
        guild = message.guild
        user = guild.get_member(user_id)
        role = discord.utils.get(guild.roles, name='Goofy')
        await user.add_roles(role)
        await asyncio.sleep(30)  # 30 sec
        await user.remove_roles(role)

    if message.content.startswith('!delete_last_20'):
        channel = message.channel
        messages = []
        async for msg in channel.history(limit=20):
            if msg.author == bot.user:
                messages.append(msg)
        await channel.delete_messages(messages)

    if message.content.startswith('!send'):
        user_id = 262037900571574272
        user = await bot.fetch_user(user_id)
        await user.send('niger')


bot.run(TOKEN)