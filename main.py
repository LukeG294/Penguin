import discord
from pymongo import MongoClient
import pymongo
import datetime
from discord.utils import get
from discord.ext import commands
import random
import time
from datetime import datetime
from discord.ext.commands import Bot
import translate

 
cooldownusers = []    
bannedusers = []
 
 

 
client = discord.Client()






clientmongo = MongoClient("mongodb+srv://USER:PASSWORD@DATABASENAME.hgwxo.mongodb.net/DATABASENAME?retryWrites=true&w=majority")
db = clientmongo.DATABASENAME_database
collection = db.CLUSTERNAME_collection
 
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


        
@client.event
async def on_message(message):
 
    
    
    name = message.author.name
    checkas = collection.find_one({"author": name})
 
    if checkas != None:
 
                  checkas["points"] += 1
                  collection.replace_one( 
          {"author": name}, 
          checkas
          )
    def Add():
 
 
 
      user = message.author
 
      time = datetime.now()
      cooldownusers.append([user, time])
 
    def Check():
      user = message.author
      for item in cooldownusers:
 
        if user in item:
          time = item[1]
 
 
 
          newtime = datetime.now()
          duration = (newtime-time)
 
          if duration.seconds >= 900:
            cooldownusers.remove(item)
            return False
          else:
            return True
 
 
    namex = "Visit top.gg here: https://top.gg/bot/770336353669480449 for a list of my commands."
    valuez = ":penguin:" 
    
      
    
    if message.content == ("p!commands"):
        embedVar = discord.Embed(title="Commands",description="**Commands**", color = 0x00ff00)
        embedVar.add_field(name = namex, value = valuez, inline=False)
 
 
        await message.channel.send(embed=embedVar)
    

    elif message.content.startswith("p!bypass"):
        authd = str(message.author.id)
        print(authd)
        
         
 
 
 
          
 
 
            
        
 
 
        userap = message.content[9:]
        userap = str(userap)
        userthatsent = message.author
        userthatsent = str(userthatsent)
 
        if userap == ("Penguin"):
                await message.channel.send("Aw, that's awfully nice of you, but you can't gift me :heart: :penguin:")
        if userthatsent.startswith(userap):
 
 
                await message.channel.send("Go help others to get karma, you can't gift yourself.")
        else:
                check = collection.find_one({"author": userap})
 
                userogifter = message.author.name
                checkus = collection.find_one({"author": userogifter})
 
                if checkus != None:
 
                    checkus["points"] += 1
                    collection.replace_one( 
                    {"author": name}, 
                    checkus
                    )
             
 
 
 
 
                if check != None:
                    values = check["points"] 
                    values = str(values)              
                    check["points"] += 10
                    collection.replace_one( 
                {"author": userap}, 
                check
                )
 
 
                    newpts = check["points"]
                    usernew = check["author"]
                    newpts = str(newpts)
                    usernew = str(usernew)
                    await message.channel.send("Thanks! "+usernew+" now has "+newpts+ " points. :penguin:")
                else:
                    await message.channel.send("User is **not** in database. Adding them now.")
                    post = {"author": userap,
                            "points":50,
                            }
                    post_id = collection.insert_one(post)
                    await message.channel.send("Added to the database. You may now ask to add points to this user with p!gift "+userap)    
 
    #STILL WORKING ON
    if message.content.startswith("p!celeryban"):
        celerytoban = message.content[12:]
        print(message.author.id)
        if message.author.id==529382433452326946:
          bannedusers.append(celerytoban)
          await message.channel.send("I just celery banned "+celerytoban+"!")
        else:
          await message.channel.send("You aren't celery!")

 
    if message.content == ("p!gift"):
        await message.channel.send("Oops! Looks like you forgot to add the user you'd like to gift.")
  
   
      
    elif message.content.startswith("p!latex"):
 
 
 
      
 
 
 
 
                authd = str(message.author.id)
                if authd in bannedusers:
                  auth = message.author
                  auth = str(auth)
                  print(auth+" is banned and used command.")
                else:
                  await message.channel.send("http://tex.z-dn.net/?f="+message.content[8:]+" ")
 
    elif message.content==("p!bug"):
                authd = str(message.author.id)
                if authd in bannedusers:
                  auth = message.author
                  auth = str(auth)
                  print(auth+" is banned and used command.")
                else:
 
 
                  await message.channel.send("Please include the bug contents after `p!bug`")
    
    elif message.content.startswith("p!bug"):
                bugrep = client.get_channel(795459557144657920)
                bugger = message.author
                bugger = str(bugger)
 
                bug = message.content[6:]
 
 
 
                if message.author in bannedusers:
                  print(message.author+" is banned and used command.")
 
                else:  
                  await bugrep.send("Bug from **"+bugger+":** "+bug)
                  await message.channel.send("Reported, thank you.")
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
            
 
 
 
 
 
 
 
 
    elif message.content.startswith("p!check"):
                
                userocheck = message.author.name
                checkcheck = collection.find_one({"author": userocheck})
 
                if checkcheck != None:
 
                    checkcheck["points"] -= 1
 
 
                checker = message.content[8:]
                checkers = collection.find_one({"author":checker})
                pof = checkers["points"]
                pof = str(pof)
 
 
 
                usertocheck = message.author
                usertocheck=str(usertocheck)
 
 
 
 
 
 
 
                await message.channel.send(checker+" has "+pof+" points :penguin:")
 
 
 
 
 
    elif message.content.startswith("p!leaderboard"):
 
                    mydoc = collection.find().sort("points",-1)
 
 
 
                    i = 0    
 
 
                    for item in mydoc:
                        await message.channel.send(str("**"+item["author"]+"**")+" - "+str(item["points"]))
                        i +=1
                        if i == 3:
                            break  
 
 
 
    elif message.content.startswith("p!gift"):           
          authd = str(message.author.id)
          print(authd)
          if authd in bannedusers:
              auth = message.author
              auth = str(auth)
              print(auth+" is banned and used command.")
          else:     
 
 
 
            if Check() == True:
                  celery = str(message.author)
                  embedVar = discord.Embed(title="You're currently on cooldown",description="Please try again later. Penguin's cooldown lasts for 15 minutes so commands are not abused. Please use p!bug {bug goes here} if you think this is a mistake.", color = 0x0000ff)
                  embedVar.add_field(name = "Cooldown reminder issued for "+celery, value = ":penguin:", inline=False)
 
 
                  await message.channel.send(embed=embedVar)
 
 
 
            else: 
              Add()  
              time = datetime.now()
              cooldownuser = message.author
              cooldownusers.append([cooldownuser, time])   
 
 
              userap = message.content[7:]
              userap = str(userap)
              userthatsent = message.author
              userthatsent = str(userthatsent)
 
              if userap == ("Penguin"):
                await message.channel.send("Aw, that's awfully nice of you, but you can't gift me :heart: :penguin:")
              elif userthatsent.startswith(userap):
 
 
                await message.channel.send("Go help others to get karma, you can't gift yourself.")
              else:
                check = collection.find_one({"author": userap})
 
                userogifter = message.author.name
                checkus = collection.find_one({"author": userogifter})
 
                if checkus != None:
 
                    checkus["points"] += 1
                    collection.replace_one( 
                    {"author": name}, 
                    checkus
                    )
             
 
 
 
 
                if check != None:
                    values = check["points"] 
                    values = str(values)              
                    check["points"] += 10
                    collection.replace_one( 
                {"author": userap}, 
                check
                )
 
 
                    newpts = check["points"]
                    usernew = check["author"]
                    newpts = str(newpts)
                    usernew = str(usernew)
                    await message.channel.send("Thanks! "+usernew+" now has "+newpts+ " points. :penguin:")
                else:
                    await message.channel.send("User is **not** in database. Adding them now.")
                    post = {"author": userap,
                            "points":50,
                            }
                    post_id = collection.insert_one(post)
                    await message.channel.send("Added to the database. You may now ask to add points to this user with p!gift "+userap)    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 client.run('bot token') 
