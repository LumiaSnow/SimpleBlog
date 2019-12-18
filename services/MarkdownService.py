
import markdown
import os
import codecs
# from markdown.extensions.wikilinks import WikiLinkExtension


class MarkdownService(object):

    __instance = False

    __FileFolder = "./articles"
    __FileBaseUrl = "/blog"
    __FileDownloadBaseUrl = "/blog/download"

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = object.__new__(cls)
            return cls.__instance

    def __init__(self):
        pass

    def __Md2Html(self, md_text):
        exts = ['markdown.extensions.toc',\
                    # WikiLinkExtension(base_url='https://en.wikipedia.org/wiki/',\
                    #     end_url='#Hyperlinks_in_wikis'),\
                    'markdown.extensions.sane_lists',\
                    'markdown.extensions.codehilite',\
                    'markdown.extensions.abbr',\
                    'markdown.extensions.attr_list',\
                    'markdown.extensions.def_list',\
                    'markdown.extensions.fenced_code',\
                    'markdown.extensions.footnotes',\
                    # 'markdown.extensions.smart_strong',\
                    'markdown.extensions.meta',\
                    'markdown.extensions.nl2br',\
                    'markdown.extensions.tables']
        return markdown.markdown(md_text, extensions=exts)

    def __BuildArticlePath(self, article_type, article_name):
        return os.path.join(self.__FileFolder, article_type, article_name)

    def GetArticleHtml(self, article_type, article_name):
        md_text = self.GetArticleMd(article_type, article_name)
        return self.__Md2Html(md_text)

    def GetArticleMd(self, article_type, article_name):
        filepath = self.__BuildArticlePath(article_type, article_name)
        filename = filepath + ".md"
        input_file = codecs.open(filename, mode="r", encoding="utf-8")
        return input_file.read()

    def GetArticleList(self):
        pass

    def __GetAllFilesName(self):
        return ([files for _, _, files in os.walk(self.__FileFolder)])[0]

    def BuildFileUrl(self, fileName):
        return "{0}/{1}".format(self.__FileBaseUrl, fileName)

    def BuildFileDownloadUrl(self, fileName):
        return "{0}/{1}".format(self.__FileDownloadBaseUrl, fileName)

    def GetAllFilesInfo(self):
        filesName = self.__GetAllFilesName()
        filesInfo = (
            [
                {
                    "image_name": fileName.replace(".md", ""),
                    "image_url": self.BuildFileUrl(fileName.replace(".md", ""))
                    # "image_download_url": self.BuildFileDownloadUrl(fileName.replace(".md", ""))
                } for fileName in filesName
            ]
        )
        return filesInfo
