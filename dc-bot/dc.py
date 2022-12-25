import discord
import random
from discord.ext import commands
#from yahoo_fin.stock_info import *
import json
import os
import datetime
from datetime import datetime

os.chdir("C:\\Users\\anton\\Desktop\\dc-bot")

intents = discord.Intents.all()
intents.members = True

# bot = commands.Bot(command_prefix='!')
activity = activity = discord.Activity(type=discord.ActivityType.listening, name="Plumbum")
bot = commands.Bot(command_prefix="!", activity=activity, intents=intents)
pppp = "cm"
#p = get_live_price("BTC-USD")
#mc = get_day_gainers()
pringles = 2.29
mwz = 0.19
#dl = get_day_losers()
channel = bot.get_channel(955141990574592094)
kugel = 0
patrone = 0

steuer = 0.19
finanzamt = "631179768980570132"
kurs = random.randint(80, 400)
print(kurs)

bot.remove_command('help')

darknetshop = [{"name": "Pistole", "price": 11,
                "description": "Du brauchst eine Pistole um einen Bank- oder Personenraub zu begehen. Vergiss nicht Munition zu kaufen. Illegal."},
               {"name": "Gewehr", "price": 56,
                "description": "Effektiver aber auffälliger und schwerer als eine Pistole. Vergiss nicht Munition zu kaufen. Illegal."},
               # {"name":"PC","price":11,"description":"Benutz dies um dinge zu hacken" "Legal."},
               # {"name":"Laptop","price":4,"description":"Weniger Rechenleistung als ein PC, dafür leichter und mobil einzusetzen. Legal."},
               {"name": "Ransomware", "price": 7,
                "description": "Schadsoftware um andere PCs/Laptops zu verschlüsseln. Illegal."},
               {"name": "Sturmmaske", "price": 1,
                "description": "Nötig um Laden- oder Banküberfälle zu begehen. Legal."},
               {"name": "Kugel", "price": 1, "description": "5 Kugeln Munition für die Pistole. Illegal."},
               {"name": "Patrone", "price": 1, "description": "10 Kugeln für das Gewehr. Illegal."}]


async def kurs_e():
    with open("XMR.json", "r") as f:
        kurs = json.load(f)
    return kurs


async def get_bank_data():
    with open("Zentralbank.json", "r") as f:
        users = json.load(f)

    return users


def numberFormate(num):
    return ("{:,}".format(num))


@bot.command()
async def btc(ctx):
    await ctx.send(p)


@bot.command()
async def kurs(ctx):
    await kurs_e()
    await ctx.send(f"Der aktuelle XMR Kurs liegt bei {kurs} €.")


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
        users[str(user.id)]["crypto wallet"] = 0
        users[str(user.id)]["pc"] = False

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)
    return True


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def hacking(ctx):
    user = ctx.author
    with open("Zentralbank.json", "r") as f:
        pcl = json.load(f)

    if "pc" in pcl[str(user.id)] == True:
        ca = random.randint(10, 1000)
        chance = random.randint(1, 50)
        if chance == 31:
            ctx.send(
                "Du wurdest von der Polizei geschnappt! Du hast vergessen NordVPN zu aktivieren. Dir wurde eine Strafe in Höhe von 10000€ verhängt.")
            await update_bank(ctx.author, -10000, "bank")
        await update_bank(ctx.author, ca, "crypto wallet")
        await ctx.send(f"Du hast {ca} beim hacking verdient. Pass auf dass du beim hacking nicht geschnappt wirst.")
    else:
        await ctx.send("Du brauchst einen Pc!")


async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)

    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
    # users[str(user.id)]["pc"]]
    return bal


async def update_casino(user, change=0, mode="gamble"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)

    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["gamble"]]
    # users[str(user.id)]["pc"]]
    return bal


async def update_bank_st(user, change=0, mode="steuer"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)

    bal = [users[str(user.id)]["wallet"], users[str(finanzamt)]["steuer"]]
    return bal


@bot.command()
async def roulette(ctx, bet, amount):
    await open_account(ctx.author)
    zahl = random.randint(0, 36)
    bet = str(bet)
    zahl = str(zahl)
    if zahl == bet:
        await ctx.send(f"{zahl}! Du hast gewonnen!")
        await update_bank(ctx.author, amount * 35, "wallet")
    else:
        await ctx.send(f"{zahl}! Du hast verloren!")
        await update_bank(ctx.author, -1 * amount, "wallet")
        await update_bank(finanzamt, 1 * amount, "gamble")


