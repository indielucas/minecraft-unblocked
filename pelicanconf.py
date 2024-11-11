AUTHOR = 'Minecraft Unblocked'
SITENAME = 'Minecraft Unblocked'
SITETITLE = 'Minecraft Unblocked | Free Online Games'
SITESUBTITLE = 'Play Minecraft unblocked for free on your browser. We provide multiplayer so you can play Minecraft online and join servers.'
SITEURL = "https://minecraft-unblocked.com"
PATH = "content"
# PATH = "content_test"
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'
STYLESHEET_URL = "/theme/css/style.css"

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ("Home", "/"),
    ("Minecraft Unblocked", "/tag/minecraft"),
)

DEFAULT_PAGINATION = 24

FEATURED = []

PLUGINS = ['search', 'sitemap', 'similar_posts']

SITEMAP = {
    "exclude": [
        "^/noindex/",  # starts with "/noindex/"
        "/tag/",       # contains "/tag/"
        "\.json$",     # ends with ".json"
    ]
}
SIMILAR_POSTS_MAX_COUNT = 16
STORK_INPUT_OPTIONS = {
    "base_directory": "output"
}

STATIC_PATHS = [
    'images',  # 你现有的图片目录
    'extra'    # 新建一个额外的目录存放这些文件
]
ARTICLE_EXCLUDES = ['extra']
PAGE_EXCLUDES = ['extra']
# 避免处理 HTML
READERS = {'html': None}

# 配置文件的目标路径
EXTRA_PATH_METADATA = {}

THEME = 'theme'
TAILWIND_CSS = True
