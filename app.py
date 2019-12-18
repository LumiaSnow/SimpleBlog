#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse
from flask import Flask, request, redirect, send_from_directory, make_response
import json
from services.MarkdownService import MarkdownService
from services.FileService import FileService
import os
import uuid

app = Flask(__name__, static_url_path="/blog")


@app.route('/blog', methods=['GET'])
def index():
    return redirect("/blog/index.html")


@app.route('/blog/<article_type>/<article_name>', methods=['GET'])
def article(article_type, article_name):
    mks = MarkdownService()
    return mks.GetArticleHtml(article_type, article_name)


@app.route('/blog/articles', methods=['GET'])
def GetArticles():
    catagory = ""
    if "catagory" in request.args:
        catagory = request.args["catagory"]
    folder_path = "./articles"
    if catagory:
        folder_path = "{0}/{1}".format(folder_path, catagory)
    fs = FileService()
    posts = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = "{0}/{1}".format(dirpath, filename)
            modify_time = fs.get_FileModifyTime(filepath)
            file_catagory = dirpath.split('/')[-1].split('\\')[-1]
            posts.append({
                "file_name": filename.replace(".md", ""),
                "catagory": file_catagory,
                "modify_time": modify_time
            })
    posts.sort(key=lambda x: x["modify_time"], reverse=True)
    result = {"posts": posts}
    return json.dumps(result)


@app.route('/blog/catagories', methods=['GET'])
def GetCatagories():
    folder_path = "./articles"
    catagories = {"catagories": (
        [dirnames for _, dirnames, _ in os.walk(folder_path)])[0]}
    return json.dumps(catagories)


if __name__ == "__main__":
    app.run(debug=True)
