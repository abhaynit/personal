from instabot import Bot
bot = Bot()
bot.login(username = "abhaynitn",password = "jhjj")
#bot.upload_photo("a.jpg")
#bot.follow('userid')
#bot.send_message(" aur video bhejo bhai ",['ankitarya7658'])
followers = bot.get_user_followers("abhaynitn")
print(len(followers))

#bot.unfollow_everyone()
