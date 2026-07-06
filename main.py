import secrets_file
import discord
from economy import check_account, user_balance, work
from moderation import clear_chat, kick_user, ban_user
from discord.ext import commands

setting = discord.Intents.default()
setting.message_content = True
bot = commands.Bot(command_prefix="!", intents=setting)


@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.tree.command(name="daily_coins", description="Claim your daily coins!")
async def daily_coins_slash(interaction: discord.Interaction):
    cash_earned = work(str(interaction.user.id))
    

@bot.tree.command(name="register", description="Register your account")
async def register(interaction: discord.Interaction):
    user_str_id = str(interaction.user.id)
    if user_str_id in user_balance:
        await interaction.response.send_message("you are already registered!")
    else:
        check_account(user_str_id)
        await interaction.response.send_message("Registration compelete")


@bot.tree.command(name="balance", description="For checkking your balance")
async def balance(interaction: discord.Interaction):
    user_str_id = str(interaction.user.id)
    await interaction.response.send_message(
        f"you currently have {user_balance[user_str_id]} coins!"
    )


@bot.tree.command(name="kick", description="Kick a member")
async def kick(
    interaction: discord.Interaction,
    member: discord.Member,
    reason: str = "No reason provided",
):
    status = await kick_user(member, reason, interaction.guild)
    await interaction.response.send_message(status)


@bot.tree.command(name="ban", description="ban a member")
async def ban(
    interaction: discord.Interaction,
    member: discord.Member,
    reason: str = "No reason provided",
):
    status = await ban_user(member, reason, interaction.guild)
    await interaction.response.send_message(status)


@bot.tree.command(
    name="clear", description="Clear a specified amount of messages"
)
async def clear(interaction: discord.Interaction, amount: int):
    await interaction.response.defer(ephemeral=True)
    status = await clear_chat(interaction.channel, amount)
    await interaction.followup.send(status)


bot.run(secrets_file.TOKEN)
