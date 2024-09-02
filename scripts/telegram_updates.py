import requests
import json
import requests
import io
import asyncio
import os

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

main_data = {}
with open('json/modules.json') as f:
    main_data = json.load(f)

async def send_telegram_message(message, buttons):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML',
        'reply_markup': json.dumps({
            'inline_keyboard': buttons
        })
    }
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print(f"Message sent: {message}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response: {response.json()}")
    except Exception as err:
        print(f"An error occurred: {err}")
        
    return "Done"

async def send_telegram_photo(photo_url, caption, buttons):
    """Send a photo from a URL with a caption to a Telegram chat."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"

    response = requests.get(photo_url)
    response.raise_for_status()

    image_file = io.BytesIO(response.content)
    
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'caption': caption,
        'parse_mode': 'HTML',
        'reply_markup': json.dumps({
            'inline_keyboard': buttons
        })
    }
    files = {
        'photo': ('image.jpg', image_file, 'image/jpeg')
    }

    try:
        response = requests.post(url, data=payload, files=files)
        response.raise_for_status()
        print(f"Photo sent successfully with caption: {caption}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response: {response.text}")
    except Exception as err:
        print(f"An error occurred: {err}")
        
    return "Done"

def check_for_module_updates():
    try:
        last_versions = {}
        
        try:
            with open('json/last_versions.json', 'r') as f:
                last_versions = json.load(f)
        except FileNotFoundError:
            pass

        for module in main_data.get("modules", []):
            id = module.get("id")
            name = module.get("name")
            version = module.get("version")
            version_code = module.get("versionCode")
            source = module.get("track").get("source")
            desc = module.get("description")
            author = module.get("author")
            donate = module.get("donate")
            support = module.get("support")
            latest = module.get("versions")[-1]
 
            if id not in last_versions or last_versions[id] != version_code:
                message = f"""<b>{name}</b>
<i>Version:</i> {version} ({version_code})

{f"""📃 {desc}

<blockquote>{module.get("note").get("message")}</blockquote>""" if module.get("note") and module.get("note").get("message") else f"📃 {desc}"}

<b>By:</b> {author}
<b>Follow:</b> @MagiskModulesAltRepo
"""

                section_1 = []
                support_urls = []
                section_2 = []

                if latest.get("zipUrl"):
                    section_1.append({'text': '📦 Download', 'url': source})

                if source:
                    support_urls.append({'text': 'Source', 'url': source})
                if support:
                    support_urls.append({'text': 'Support', 'url': support})
                if donate:
                    section_2.append({'text': 'Donate', 'url': donate})

                buttons = [section_1,support_urls,section_2]

                if not module.get("cover"):
                    result = asyncio.run(send_telegram_message(message, buttons))
                else:
                    result = asyncio.run(send_telegram_photo(module.get("cover"), message, buttons))
                    
                last_versions[id] = version_code

                print(result)

        with open('json/last_versions.json', 'w') as f:
            json.dump(last_versions, f)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_for_module_updates()
