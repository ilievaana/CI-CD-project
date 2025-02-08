from bson import ObjectId

from models.article import Article


def serializeArticle(article: dict) -> dict:
    if "_id" in article and isinstance(article["_id"], ObjectId):
        article["_id"] = str(article["_id"])
    return article


def serializeArticleList(articles: list) -> list:
    return [serializeArticle(article) for article in articles]