# Discord AI-Powered Bot

## Overview
This is a multifunctional Discord bot with AI-powered chat, music playback, reminders, polls, and text summarization capabilities. It integrates Google Gemini AI for chatbot responses, YouTube audio streaming, and task scheduling for reminders. The bot is built using discord.py, yt-dlp, transformers, and apscheduler.

## Features
- *AI Chat*: Leverages Google Gemini AI (gemini-1.5-flash) for natural language responses.
- *Music Playback*: Streams high-quality audio from YouTube.
- *Reminders*: Allows users to schedule reminders that the bot will send as private messages.
- *Polls*: Enables users to create interactive polls with up to 10 options.
- *Summarization*: Uses a transformer-based model (facebook/bart-large-cnn) to summarize long texts.
- *Voice Channel Management*: Joins and leaves voice channels dynamically.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- FFmpeg (apt install ffmpeg -y on Linux)

### Setup
1. Install dependencies:
   bash
   pip install -U discord.py[voice] pynacl nest_asyncio youtube_dl transformers google-generativeai apscheduler yt-dlp
   
2. Set up environment variables:
   - Replace YOUR_GEMINI_KEY with your Google Gemini AI API key.
   - Replace YOUR_DISCORD_TOKEN with your Discord bot token.


### Commands
| Command       | Description |
|--------------|-------------|
| !chat <message> | Interact with the AI chatbot. |
| !remind HH:MM YYYY-MM-DD <message> | Sets a reminder. |
| !poll <question> <option1> <option2> ... | Creates a poll (2-10 options). |
| !join | Joins the voice channel. |
| !play <url> | Plays music from YouTube. |
| !stop | Stops music playback and clears the queue. |
| !summarize <text> | Summarizes the given text. |

## Future Enhancements (If More Time is Available)
- *Better AI Responses*: Implement memory/context retention.
- *Enhanced Music Features*: Add playlists and volume control.
- *Advanced Reminders*: Recurring reminders and event-based notifications.
- *Admin Tools*: Moderation features like message filtering and auto-kick for inactive users.
- *Custom Integrations*: Connect to external APIs for weather, news, or stock market updates.
