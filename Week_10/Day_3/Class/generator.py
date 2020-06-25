import requests
import time


endpoint = "https://newsapi.org/v2/top-headlines"
api_key = "35f754e21cb449b79e2be6dac7e5fb82"


def get_news(country=None, category=None, sources=None, pageSize=None, q=None, page=None):

    params = {
        'country': country,
        'category': category,
        'sources': sources,
        'pageSize': pageSize,
        'q': q,
        'page': page,
        'apiKey': api_key
    }

    params = {k: v for k, v in params.items() if v is not None}

    r = requests.get(endpoint, params=params)

    return r.json()


def render_element(article):

    news_element = f"""
                <div class="news-container">
                    <div class="left">
                        <img class="news-img" src="{article['urlToImage']}"/>
                    </div>

                    <div class="right">
                        <h3 class="news-title">{article['title']}</h3>
                        <p class="news-content">
                        {article['description']}
                        </p>
                        <small class="news-date">On {article['publishedAt']}</small>
                        <br>
                        <a href="article['url']">Read more</a>
                    </div>

                </div>
    """

    return news_element


def render_articles(articles, max_articles=10):
    html_code = ""
    for article in articles[:max_articles]:
        article_html = render_element(article)
        html_code += article_html + "\n"

    return html_code


# METHODS:
    # 1) USE A PREBUILT STRING --> Inject the news
    # --> Load it from a file (a template)
while True:
    print("Refreshing the page !")
    template = open("news_template.html", 'r').read()

    news = get_news(country='il')

    articles_html = render_articles(news['articles'])

    html_code = template.replace('{{ news }}', articles_html)
    html_code = html_code.replace('{{ news_dict }}', str(news))

    open('news.html', 'w').write(html_code)

    time.sleep(60)
