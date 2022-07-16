# Import Pakages
import telegram
import feedparser
import asyncio

# Set Up Varibals
BOT_TOKEN = '5014571744:AAFBHU3UqfoUAFuv4ZXWv7j00r5mhLIdgDQ'
CHAT_ID = '-1001483409081'
PHOTO_PATH = 'https://drive.google.com/file/d/1oW4xFwu_hvLwzh-7PA4XwSw5HiUu4lKC/view?usp=sharing'
bot = telegram.Bot(token=BOT_TOKEN)
url = 'https://www.livechart.me/feeds/episodes'
no = 0

# Time Out Function
async def main():
    await asyncio.sleep(60)

# Set Up Lists
names_list = """BORUTO: NARUTO NEXT GENERATIONS
Dragon Quest: Dai no Daibouken (2020)
Meitantei Conan
One Piece
Kingdom 4th Season
Aoashi
Summer Time Render
Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 2nd Season
Engage Kiss
Hataraku Maou-sama!!
Isekai Ojisan
Lycoris Recoil
MADE IN ABYSS: Retsujitsu no Ougonkyo
Overlord IV
SHADOWS HOUSE 2nd Season
Soredemo Ayumu wa Yosetekuru
Yofukashi no Uta"""
names_list = names_list.split("\n")

tags_list = """#Boruto
#DragonQuestDai
#DetectiveConan
#OnePiece
#Kingdom S4
#Aoashi
#SummertimeRender
#ClassroomOfTheElite S2
#EngageKiss
#HatarakuMaouSama!!
#IsekaiOjisan
#LycorisRecoil
#MadeInAbyss
#OverlordIV
#ShadowsHouse S2
#SoredemoAyumuWaYosetekuru
#YofukashiNoUta"""
tags_list = tags_list.split("\n")

# RSS First Request
feed = feedparser.parse(url)
title = feed.entries[0].title.split("#")[0][:-1]
ep = feed.entries[0].title.split("#")[1]
ep = '{:0>2}'.format(ep)
if title in names_list:
    no = 1

# Main Loop
while 1:
        title2 = feed.entries[0].title.split("#")[0][:-1]
        ep = feed.entries[0].title.split("#")[1]
        ep = '{:0>2}'.format(ep)

        if title2 != title or no == 1 and title2 in names_list:
            cap = f'═────⊹⋘•♢•⋙⊹────═\n『`%s`』┇EP%s\n═────⊹⋘•♢•⋙⊹────═'
            bot.send_photo(chat_id=CHAT_ID, photo=PHOTO_PATH, caption=cap%(tags_list[names_list.index(title2)], ep), parse_mode="MARKDOWN")

        no = 0
        title = title2
        asyncio.run(main())
