from urllib.parse import urlsplit

import pyshorteners


def shorten_url(url: str) -> str:
    url = url.strip()

    if not url:
        raise ValueError("URL cannot be empty.")

    if "://" not in url:
        url = f"https://{url}"

    parsed = urlsplit(url)

    if (
        parsed.scheme not in {"http", "https"}
        or not parsed.hostname
        or "." not in parsed.hostname
        or any(char.isspace() for char in url)
    ):
        raise ValueError("Please enter a valid URL.")

    return pyshorteners.Shortener(timeout=5).tinyurl.short(url)


def main() -> None:
    try:
        url = input("Enter URL: ")
        print(f"Short URL: {shorten_url(url)}")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nCancelled.")
    except Exception:
        print("Error: Unable to shorten URL. Check your connection.")


if __name__ == "__main__":
    main()