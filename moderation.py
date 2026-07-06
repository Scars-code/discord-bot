import discord
import os
async def clear_chat(channel,amount):
    amount=int(amount)
    if amount > 0:
        await channel.purge(limit=amount+1)
        return(f"successfully {amount} messages! ")
    else:
        return("failed to clear chat due to invalid input")
async def kick_user(target_user,reason="",guild=None):
    if guild==None:
        return("Error: Guild context missing.")
    if not guild.me.guild_permissions.kick_members:
        return("permission to kick members is not granted")
    await target_user.kick(reason=reason)
    return(f"Kicked {target_user} for reason: {reason}")
        
async def ban_user(target_user,reason="",guild=None):
    if guild==None:
        return
    if not guild.me.guild_permissions.ban_members:
        return("permission to ban members is not granted")
    await target_user.ban(reason=reason)
    return(f"Banned {target_user} for reason: {reason}")

