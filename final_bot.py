import feedparser
import asyncio
import telegram

TELEGRAM_BOT_TOKEN = '5014571744:AAFBHU3UqfoUAFuv4ZXWv7j00r5mhLIdgDQ'
TELEGRAM_CHAT_ID = '-1001483409081'
PHOTO_PATH = 'https://drive.google.com/file/d/1J1tJGlyzKK1kohHry1wuC6f-gloy27u_/view?usp=sharing'
FEED_URL = 'https://www.livechart.me/feeds/episodes'

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

NewsFeed = feedparser.parse(FEED_URL)
entry = NewsFeed.entries[0]
title = entry.title
info1 = title.split("#")
ti1 = info1[0][:-1]
ep1 = info1[1]
ep1 = '{:0>2}'.format(ep1)
x = 0

my_list = """BORUTO: NARUTO NEXT GENERATIONS
Dragon Quest: Dai no Daibouken (2020)
Meitantei Conan
One Piece
SHAMAN KING (2021)
Aharen-san wa Hakarenai
Deaimon
Heroine Tarumono! Kiraware Heroine to Naisho no Oshigoto
Kaguya-sama wa Kokurasetai -Ultra Romantic-
Kawaii dake ja Nai Shikimori-san
Kingdom 4th Season
Komi-san wa, Comyushou desu. 2nd Season
Meitantei Conan: Zero no Nichijou
Paripi Koumei
SPY x FAMILY
Summer Time Render
Tate no Yuusha no Nariagari Season 2
Tomodachi Game"""
list = my_list.split("\n")

my_list2 = """#Boruto
#DragonQuestDai
#DetectiveConan
#OnePiece
#ShamanKing
#AharenSanWaHakarenai
#Deaimon
#HeroineTarumono
#KaguyaSama S3
#KawaiiDake
#Kingdom S4
#KomiSan S2
#ZeroNoNichijou
#ParipiKoumei
#SpyxFamily
#SummertimeRender
#TateNoYuusha S2
#TomodachiGame"""
list2 = my_list2.split("\n")

async def main():
    await asyncio.sleep(60)

while 1:
    NewsFeed = feedparser.parse(FEED_URL)
    entry = NewsFeed.entries[0]
    title = entry.title
    info2 = title.split("#")
    ti2 = info2[0][:-1]
    ep2 = info2[1]
    ep2 = '{:0>2}'.format(ep2)
    if ti1 != ti2 or x == 0:
        #print('if 1 is true')
        if ti2 in list:
            #print('if 2 is true')
            ind = list.index(ti2)
            #print(ind)
            ti22 = list2[ind]
            cap = f'═────⊹⋘•♢•⋙⊹────═\n『`%s`』┇EP%s\n═────⊹⋘•♢•⋙⊹────═'
            bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=PHOTO_PATH, caption=cap%(ti22, ep2), parse_mode="MARKDOWN")
            x = 1
    ti1 = ti2
    asyncio.run(main())
