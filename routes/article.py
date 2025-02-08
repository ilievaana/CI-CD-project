from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pydantic import SecretStr
from starlette import status

from models.article import Article

from config.db import article_collection

from schemas.article import serializeArticle, serializeArticleList

article = APIRouter()


@article.get('/')
async def find_all_articles():
    articles = article_collection.find()
    return serializeArticleList(articles)


@article.post('/')
async def create_article(article: Article):
    article_dict = dict(article)
    article_collection.insert_one(article_dict)
    return serializeArticle(article_dict)


@article.put('/{id}')
async def update_article(id: str, article: Article):
    article_dict = article.dict(exclude_unset=True)
    result = article_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": article_dict},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="Article not found")
    return serializeArticle(result)


@article.delete('/{id}')
async def delete_article(id: str):
    return serializeArticle(article_collection.find_one_and_delete({"_id": ObjectId(id)}))
