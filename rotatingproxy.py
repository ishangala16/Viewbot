from proxyscrape import create_collector
collector = create_collector('my-collector', 'https')
# collector.apply_filter({'type':'https','anonymous':True})

proxy=collector.get_proxy()

proxy1 = proxy.host + ":" + proxy.port
print(proxy1)

proxies = {"https": proxy1}







