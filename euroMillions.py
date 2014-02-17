import mechanize
import cookielib
import html5lib, lxml, lxml.cssselect

class euroMillions:
    def results(self,date):
        # Browser
        br = mechanize.Browser()

        # Cookie Jar
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)

        # Browser options
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        r = br.open('http://es.euro-millions.com/resultados/'+date+'.asp')
        html = r.read()
        htmlparser = html5lib.HTMLParser(tree=html5lib.treebuilders.getTreeBuilder("lxml"), namespaceHTMLElements=False)
        page = htmlparser.parse(html)
        selector = lxml.cssselect.CSSSelector("#jsBallOrderCell li")
        numbers = []
        stars = []
        for li in selector(page):
            if (li.get("class") == "ball"):
                numbers.append(li.text)
            else:
                stars.append(li.text)
        return {"numbers":numbers,"stars":stars}


