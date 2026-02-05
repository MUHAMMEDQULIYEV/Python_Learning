import speedtest


def check_internet_speed():
    st = speedtest.Speedtest()
    print("Testing Speedtest")
    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    st.get_best_server()
    ping = st.results.ping

    return {"download": download, "upload": upload, "ping": ping}


speed = check_internet_speed()
print(speed["download"])
