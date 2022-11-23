import os

# Set environment variables
os.environ['BOT_API_KEY'] = input("Input telegram bot api key from @BotFather: ") 
os.environ['SEARCH_API_KEY'] = input("Input search engine api key from https://serpapi.com/: ")
os.environ['TG_ADMIN_ID'] = input("Input admin tg user ID: ")