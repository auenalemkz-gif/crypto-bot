import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
POSTS_PER_DAY = int(os.getenv("POSTS_PER_DAY", "80"))
MAX_CAPTION_LENGTH = 1024

RSS_FEEDS = [
{"url": "https://bits.media/rss/", "sport": "Крипто", "lang": "ru"},
{"url": "https://coinspot.io/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://cryptonews.net/ru/rss/", "sport": "Крипто", "lang": "ru"},
{"url": "https://ru.beincrypto.com/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://forklog.com/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://incrypted.com/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://cryptorussia.ru/rss", "sport": "Крипто", "lang": "ru"},
{"url": "https://www.rbc.ru/crypto/rss/", "sport": "Крипто", "lang": "ru"},
{"url": "https://bloomchain.ru/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://coinpress.ru/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://bitjournal.media/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://crypto.ru/feed/", "sport": "Крипто", "lang": "ru"},
{"url": "https://www.coindesk.com/arc/outboundfeeds/rss/", "sport": "Крипто", "lang": "en"},
{"url": "https://cointelegraph.com/rss", "sport": "Крипто", "lang": "en"},
{"url": "https://decrypt.co/feed", "sport": "Крипто", "lang": "en"},
{"url": "https://bitcoinmagazine.com/.rss/full/", "sport": "Крипто", "lang": "en"},
{"url": "https://cryptoslate.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://cryptobriefing.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://ambcrypto.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://newsbtc.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://www.theblock.co/rss.xml", "sport": "Крипто", "lang": "en"},
{"url": "https://beincrypto.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://cryptonews.com/news/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://u.today/rss", "sport": "Крипто", "lang": "en"},
{"url": "https://dailyhodl.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://coinjournal.net/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://www.coinspeaker.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://zycrypto.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://cryptopotato.com/feed/", "sport": "Крипто", "lang": "en"},
{"url": "https://coinpedia.org/feed/", "sport": "Крипто", "lang": "en"},
]

SYSTEM_PROMPT = """Ты редактор крипто Telegram-канала для СНГ аудитории. Пишешь живые эмоциональные посты ТОЛЬКО на русском языке. Если новость на английском — переведи и адаптируй на русский. Длина 150-300 символов если есть фото, до 800 если нет. Добавляй эмодзи 💎🚀📈💰🔥 и 3-5 хэштегов: #биткоин #крипто #bitcoin #ethereum #блокчейн. Формат HTML."""
