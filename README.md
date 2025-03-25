
## WatchBot for "too good to go"
This repo is a fork of @AukiJuanDiaz repo, which were no longer maintained. Now it is working with a new version of the tgtg library.
### Problem
This project helps me to no longer miss my favorite offers at "[too good to go](https://toogoodtogo.org/en)" (also known as tgtg)!

"Too good to go" is a platform, where stores can offer bags of leftover food, that they otherwise need to throw away. The stores save a little bit of money, we get goods, that already have a few quirks, but are still consumable. Most importantly, this reduces food waste and thereby is good for the planet. In my neighborhood, e.g. a supermarket offers fruits & vegetables and a bakery offer their leftover bread at the end of the day.

However, the tgtg-app does often not notify me in time when my favorite goods are in stock. Since the offers are popular and limited, I regularly miss the time to click and collect the items. There are no settings for notifications in the app.

### Solution
This application scrapes info from the tgtg-app and sends me a notification via a Telegram bot as soon as my favorite items are available. The application runs in the cloud via heroku.
Here is a screenshot of the application:

![Telegram Screenshot](/result_screenshot.jpeg "Telegram bot with notifications")


##### Tgtg API
There is a library wrapped around the API of the tgtg-app. You can find the library and a short documentation [here.](https://pypi.org/project/tgtg/)
To use WatchBot you will need to get account credentials. Provided function get_credentials() will help you to do this.
##### Telegram bot
I used Telegram as the service to notify me, because they are quite supportive for adding your own bots to the platform and provide a rich API. [This article](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e) provides a quick introduction into sending Telegram messages with python.
- To create a bot, you need to search @BotFather on Telegram, send him a “/start” message.
- Send another “/newbot” message, then follow the instructions to setup a name and a username
- Your bot is now ready, save a backup of your API token - it is our first telegram variable - bot_token.
- On Telegram, search your bot (by the username you just created), press the “Start” button or send a “/start” message
- Open a new tab with your browser, enter https://api.telegram.org/bot<yourtoken>/getUpdates , replace <yourtoken> with your API token, press enter and you should see something like this:
```json
{"ok":true,"result":[{"update_id":86xxxxxxx,
"message":{"message_id":1147,"from":{"id":40xxxxxxx,"is_bot":false,"first_name":"Anton","username":"se*****","language_code":"en"},"chat":{"id":404539480,"first_name":"Anton","username":"septiconn","type":"private"},"date":1658058440,"text":"ffffff"}}]}
```
- Look for “id”, for instance, 40xxxxxxx above is my chat id. Look for yours and put it as your bot_chatID1 variable
- If you want bot messages to be sent to another chat, you should add bot to your chat and get id of this chat. After you have added bot to your chat, you can get id of this chat by using same command as for your first chat. 
```json
"my_chat_member":{"chat":{"id":-72xxxxxx,"title":"your_chat_name","type":"group","all_members_are_administrators":true},"from":{"id":40xxxxxx,"is_bot":false,"first_name":"Anton","username":"xxxxx","language_code":"en"},"date":1658075479,"old_chat_member":{"user":{"id":55xxxxxxx,"is_bot":true,"first_name":"TGTG Watchbot","username":"tgtg"},"status":"left"},"new_chat_member":{"user":{"id":55xxxxxxx,"is_bot":true,"first_name":"TGTG Watchbot","username":"tgtg"},"status":"member"}}}]}
```
- Look for “id”, for instance, -72xxxxxx above is chat id for my chat. Look for yours and put it as your bot_chatID2 variable
[Source](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e)
##### Heroku Deployment
Heroku is a platform to run small web applications in the cloud for free. [This article](https://medium.com/dev-genius/how-to-deploy-your-python-script-to-heroku-in-4-minutes-cddf11d852af) gives a short description on how to deploy a python script on Heroku. Additionally, I used config variables to hide my credentials in the project. These variables are explained [here](https://devcenter.heroku.com/articles/config-vars#config-var-policies) in the heroku documentation.
