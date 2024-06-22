import requests

def fetch_deezer_metadata(deezer_url):
    try:
        track_id = deezer_url.split("/")[-1]
        response = requests.get(f'https://api.deezer.com/track/{track_id}')
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching Deezer metadata: {e}")
        return None

def print_track_details(details):
    print(f"ISRC: {details.get('isrc', 'ISRC not found')}")
    print(f"Track Name: {details['title']}")
    print(f"Artist: {details['artist']['name']}")
    print(f"Album: {details['album']['title']}")
    print(f"Release Date: {details['release_date']}")
    print(f"Album Cover: {details['album']['cover_medium'] if 'cover_medium' in details['album'] else 'Cover not found'}")

def deezer_finder():
    deezer_url = input("Enter Deezer track URL: ").strip()
    metadata = fetch_deezer_metadata(deezer_url)
    if metadata:
        print_track_details(metadata)
    else:
        print("Failed to fetch Deezer metadata.")

def main():
    print("Deezer Metadata Grabber")
    deezer_finder()

if __name__ == "__main__":
    main()
