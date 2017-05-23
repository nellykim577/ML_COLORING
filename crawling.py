from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4, storage={'root_dir': 'wp'})

google_crawler.crawl(keyword='western painting', max_num=5000,
	date_min=None, date_max=None, min_size=None, max_size=None)
