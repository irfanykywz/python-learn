from ichrome import ChromeDaemon, Chrome


def main():
    with ChromeDaemon() as chromed:
        # run_forever means auto_restart
        chromed.run_forever(0)
        chrome = Chrome()
        tab = chrome.new_tab(url="https://pypi.org")
        tab.wait_loading(3)
        tab.js('alert("test ok")')
        tab.close()


if __name__ == "__main__":
    main()