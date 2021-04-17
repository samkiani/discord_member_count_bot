# Discord Member Count Bot

Simple Discord bot which displays the members in a Discord server in the channels list. 

## Setup and Run

Requires Python `3.6.8+`.

Install necessary packages (locally):

```bash
python3 -m pip install -r requirements.txt
```

Copy `.env.sample` to `.env`

```bash
cp .env.sample .env
```

Open `.env` and insert the following fields:

| Field           | Explanation                                                           |
|-----------------|-----------------------------------------------------------------------|
| `DISCORD_TOKEN` | Discord bot token                                                     |

Copy `data.json.sample` to `data.json`

```bash
cp data.json.sample data.json 
```

Open `data.json` and insert the following fields for your server:

| Field           | Explanation                                                           |
|-----------------|-----------------------------------------------------------------------|
| `id`            | ID your of Discord server                                             |
| `channel_id`    | ID of the channel which should display the member count               |
| `suffix`        | Name displayed after the number of the member count                   |

Start Bot:

```bash
python3 bot.py
```

## Credits
![K0nze Logo](./images/k_logo_30x30.png "Logo") Created by Konstantin (Konze) Lübeck

 * Twitch: [twitch.tv/k0nze](https://twitch.tv/k0nze) 
 * Youtube: [youtube.com/k0nze](https://youtube.com/k0nze) 
 * Patreon: [patreon.com/k0nze](https://patreon.com/k0nze) 
 * Discord: [discord.k0nze.gg](https://discord.k0nze.gg) 
 * Twitter: [twitter.com/k0nze_gg](https://twitter.com/k0nze_gg) 
 * TikTok: [tiktok.com/@k0nze.gg](https://tiktok.com/@k0nze.gg) 