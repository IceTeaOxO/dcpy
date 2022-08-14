import discord
import random
import re
from decouple import config
from novel import noveltext
from yt import makeMusic

TOKEN = config('TOKEN')



client = discord.Client()

random_contents = [
    "にゃーん",
    "わん！",
    "コケッコッコー",
]


@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

# 若使用者輸入的文字含有"鳴いて"，則回傳random_contents
@client.event
async def on_message(message):
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return 
    # メッセージの本文が 鳴いて だった場合
    if message.content == "sesela":
        # content = random.choice(random_contents)
        #爬蟲
        content=noveltext()

        # content = ""
        # with open("test.txt",'r',encoding="utf-8") as f:
        #     content = f.read()
        sep = "▚▚▚▚▚▚▚▚▚▚▚▚▚▚▚"
        await message.channel.send(sep)
        #使用for迴圈一次傳2000字
        for i in range(round(len(content)/1500)+1):
            await message.channel.send(content[i*1500:min(((i+1)*1500),len(content))])

        await message.channel.send(sep)

    
    #發送圖片
    # if message.content == "Petra":
    #     # ローカルにあるcat.pngという名前のファイルを送信する
    #     await message.channel.send(file=discord.File("image/007635388430553.png"))


    #儲存有權限的頻道的圖片
    if message.attachments:
        for attachment in message.attachments:
            # Attachmentの拡張子がpng, jpg, jpegのどれかだった場合
            if attachment.url.endswith(("png")):
                #發送圖片的URL
                # await message.channel.send(attachment.url)
                await attachment.save("./image/"+str(attachment.url[60:77])+".png")
                print(attachment.url)
            if attachment.url.endswith(("jpg")):
                await attachment.save("./image/"+str(attachment.url[60:77])+".jpg")
                print(attachment.url)
            if attachment.url.endswith(("jpeg")):
                await attachment.save("./image/"+str(attachment.url[60:77])+".jpeg")
                print(attachment.url)
    #發送embed訊息
    # if message.content=="QQQQQQQ":
    #     embed = discord.Embed(title="タイトル", description="説明")

    #     # フィールドを追加する
    #     embed.add_field(name="名前", value="値")

    #     # タイムスタンプを設定する
    #     import datetime
    #     embed.timestamp = datetime.datetime.now()

    #     # サムネイルを追加する(URL指定なので注意！)
    #     embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/0/07/Viscontisforzatarot.jpg")

    #     # 画像を追加する(こちらもURL)
    #     embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/0/07/Viscontisforzatarot.jpg")

    #     # 上側のユーザー情報を追加
    #     embed.set_author(name="タロットマン", url="https://ja.wikipedia.org/wiki/タロット", icon_url="https://upload.wikimedia.org/wikipedia/commons/6/6f/Taroky_trul.JPG")

    #     # 下側のアイコンとテキストを追加
    #     embed.set_footer(text="アルカナあるかな？", icon_url="https://upload.wikimedia.org/wikipedia/commons/6/6f/Taroky_trul.JPG")

    #     await message.channel.send(embed=embed)

   

    if message.content == "!join":
        if message.author.voice is None:
            await message.channel.send("機器人未加入語音頻道")
            return
        # ボイスチャンネルに接続する
        await message.author.voice.channel.connect()
        await message.channel.send("連接成功")

    elif message.content == "!leave":
        if message.guild.voice_client is None:
            await message.channel.send("未連接語音頻道")
            return

        # 切断する
        await message.guild.voice_client.disconnect()

        await message.channel.send("切斷連接")
    
    
    elif message.content.startswith('!play '):
        if message.guild.voice_client is None:
            await message.channel.send("未連接語音頻道")
            return
        musicName = makeMusic(message.content)
        # print(musicName)
        message.guild.voice_client.play(discord.FFmpegPCMAudio(executable="C:/Users/sandy/ffmpeg-2022-08-10-git-8fc7f0fdec-essentials_build/bin/ffmpeg.exe",source="./music/"+musicName))
        await message.channel.send("正在撥放\n"+musicName[:-5])
        # 再生中の場合は再生しない
        # if message.guild.voice_client.is_playing():
        #     await message.channel.send("再生中です。")
        #     return

        # source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("./music/「 phony (フォニイ)  Tsumiki 」ver Petra Gurin.mp3"), volume=0.5)
        # message.guild.voice_client.play(source)

        # await message.channel.send('{} を再生します。'.format(player.title))
    elif message.content == "!stop":
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return

        # 再生中ではない場合は実行しない
        if not message.guild.voice_client.is_playing():
            await message.channel.send("再生していません。")
            return

        message.guild.voice_client.stop()

        await message.channel.send("ストップしました。")



client.run(TOKEN)


