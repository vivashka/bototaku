import discord
from discord.ext import commands
import random
import os

bot = commands.Bot(command_prefix='#')
bot.remove_command("help")

client = discord.Client()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('prefix = # '))
    print('bot is ready!')


# help commands
@bot.command()
async def help(ctx):
    embed = discord.Embed(description='''Важно заметить, что команды-гифки работают только с именами участников сервера или их упоминанием!!!''',color=0x00ff00)
    embed.add_field(name='**kiss**', value='поцелуй!', inline=True)
    embed.add_field(name='**hug**', value='объятия!', inline=True)
    embed.add_field(name='**sex**', value='Да... Да... Это то самое!', inline=True)
    embed.add_field(name='**baka**', value='ты идиот...', inline=True)
    embed.add_field(name='**beat**', value='помянем...', inline=True)
    embed.add_field(name='~~secret~~',value='~~???~~', inline=True)
    embed.add_field(name='**clear**',value='очистка сообщений. Работает если вы имеете права - управелние сообщениями\nТолко с правами - manage message', inline=False)
    embed.add_field(name='**rnum**', value='Ну что поделать... Меня экплуатируют...', inline=True)
    embed.add_field(name='**reaction**', value='добавляет роль к эмодзи в определённом сообщении\nпример:\n!reaction 678920410716176410(id роли) :osu:(название эмодзи) 676783533867401216(id сообщения)\nТолько для админа', inline=False)
    embed.add_field(name='**del_rection**', value='удаляет эмодзи и роль из сообщения')
    embed.add_field(name='**join**', value='создаёт роль, для людей, которые заходят на сервер\nпример:\n!join user(название роли)\nТолько для админа', inline=False)
    embed.add_field(name='**del_join**', value='удаляет всё, что вы написали в команде join')
    embed.set_image(url='https://99px.ru/sstorage/86/2018/12/image_8618121812560148847.gif')
    await ctx.send(embed=embed, delete_after=90)
# end help commands

# Начало действий
@bot.command(pass_context=True)
async def hug(ctx, pers: discord.Member):
    url_random = ('https://animegif.ru/up/photos/album/oct17/171023_8359.gif',
                  'https://i.gifer.com/G8Vg.gif',
                  'https://1.bp.blogspot.com/-Z1d31ECXTqM/V-QcrI4iNsI/AAAAAAAADzo/6bgaRuLCxrgV76zEaeqyq92Tu3gO2uL3gCLcB/s400/katana.gif',
                  'https://cdn-nus-1.pinme.ru/tumb/600/photo/4f/0e9c/4f0e9c1b2f24382afa747fda13218dd2.gif',
                  'https://i.gifer.com/Ulna.gif',
                  'https://pa1.narvii.com/7294/fec88dad2fb9f77bddc26dea22c2471dbbb19673r1-500-281_hq.gif')
    url = random.choice(url_random)
    author = ctx.author
    write_random = ('**{} прижал к сердцу {}**'.format(author.mention, pers.mention),
                    '**Ох... как же это мило, {} захватил в мягкие объятия {}**'.format(author.mention, pers.mention),
                    '**{} смутил своими объятиями {}**'.format(author.mention, pers.mention),
                    '**Кажется, {} требуются экстренные обнимашки от {}**'.format(author.mention, pers.mention),
                    '**Ой, {} случайно обхватывает руками {}**'.format(author.mention, pers.mention))
    write = random.choice(write_random)
    embed = discord.Embed(description=write, color=0x00ff00)
    embed.set_image(url=url)
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=90)

@hug.error
async def on_arg(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('нужно упомянуть человека!', delete_after=30)

@bot.command(pass_context=True)
async def sex(ctx, pers: discord.Member):
    url_random = ('https://media.discordapp.net/attachments/426084205395574784/676864320511934474/Touch.gif',
                  'https://media.discordapp.net/attachments/426084205395574784/676816594189549589/sex.gif'
                  'https://i.kym-cdn.com/photos/images/newsfeed/000/764/605/d93.gif')
    url = random.choice(url_random)
    author = ctx.author
    write_random = ('**{} домогается до {}**'.format(author.mention, pers.mention),
                    '**Ох... как же это пошло, {} схватил {} за интимное место**'.format(author.mention, pers.mention),
                    '**{} поддался животным инстинктам и поймал - {}**'.format(author.mention, pers.mention),
                    '**Кажется, {} требует секс от {}**'.format(author.mention, pers.mention),
                    '**{} хочет почебурекаться с {}**'.format(author.mention, pers.mention))
    write = random.choice(write_random)
    embed = discord.Embed(description=write, color=0x00ff00)
    embed.set_image(url=url)
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=90)