async def update_bank_cs(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)

    bal = [users[str(user.id)]["wallet"]]
    return bal


async def update_bank_shoot(user, change=0, mode="wallet"):
    users = await get_bank_data()

    #  users[str(user.id)][mode] += change

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)

    bal = [users[str(user.id)]["kugel"]]
    return bal


@bot.command()
async def pc(ctx):
    await open_account(ctx.author)

    users = get_bank_data()

    await update_bank(ctx.author, True, "pc")
    ctx.send("Du hast einen Pc gekauft.")


async def update_bank_s(user, change=0, mode="bank"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)

    bal = [users[str(user.id)]["bank"], users[str(user.id)]["bank"]]
    return bal


@bot.event
async def on_ready():
    kurs = random.randint(80, 400)
    with open("XMR.json", "w") as f:
        json.dump(kurs, f, indent=1)
    print("Bereit")


@bot.command()
async def konto(ctx):
    await open_account(ctx.author)

    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]
    crypto_amt = users[str(user.id)]["crypto wallet"]

    wallet_amt = round(wallet_amt, 2)
    bank_amt = round(bank_amt, 2)
    crypto_amt = round(crypto_amt, 2)

    em = discord.Embed(title=f"{ctx.author.name}'s Kontostand", color=discord.Color.red())
    em.add_field(name="wallet", value=numberFormate(wallet_amt))
    em.add_field(name="bank", value=numberFormate(bank_amt))
    em.add_field(name="crypto wallet", value=numberFormate(crypto_amt))
    await ctx.send(embed=em)


@bot.command()
@commands.is_owner()
async def kontos(ctx):
    await open_account(ctx.author)

    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]
    crypto_amt = users[str(user.id)]["crypto wallet"]
    steuer_amt = users[str(user.id)]["steuer"]
    gamble_amt = users[str(user.id)]["gamble"]

    wallet_amt = round(wallet_amt, 2)
    bank_amt = round(bank_amt, 2)
    crypto_amt = round(crypto_amt, 2)
    steuer_amt = round(steuer_amt, 2)
    gamble_amt = round(gamble_amt, 2)

    em = discord.Embed(title=f"{ctx.author.name}'s balance", color=discord.Color.red())
    em.add_field(name="wallet", value=numberFormate(wallet_amt))
    em.add_field(name="bank", value=numberFormate(bank_amt))
    em.add_field(name="crypto wallet", value=numberFormate(crypto_amt))
    em.add_field(name="Steuereinnahmen", value=numberFormate(steuer_amt))
    em.add_field(name="Casino Einnahmen", value=numberFormate(gamble_amt))
    await ctx.send(embed=em)


@bot.command()
async def betteln(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earning = random.randint(1, 30)

    await ctx.send(f"Jemand hat dir {earning}€ gegeben!")

    users[str(user.id)]["wallet"] += earning

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)


@bot.command()
async def abhebung(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Bitte gebe die Menge an")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)

    if amount > bal[1]:
        await ctx.send("Du hast zu wenig Geld.")
        return
    if amount < 0:
        await ctx.send("Menge muss positiv sein.")
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1 * amount, "bank")

    await ctx.send(f"Du hast {numberFormate(amount)}€ abgehoben.")


