import discord
from discord.ext import commands
import random
import os


bot = commands.Bot(command_prefix = '=')

client = discord.Client()

# Начало действий
@bot.command(pass_context = True)
async def huge(ctx, pers: discord.Member):

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
        await ctx.send(embed=embed)

@bot.command(pass_context = True)
async def kiss(ctx, pers: discord.Member):

        url_random = ('https://i.gifer.com/2Ugo.gif',
                      'https://i.pinimg.com/originals/99/c4/18/99c41869ba1551575aefd9c8ffc533de.gif',
                      'https://i.pinimg.com/originals/b0/85/98/b08598aa7bf906bbf298dc067820436e.gif',
                      'http://99px.ru/sstorage/86/2015/04/image_86060415165552581631.gif',

                      )
        url = random.choice(url_random)
        author = ctx.author
        write_random = ('**{} поцеловал {}**'.format(author.mention, pers.mention),
                    '**У всех на виду {} засосал {}**'.format(author.mention, pers.mention),
                    '**{} облизал губы {}**'.format(author.mention, pers.mention),
                    '**Кажется, {} сделал что-то постыдное с {}**'.format(author.mention, pers.mention),
                    '**Оу... {} даёт понять {} свои намерения (как жаль, что у нас на сервер сидят лишь парни...)**'.format(author.mention, pers.mention))
        write = random.choice(write_random)
        embed = discord.Embed(description=write, color=0x00ff00)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

@bot.command(pass_context = True)
async def beat(ctx, pers: discord.Member):

        url_random = ('https://cs.pikabu.ru/post_img/2013/10/04/9/1380898436_18882066.gif',
                      'https://i.gifer.com/7zBH.gif',
                      'https://i.gifer.com/777c.gif',
                      'https://data.whicdn.com/images/218727150/original.gif',
                      'https://pa1.narvii.com/7296/e35a74427cb6801a25bf59880dd9df11d9c2bf8ar1-400-225_hq.gif'
                      )
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
        await ctx.send(embed=embed)

@bot.command(pass_context = True)
async def baka(ctx, pers: discord.Member):

        url_random = ('https://thumbs.gfycat.com/SandyTheseAmericanwarmblood-small.gif',
                      'https://gifimage.net/wp-content/uploads/2017/09/baka-gif-4.gif',
                      'https://anime-chan.me/uploads/posts/2015-07/1435986861_tumblr_nqwk1u0lht1ua4ow2o1_500.gif',
                      'https://thumbs.gfycat.com/ConcreteVibrantDalmatian-size_restricted.gif',
                      'https://i.gifer.com/GvWY.gif'
                      )
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
        await ctx.send(embed=embed)
@bot.command(pass_context = True)
async def secret(ctx):
    url_random = [
        'https://animehub.cc/wp-content/uploads/2019/08/Anime-Anime-Gifki-senko-sewayaki-kitsune-no-senko-san-sewayaki-kitsune-no-senko-san.gif',
        'https://66.media.tumblr.com/c7509993bf557309fb945276500d5bc8/tumblr_pvbekvDBVY1usc9y9o9_500.gif'
    ]
    author = ctx.author
    write = ['Милая кицуне заботится о {}'.format(author.mention),
             'Внутри страха живёт сила!'
              ]
    url_object = int(len(url_random)) - 1
    x = (0, url_object)
    y = random.choice(x)
    url = url_random[y]
    write = write[y]
    embed = discord.Embed(description=write, color=0x00ff00)
    embed.set_image(url=url)
    await ctx.send(embed=embed)


#конец действий

token = os.environ.get('BOT_TOKEN')
bot.run(token)
