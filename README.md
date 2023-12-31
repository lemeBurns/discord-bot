# Discord Quote Bot

## Description
This bot sends quotes to a Discord channel at regular intervals using a CSV file stored on Google Drive.

## Installation
To use this bot, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/lemejobless/discord-quote-bot.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    - `csvurl`: Google Drive link to the CSV file.
    - `YOUR_DISCORD_BOT_TOKEN`: Your Discord bot token.
    - `your_channel_id`: ID of the channel where you want to send quotes.

## Configuration
Set the following environment variables:

- `csvurl`: (String) Google Drive link to the CSV file.
- `YOUR_DISCORD_BOT_TOKEN`: (String) Your Discord bot token.
- `your_channel_id`: (Integer) ID of the channel where quotes will be sent.

## Usage
1. Ensure the environment variables are set.
2. Run the bot:

    ```bash
    python main.py
    ```

The bot will automatically start sending quotes to the specified Discord channel every 18 hours.

## How It Works
The bot fetches data from the provided Google Drive link (CSV format) containing quotes and authors. It then sends a random quote from the CSV file to the specified Discord channel.

## Dependencies
- `discord.py`
- `Pillow`

## File Structure
- `main.py`: Contains the Discord bot code.
- `requirements.txt`: File containing Python dependencies.

---