@sex.error
async def on_arg(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('нужно упомянуть человека!', delete_after=30)


@bot.command(pass_context=True)
async def kiss(ctx, pers: discord.Member):
    url_random = ('https://i.gifer.com/2Ugo.gif',
                  'https://i.pinimg.com/originals/99/c4/18/99c41869ba1551575aefd9c8ffc533de.gif',
                  'https://i.pinimg.com/originals/b0/85/98/b08598aa7bf906bbf298dc067820436e.gif',
                  'http://99px.ru/sstorage/86/2015/04/image_86060415165552581631.gif')
    url = random.choice(url_random)
    author = ctx.author
    write_random = ('**{} поцеловал {}**'.format(author.mention, pers.mention),
                    '**У всех на виду {} засосал {}**'.format(author.mention, pers.mention),
                    '**{} облизал губы {}**'.format(author.mention, pers.mention),
                    '**Кажется, {} сделал что-то постыдное с {}**'.format(author.mention, pers.mention),
                    '**Оу... {} даёт понять {} свои намерения (как жаль, что у нас на сервер сидят лишь парни...)**'.format(
                        author.mention, pers.mention))
    write = random.choice(write_random)
    embed = discord.Embed(description=write, color=0x00ff00)
    embed.set_image(url=url)
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=90)


@kiss.error
async def on_arg(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('нужно упомянуть человека!', delete_after=30)


@bot.command(pass_context=True)
async def beat(ctx, pers: discord.Member):
    url_random = ('https://cs.pikabu.ru/post_img/2013/10/04/9/1380898436_18882066.gif',
                  'https://i.gifer.com/7zBH.gif',
                  'https://i.gifer.com/777c.gif',
                  'https://data.whicdn.com/images/218727150/original.gif',
                  'https://i.pinimg.com/originals/c0/be/39/c0be39358dd4b11101f4f23241ddbe3c.gif')
    url = random.choice(url_random)
    author = ctx.author
    write_random = ('**{} ударил {}, кричя при этом: "НЫЫЫАААААААА"**'.format(author.mention, pers.mention),
                    '**Фотошопер {} отредактировал ебало {}**'.format(author.mention, pers.mention),
                    '**{} не используя слов, убедил {}**'.format(author.mention, pers.mention),
                    '**Кажется, {} начистил face {}, за многословность**'.format(author.mention, pers.mention),
                    '**{} вступил в битву с {} и одержал победу**'.format(author.mention, pers.mention))
    write = random.choice(write_random)
    embed = discord.Embed(description=write, color=0x00ff00)
    embed.set_image(url=url)
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=90)


@beat.error
async def on_arg(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('нужно упомянуть человека!', delete_after=30)


@bot.command(pass_context=True)
async def baka(ctx, pers: discord.Member):
    url_random = ('https://thumbs.gfycat.com/SandyTheseAmericanwarmblood-small.gif',
                  'https://gifimage.net/wp-content/uploads/2017/09/baka-gif-4.gif',
                  'https://anime-chan.me/uploads/posts/2015-07/1435986861_tumblr_nqwk1u0lht1ua4ow2o1_500.gif',
                  'https://thumbs.gfycat.com/ConcreteVibrantDalmatian-size_restricted.gif',
                  'https://i.gifer.com/GvWY.gif',
                  'https://media.discordapp.net/attachments/426084205395574784/678992099164553246/0_0.gif')
    url = random.choice(url_random)
    author = ctx.author
    write_random = ('**{} разослился на {}**'.format(author.mention, pers.mention),
                    '**Анимешник {}, использовал секретные слова на {}**'.format(author.mention, pers.mention),
                    '**{} оскорбил {}**'.format(author.mention, pers.mention),
                    '**{} не нашёл аргументов и надругался над {}**'.format(author.mention, pers.mention),
                    '**{} дал понять {}, кто он такой**'.format(author.mention, pers.mention))
    write = random.choice(write_random)
    embed = discord.Embed(description=write, color=0x00ff00)
    embed.set_image(url=url)
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=90)



