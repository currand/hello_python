import urllib2

def get_stock_html(ticker_symbol):
    opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
    )
    opener.addheaders = [
        ('User-agent',
         "Mozilla/4.0 (compatible; MSIE 7.0; "
         "Windows NT 5.1; .NET CLR 2.0.50727; "
         ".NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
    ]

    url = "http://finance.yahoo.com/q?s=" + ticker_symbol
    response = opener.open(url)
    return ''.join(response.readlines())

if __name__ == '__main__':
    print get_stock_html('GOOG')