@bot.command()
@commands.is_owner()
async def abhebungs(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Bitte gebe die Menge an")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)

    if amount > bal[1]:
        await ctx.send("Du hast zu wenig Geld.")
        return
    if amount < 0:
        await ctx.send("Menge muss positiv sein.")
        return

    await update_bank(ctx.author, amount, "crypto wallet")
    await update_bank(ctx.author, -1 * amount, "steuer")

    await ctx.send(f"Du hast {amount}XMR abgehoben.")


@bot.command()
async def einzahlung(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Bitte gebe die Menge an")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)

    if amount > bal[0]:
        await ctx.send("Du hast zu wenig Geld.")
        return
    if amount < 0:
        await ctx.send("Menge muss positiv sein.")
        return

    await update_bank(ctx.author, -1 * amount)
    await update_bank(ctx.author, amount, "bank")

    await ctx.send(f"Du hast {amount}€ eingezahlt.")


@bot.command()
async def sende(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send("Bitte gebe die Menge an")
        return

    bal = await update_bank_s(ctx.author)
    amount = int(amount) * int(steuer) + int(amount)
    amounts = int(amount) * int(steuer)

    if amount > bal[0]:
        await ctx.send("Du hast zu wenig Geld.")
        return
    if amount < 0:
        await ctx.send("Menge muss positiv sein.")
        return

    await update_bank_s(ctx.author, -1 * amount, "bank")
    await update_bank_s(member, amount, "bank")

    await ctx.send(f"Du hast {amount}€ an {member} gesendet.")

@commands.is_owner()
@bot.command()
async def gib(ctx,amount):
    await open_account(ctx.author)
    await update_bank(ctx.author,amount,"bank")


@bot.command()
async def ausrauben(ctx, member: discord.Member):
    await open_account(ctx.author)
    await open_account(member)

    bal = await update_bank(member)

    if bal[0] < 100:
        await ctx.send("Er braucht das Geld mehr als du.")
        return

    earnings = random.randrange(0, bal[0])

    await update_bank(ctx.author, earnings)
    await update_bank(member, -1 * earnings)

    await ctx.send(f"Du hast hast durch einen Raub auf {member} {earnings}€ erbeutet.")


@bot.command()
async def slots(ctx, amount=None):
    await open_account(ctx.author)

    # owner = "631179768980570132"
    # guild_owner = bot.get_user(int(ctx.guild.owner.id))

    if amount == None:
        await ctx.send("Bitte gebe die Menge an")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("Du hast zu wenig Geld.")
        return
    if amount < 0:
        await ctx.send("Menge muss positiv sein.")
        return

    final = []
    for a in range(3):
        a = random.choice(["💰", "🔔", "🍒", "⭐", "💸", "🏛","💊","📈","📉"])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
        await update_bank(ctx.author, 2 * amount)
        amounts = amount * 2
        await ctx.send("Du hast gewonnen")
        await ctx.send(f"Du hast {numberFormate(2 * amount)}€ plus gemacht. {ctx.author}")
        await update_bank(finanzamt, 0.19 * amounts, "bank")
    elif final[0] == final[1] and final[0] == final[2] and final[1] == final[2]:
        await update_bank(ctx.author, 10 * amount)
        amounts = amount * 11
        await ctx.send("Du hast gewonnen")
        await ctx.send(f"Du hast {numberFormate(9 * amount)}€ plus gemacht! {ctx.author}")
        await update_bank(finanzamt, 0.19 * amounts, "bank")
    else:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send("Du hast verloren")
        await ctx.send(f"Du hast {numberFormate(amount)}€ minus gemacht {ctx.author}")
        await update_bank(finanzamt, amount * 1, "bank")


@bot.command()
async def darknet(ctx):
    em = discord.Embed(title="Darknet-shop")

    for item in darknetshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name=name, value=f"{price} XMR | {desc}")

    await ctx.send(embed=em)


@bot.command()
async def buy(ctx, item, amount=1):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    # global kugel
    # global patrone

    # if item == "pc":
    #  users[str(user.id)]["crypto wallet"] = True
    # await update_bank(user, -11, "crypto wallet")

    res = await buy_this(ctx.author, item, amount)
    # if item == "Kugel":
    #   kugel += 1
    # if item == "Patrone":
    #   patrone += 1
    item = item

    if not res[0]:
        if res[1] == 1:
            await ctx.send("Diesen Gegenstand gibt es nicht.")
            return
        if res[1] == 2:
            await ctx.send(f"Du hast nicht genug XMR um {amount} {item}.")
            return
    now = datetime.datetime.now()
    nnow = now.strftime("%d-%m-%y %H:%M:%S")
    msg = f"{nnow} {user} hat {amount} {item} gekauft."

    def msgs():
        outfile = open('Finanzamt.txt', 'a')
        outfile.write("\n" + msg)

    msgs()
    await ctx.send(f"Du hast {amount} {item} gekauft.")


@bot.command(name="size")
async def size(ctx):
    cm = str("cm")
    idm = ctx.author.id
    # if idm == 922194085689851966:
    #   pps = -10
    #  await ctx.reply(str(pps)+cm)
    # elif idm != 922194085689851966 and idm != 631179768980570132 and idm != 699186870290087986:
    ppp = random.randint(1, 20)
    await ctx.reply(str(ppp) + cm)
    # elif idm == 699186870290087986:
    #   pppa = random.randint(69,69)
    #  await ctx.reply(str(pppa)+cm)
    # elif idm == 631179768980570132:
    #   ppp = 420
    #  await ctx.reply(str(ppp)+cm)


@bot.command(name="pringles")
async def p_price(ctx):
    pringles2 = pringles * mwz
    pringles3 = pringles + pringles2
    pringles3 = "2,72€"
    await ctx.reply(str(pringles3))


@bot.command()
@commands.is_owner()
async def DM(ctx, user: discord.User, *, message=None):
    msg = message or "Hey"
    message = ctx.message.id
    await ctx.message.delete()
    await user.send(msg)



@bot.event
async def on_message(message: discord.Message):
    if message.guild is None and not message.author.bot:
        print(message.content)
    await bot.process_commands(message)


# @bot.command()
# async def write(ctx, *, text):
#   with open("btc.json", "r") as f:
#     data=json.load(f)
#  data[ctx.guild.name]=text
# with open("btc.json", "w") as f:
#    json.dump(data, f)
# await ctx.send(f"ich habe **{text}** erfolgreich in die json geschrieben")

# @bot.command()
# async def read(ctx):
#   with open("btc.json", "r") as f:
#      data=json.load(f)
# await ctx.send(data)

# @bot.command()
# async def buy(ctx, *, text):
#    with open("btc.json", "r") as f:
#       data=json.load(f)
#   data[ctx.guild.name]=text
#  with open("btc.json", "w") as f:
#     json.dump(data, f)
# await ctx.send(f"Dein neuer Kontostand beträgt: " + [0] )


@bot.command()
async def inventar(ctx):
    # await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        Inventar = users[str(user.id)]["bag"]
    except:
        Inventar = []

    em = discord.Embed(title="Inventar")
    for item in Inventar:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name, value=amount)

    await ctx.send(embed=em)


@bot.command(name="price")
async def bt_price(ctx, *, text):
    pp = get_live_price(text)
    await ctx.reply(pp)


@bot.command(name="btc_p")
async def btc_price(ctx):
    pp = get_live_price("BTC-USD")
    await ctx.reply(pp)


@bot.command(name="d_g")
async def day_gainers(ctx):
    await ctx.reply(mc)


@bot.command(name="hello")
async def hello(ctx):
    await ctx.reply("hello")


@bot.command(name="d_l")
async def day_losers(ctx):
    await ctx.reply(dl)


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in darknetshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False, 1]
    # if name_ == "pc":
    #   return [True,"Worked"]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["bag"] = [obj]

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)

    msgf = f"{user} hat {cost * 0.19}€ Steuern bezahlt"

    await update_bank(user, cost * -1, "crypto wallet")
    await update_bank(user, cost * 1, "steuer")

    def msgr():
        outfile = open('Finanzamt.txt', 'a')
        outfile.write("\n" + msgf)

    msgr()

    return [True, "Worked"]


