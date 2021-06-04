
import requests, time

print("\n---> This is a Site Connectivity Checker <---\n")
print("Input your URL in the following format 'http://www.google.com'")


def comin():
    url = input("Enter a URL to check: ")
    diff = input(f"Ping {url} on an interval of (seconds): ")

    return url, diff
url, diff = comin()

# response = requests.get(url)
while True:

    try:
        response = requests.get(url)
        status_code = response.status_code
        # print("Enter 'Q' to stop")
        if status_code == 200:
            print(f"{url} is LIVE, the site responded with a status code {status_code}")
        if status_code == 301:
            print(f"{url} is UNAVAILABLE, the site Moved Permanently and responded with a status code {status_code}")
        if status_code == 302:
            print(f"{url} is UNAVAILABLE, the site Moved TEMPORARILY and responded with a status code {status_code}")
        if status_code == 404:
            print(f"{url} is UNAVAILABLE, the site was NOT FOUND and responded with a status code {status_code}")
        if status_code == 500:
            print(f"{url} is UNAVAILABLE, the site is having an INTERNAL SERVER ERROR and responded with a status code {status_code}")
        if status_code == 503:
            print(f"{url} is UNAVAILABLE, the site's SERVICE is UNAVAILABLE and responded with a status code {status_code}")


    except Exception as e:
        print(e)
        url = input("\nEnter another URL to check: ")
        diff = input("Ping the following site on an interval of (seconds): ")

    time.sleep(int(diff))
