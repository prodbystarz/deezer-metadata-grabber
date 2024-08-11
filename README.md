# deezer-metadata-grabber

this python script fetches and displays metadata for a specified deezer track. the metadata includes isrc, track name, artist name, album name, release date, and album cover.

## setup

1. **clone the repository**:
    ```sh
    git clone https://github.com/prodbystarz/deezer-metadata-grabber.git
    cd deezer-metadata-grabber
    ```

2. **create a virtual environment (optional but recommended)**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # on windows use `venv\scripts\activate`
    ```

3. **install required packages**:
    ```sh
    pip install requests
    ```

4. **run the script**:
    ```sh
    python deezer_metadata_grabber.py
    ```

## usage

1. when prompted, enter the deezer track url.
2. the script will fetch and display the metadata for the specified track.

## example

enter deezer track url: https://www.deezer.com/track/123456789
```sh
isrc: us1234567890
track name: example track
artist: example artist
album: example album
release date: 2022-01-01
album cover: https://example.com/cover.jpg
```
