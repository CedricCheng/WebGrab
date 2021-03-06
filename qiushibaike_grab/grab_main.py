# coding=utf-8

from qiushibaike_grab import url_manager, html_parser, html_downloader, text_output


class QSBKGrab(object):

    def __init__(self):
        self.url = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = text_output.TextOutput()

    def craw(self, root):
        count = 0
        self.url.add_new_url(root)

        while self.url.has_new_url():
            new_url = self.url.get_new_url()
            print "craw %d : %s " % (count+1, new_url)
            html_cont = self.downloader.download(new_url)
            new_url, new_data = self.parser.parse(new_url, html_cont)
            self.url.add_new_url(new_url)
            self.output.collect_data(new_data)
            count += 1

            if count == 10:
                break

        print '\ncraw finished!'
        print '...writing to files'
        self.output.text_output()
        print '...done!'

if __name__ == '__main__':
    print '...start crawing'
    root_url = 'http://www.qiushibaike.com/hot/'
    spider = QSBKGrab()
    spider.craw(root_url)