@bot.command()
async def XMR(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Bitte gebe die Menge an")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)

    if amount > bal[0]:
        await ctx.send("Du hast zu wenig Geld.")
        return
    if amount < 0:
        await ctx.send("Menge muss positiv sein.")
        return

    await update_bank(ctx.author, -170 * amount, "bank")
    await update_bank(ctx.author, amount, "crypto wallet")

    await ctx.send(f"Du hast {amount} XMR gekauft.")


@bot.command()
async def xmr_r(ctx, amount=None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Bitte gebe die Menge an")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)

    if amount > bal[0]:
        await ctx.send("Du hast zu wenig Geld.")
        return
    if amount < 0:
        await ctx.send("Menge muss positiv sein.")
        return

    await update_bank(ctx.author, -amount, "crypto wallet")
    await update_bank(ctx.author, amount * 1000, "bank")

    await ctx.send(f"Du hast {amount}XMR für {170 * amount}€ verkauft.")


@bot.command()
async def shoot_p(ctx, member: discord.Member, amount=None):
    await open_account(member)
    await inventar(ctx.author)

    # member = message.author.mention

    if amount == None:
        ctx.send("Bitte gib eine Anzahl der Schüsse an.")
        return

    global kugel

    mb = await get_bank_data(member)

    amount = int(amount)

    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send("Bitte gebe die Menge an")
        return

    bal = await inventar(ctx.author, "kugeln")
    bal = int(bal)
    amount = int(amount)

    if amount > bal[0]:
        await ctx.send("Du hast zu wenig Geld.")
        return
    if amount < 0:
        await ctx.send("Menge muss positiv sein.")
        return

    for cb in range(amount):
        c = random.randint(1, 10)
        if c == 1:
            await update_bank(member, -10000000000000000000000000000000000000000000000000000000000000000000000000000)
            await update_bank(ctx.author, -1, "kugel")
            await ctx.send(f"Du hast {member} erschossen. Er hat sein gesamtes Bargeld verloren.")

    # await update_bank_s(ctx.author,-1* amount, "bank")
    await update_bank_s(member, -1000000000000000000000000000, "wallet")

    await ctx.send(f"Du hast {member} erschossen. Er hat sein gesamtes Bargeld verloren.")


@bot.command()
async def sh(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)

    user = ctx.author
    users = await get_bank_data()

    if amount == None:
        await ctx.send("Bitte gebe die Anzahl der Schüsse / Versuche an")
        return


@commands.is_owner()
@bot.command()
async def finanzamt(ctx,member: discord.Member, steuersatz):
    await open_account(ctx.author)
    await open_account(member)

    await update_bank(member, )





@bot.command()
async def sell(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("Das gibt es nicht.")
            return
        if res[1] == 2:
            await ctx.send(f"Du hast nicht {amount} {item} in deinem Inventar.")
            return
        if res[1] == 3:
            await ctx.send(f"Du hast {item} nicht in deinem Inventar.")
            return

    user = ctx.author
    now = datetime.datetime.now()
    nnow = now.strftime("%d-%m-%y %H:%M:%S")
    msgss = f"{nnow} {user} hat {amount} {item} verkauft."

    def msgs():
        outfile = open('Finanzamt.txt', 'a')
        outfile.write("\n" + msgss)

    msgs()

    await ctx.send(f"Du hast {amount} {item} verkauft.")




# bal = await update_bank_s(ctx.author)
# amount = int(amount)

#   if amount > bal[0]:
#    await ctx.send("Du hast zu wenig Geld.")
#     return
#   if amount<0:
#      await ctx.send("Menge muss positiv sein.")
#   return
#   Inventar = users[str(user.id)]["bag": kugel]

#   if amount > Inventar:
#      ctx.send("Du hast nicht genug Schüsse.")
#     return


# for i in range(amount):
#       await inventar(ctx.author,-1 ,"bag":"kugel")
#   sch = random.randint(1,10)
#  if sch == 1:


#     await update_bank(member,-1* "wallet","wallet")
#    await ctx.send(f"Du hast {member} erschossen.")


@bot.command()
async def shoot(ctx, member: discord.Member, amount=1):
    await open_account(ctx.author)

    for i in range(amount):
        res = await sell_this_s(ctx.author, "kugel", 1)
        k = random.randint(1, 10)
        if k == 1:

            if not res[0]:
                if res[1] == 1:
                    await ctx.send("Das gibt es nicht.")
                    return
                if res[1] == 2:
                    await ctx.send(f"Du hast nicht {amount} kugeln in deinem Inventar.")
                    return
                if res[1] == 3:
                    await ctx.send(f"Du hast keine Kugeln.")
                    return

            await update_bank(member, -2000, "wallet")
            await ctx.send(f"Du hast {member} erschossen.")
            await ctx.send(
                f"@{member} Du wurdest von {ctx.author} erschossen. Dir wurden Kosten in Höhe von 5000€ pro Treffer berechnet.")


async def sell_this(user, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in darknetshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.7 * item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)

    await update_bank(user, cost, "crypto wallet")

    return [True, "Worked"]


async def sell_this_steuer(user, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in darknetshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.7 * item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)

    await update_bank(user, 0.19 * cost, "steuer")

    return [True, "Worked"]


async def sell_this_s(user, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in darknetshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.7 * item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]

    with open("Zentralbank.json", "w") as f:
        json.dump(users, f, indent=4)

    return [True, "Worked"]


@bot.command()
async def p656857645z45hrtuhzrt(ctx):
    user_id = "922194085689851966"
    await ctx.send(
        f"<@{user_id}>Als Honorar dafür, dass du so oft getaggt und erschossen wurdest, wurde dir eine Gutschrift in Höhe von 10.000€ erteilt.")


@bot.command()
@commands.is_owner()
async def c_s(message):
    await message.channel.purge(limit=1)
    await message.send("Das Casino schließt jetzt!")


# betrag = None
# async def steuer():

@bot.command()
@commands.is_owner()
async def purge(ctx, amount):
    amount = int(amount)
    await ctx.channel.purge(limit=amount)


@bot.command()
@commands.is_owner()
async def c_o(message):
    await message.channel.purge(limit=1)
    await message.send("Das Casino hat geöffnet!")


bot.run("TOKEN")
