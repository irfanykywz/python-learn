# clear cache
assert await tab.clear_browser_cache()

# close tab
await tab.close()

 # load url for other tests
                await tab.set_url('http://httpbin.org/forms/post')

                tab._target_info

                tab.info

                chrome.get_memory()