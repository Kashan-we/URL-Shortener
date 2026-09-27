import pyshorteners

url = input("Enter the URL: ")

def shortenurl(url):
    s = pyshorteners.Shortener()
    short_link = s.tinyurl.short(url)
    print(f"The shortened link: {short_link}")

shortenurl(url)