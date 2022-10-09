import discord
from discord.ext import commands
import datetime
from datetime import datetime
from discord import permissions
bot = commands.Bot(command_prefix='!', description="Test Bot for the discord.py")
MESSAGEID = 912350756080848896


@bot.event
async def on_ready():
    print(f"I am alive!")


@bot.command(pass_context=True)
async def hello(ctx, name: str):
    await ctx.send(f"Welcome {name}")


@bot.event
async def on_raw_reaction_add(payload):
    if MESSAGEID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == '🔥':
            role = discord.utils.get(guild.roles, name="ติดVtuber")
        elif emoji == '📗':
            role = discord.utils.get(guild.roles, name="ติวสอบ ขอกูก่อน")
        elif emoji == '🩺':
            role = discord.utils.get(guild.roles, name="หมอ .... หมอผี SEC B")
        elif emoji == '⚙️':
            role = discord.utils.get(guild.roles, name="วิศ.....วิดนำท่อมันตัน SEC C")
        elif emoji == '🤖':
            role = discord.utils.get(guild.roles, name="สร้างไรพังหมด SEC D")
        elif emoji == '🖥️':
            role = discord.utils.get(guild.roles, name="หุ่นยนต์นี่มันดีจิงๆ (ตุ๊กตายางอ่ะ) SEC E")
        await member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    if MESSAGEID == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        print(emoji)
        if emoji == '🔥':
            role = discord.utils.get(guild.roles, name="ติดVtuber")
        elif emoji == '📗':
            role = discord.utils.get(guild.roles, name="ติวสอบ ขอกูก่อน")
        elif emoji == '🩺':
            role = discord.utils.get(guild.roles, name="หมอ .... หมอผี SEC B")
        elif emoji == '⚙️':
            role = discord.utils.get(guild.roles, name="วิศ.....วิดนำท่อมันตัน SEC C")
        elif emoji == '🤖':
            role = discord.utils.get(guild.roles, name="สร้างไรพังหมด SEC D")
        elif emoji == '🖥️':
            role = discord.utils.get(guild.roles, name="หุ่นยนต์นี่มันดีจิงๆ (ตุ๊กตายางอ่ะ) SEC E")
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            print("Member not found")


@bot.command(pass_context=True)
async def online(ctx):
    embed = discord.Embed(
        title="Welcome To ใช่แล้ว โหน่หร่า",
        color=0x1abc9c
    )
    embed.add_field(name="Please Select a Role from the reactions below",
                    value=
                        "ติดVtuber -  🔥"
                        "\nติวสอบ ขอกูก่อน - 📗"
                        "\nหมอ .... หมอผี SEC B - 🩺"
                        "\nวิศ.....วิดนำท่อมันตัน SEC C - ⚙️"
                        "\nสร้างไรพังหมด SEC D - 🤖"
                        "\nหุ่นยนต์นี่มันดีจิงๆ (ตุ๊กตายางอ่ะ) SEC E - 🖥️"
                        )
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🔥')
    await msg.add_reaction('📗')
    await msg.add_reaction('🩺')
    await msg.add_reaction('⚙️')
    await msg.add_reaction('🤖')
    await msg.add_reaction('🖥️')
    


@bot.command(pass_context=True)
async def clear(ctx, amount: str):
    if amount == 'all':
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=(int(amount) + 1))


@bot.command(pass_context=True)
@commands.has_role("Gamer")
async def game(ctx):
    await LoadGames(ctx, bot)

bot.run('ODY2NTgyMTkzMDA1MTMzODI0.YPUpjw.AOWpuRMKBdgieMRPFh8S4yUHsPA', bot=True, reconnect=True)