@baka.error
async def on_arg(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('нужно упомянуть человека!', delete_after=30)


@bot.command(pass_context=True)
async def secret(ctx):
    url_random = [
        'https://animehub.cc/wp-content/uploads/2019/08/Anime-Anime-Gifki-senko-sewayaki-kitsune-no-senko-san-sewayaki-kitsune-no-senko-san.gif',
        'https://66.media.tumblr.com/c7509993bf557309fb945276500d5bc8/tumblr_pvbekvDBVY1usc9y9o9_500.gif',
        'https://media.discordapp.net/attachments/426084205395574784/679019793793417255/Vovachke.gif',
        'https://media.discordapp.net/attachments/426084205395574784/679046074975125514/Smer5t.gif']
    author = ctx.author
    write = ['Милая кицуне заботится о {}'.format(author.mention),
             'Внутри страха живёт сила!',
             '...Ня...',
             'А в начале пути мало кто в нас верил... не так ли?']
    url_object = len(url_random)
    x = (range(url_object))
    y = random.choice(x)
    url = url_random[y]
    write = write[y]
    embed = discord.Embed(description=write, color=0x00ff00)
    embed.set_image(url=url)
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=90)

# конец действий

# команды модеров
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, num=5):
    await ctx.channel.purge(limit=num)
    await ctx.send('сообщения удалены', delete_after=10)

@clear.error
async def bug_clear(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('у вас недостаточно прав', delete_after=10)

#конец команд модеров

# reaction

bot.messages = []

@bot.command()
async def counter(ctx):
    await ctx.send(bot.messages)

@bot.command()
@commands.has_permissions(administrator=True)
async def reaction(ctx, role_ids, emoji_ids, msg_ids):
    global emoji_roles
    if int(msg_ids) in bot.messages:
        bot.messages.remove(int(msg_ids))
        bot.messages.append(int(msg_ids))
    else:
        bot.messages.append(int(msg_ids))
    emoji_roles = {}
    emoji_roles.setdefault(emoji_ids, int(role_ids))
    await ctx.send('Роль добавлена!', delete_after=10)

@bot.command()
@commands.has_permissions(administrator=True)
async def del_reaction(ctx, role_ids, emoji_ids, msg_ids):
    global emoji_roles
    emoji_roles = {}
    emoji_roles.pop(emoji_ids, int(role_ids))
    await ctx.send('Роль и эмодзи удалена удвлена!', delete_after=10)

@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    user_id = payload.user_id
    if int(message_id) in bot.messages:
        guild_id = payload.guild_id
        guild = bot.get_guild(guild_id)
        if str(payload.emoji.name) in emoji_roles:
            roles  = emoji_roles.get(str(payload.emoji.name))
            member = guild.get_member(user_id)
            role = guild.get_role(roles)
            await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    user_id = payload.user_id
    if int(message_id) in bot.messages:
        guild_id = payload.guild_id
        guild = bot.get_guild(guild_id)
        if str(payload.emoji.name) in emoji_roles:
            roles  = emoji_roles.get(str(payload.emoji.name))
            member = guild.get_member(user_id)
            role = guild.get_role(roles)
            await member.remove_roles(role)

# end reaction


#зачисление в ряды
bot.guild_role = []

@bot.command()
@commands.has_permissions(administrator=True)
async def join(ctx, server_role):
    if server_role in bot.guild_role:
        bot.guild_role.remove(server_role)   
        bot.guild_role.append(server_role)
    else:
        bot.guild_role.append(server_role)
    await ctx.send('роль добавлена', delete_after=15)

@bot.command()
async def del_join(ctx, server_role):
    if server_role in bot.guild_role:
        bot.guild_role.remove(server_role)
        ctx.send('роль удалена', delete_after=30)
    else:
        ctx.send('Этой роли итак нет', delete_after=30)

@bot.event
async def on_member_join(member):
    for role in bot.guild_role:
        roles = discord.utils.get(member.guild.roles, name=role)
        await member.add_roles(roles)
#end - зачисление в ряды

@bot.command(pass_context=True)
async def rnum(ctx):
    number = random.choice(range(1, 7))
    await ctx.message.delete()
    await ctx.send(number, delete_after=60)


token = os.environ.get('BOT_TOKEN')
bot.run(token)
