from instabot import Bot
bot = Bot()
bot.login(username="",password="")#username and password of the acc which should be altered
bot.follow('name')#username of whom you want to follow
bot.upload_photo("path of photo with / forward ",caption="caption to post")#to post anything
bot.unfollow('name')#to unfollow someone
bot.send_message("i like python",["username1","username2","username3"])#message multiple users
#tell us the total number of followers for that userId
followers = bot.get_user_followers("userid")
for follower in followers:
    print (bot.get_user_info(follower))
#similar for following but insted of follower its following
