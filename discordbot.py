import discord
import random
import re
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
    if message.content == "鳴いて":
        # 送信するメッセージをランダムで決める
        content = random.choice(random_contents)
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)
    elif message.content == "おはよう":
        await message.channel.send("おはよう！！")
    
    #發送圖片
    if message.content == "Petra":
        # ローカルにあるcat.pngという名前のファイルを送信する
        await message.channel.send(file=discord.File("image/007635388430553.png"))


    #儲存有權限的頻道的圖片
    if message.attachments:
        for attachment in message.attachments:
            # Attachmentの拡張子がpng, jpg, jpegのどれかだった場合
            if attachment.url.endswith(("png")):
                #發送圖片的URL
                # await message.channel.send(attachment.url)
                await attachment.save("./image/"+str(attachment.url[60:78])+".png")
                print(attachment.url)
            if attachment.url.endswith(("jpg")):
                await attachment.save("./image/"+str(attachment.url[60:78])+".jpg")
                print(attachment.url)
            if attachment.url.endswith(("jpeg")):
                await attachment.save("./image/"+str(attachment.url[60:78])+".jpeg")
                print(attachment.url)
    #發送embed訊息
    if message.content=="embed":
        embed = discord.Embed(title="タイトル", description="説明")

        # フィールドを追加する
        embed.add_field(name="名前", value="値")

        # タイムスタンプを設定する
        import datetime
        embed.timestamp = datetime.datetime.now()

        # サムネイルを追加する(URL指定なので注意！)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/0/07/Viscontisforzatarot.jpg")

        # 画像を追加する(こちらもURL)
        embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/0/07/Viscontisforzatarot.jpg")

        # 上側のユーザー情報を追加
        embed.set_author(name="タロットマン", url="https://ja.wikipedia.org/wiki/タロット", icon_url="https://upload.wikimedia.org/wikipedia/commons/6/6f/Taroky_trul.JPG")

        # 下側のアイコンとテキストを追加
        embed.set_footer(text="アルカナあるかな？", icon_url="https://upload.wikimedia.org/wikipedia/commons/6/6f/Taroky_trul.JPG")

        await message.channel.send(embed=embed)

    # if message.content=="react":
    #     for reaction in ["☺️", "😙", "🚗"]:
    #         await message.add_reaction(reaction)
    #         # 自分の😙というリアクションを消す
    #         await message.remove_reaction(message.guild.me, "😙")
    #         #關閉特定反應
    #         # 全員の😙というリアクションを消す
    #         await message.clear_reaction("😙")

    #     if message.content=="clear":
    #         await message.clear_reactions()
    



client.run("MTAwNzE2NTU5MzI5MzY4NDc2Nw.GLjGjr.O0yhvJQTa65s3Ch4pkNWOb7bEh6gkQGrOGQ8yo")


