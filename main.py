import csv
import discord
import os
import random
import zipfile
from discord.ext import tasks
from PIL import Image, ImageDraw, ImageFont
import requests

csvurl = os.environ['csvurl']
YOUR_DISCORD_BOT_TOKEN = os.environ['YOUR_DISCORD_BOT_TOKEN']
your_channel_id = int(os.environ['your_channel_id'])  # Convert to int if it's a numeric channel ID

intents = discord.Intents.default()
client = discord.Client(intents=intents)

quotes = []  # List to store fetched quotes
last_sent_quote = None  # To track the last sent quote

# Function to fetch CSV data from the Google Drive link
def fetch_csv_data():
    file_url = csvurl

    response = requests.get(file_url)
    if response.status_code == 200:
        content = response.content.decode('utf-8').splitlines()
        csv_reader = csv.DictReader(content)
        return list(csv_reader)  # Returning the CSV data as a list of dictionaries
    else:
        print("Failed to fetch the file.")
        return []

@tasks.loop(hours=18)
async def send_quote():
    global last_sent_quote
    global quotes

    if not quotes:
        quotes = fetch_csv_data()  # Fetching CSV data from Google Drive

    if quotes:
        shuffled_quotes = quotes[:]  # Create a copy of the quotes list
        random.shuffle(shuffled_quotes)  # Shuffle the quotes list

        for quote in shuffled_quotes:
            if quote != last_sent_quote:
                last_sent_quote = quote  # Update the last sent quote
                quote_text = quote.get('Quote')
                author_text = quote.get('Author')

                channel = client.get_channel(your_channel_id)  # Get the channel to send the message

                if channel:
                    message = f"**{quote_text}** - *{author_text}*"
                    await channel.send(message)
                    return  # Exit the loop after sending a quote
                else:
                    print("Channel not found. Please check your channel ID.")

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    send_quote.start()  # Start the quote-sending loop when the bot is ready

# Run the bot (replace 'YOUR_DISCORD_BOT_TOKEN' with your bot token)
client.run(YOUR_DISCORD_BOT_TOKEN)
