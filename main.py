import requests
import time

def read_messages(filename):
    with open(filename, "r") as file:
        messages = []
        current_message = []

        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                current_message.append(stripped_line)
            else:
                if current_message:
                    messages.append("\n".join(current_message))
                current_message = []

        if current_message:
            messages.append("\n".join(current_message))

        return messages

def main():
    channelID = ""
    token = ""
    headers = {
        "authorization": token,
        "Content-Type": "application/json"
    }
    filename = "file.txt"

    messages = read_messages(filename)

    while True:
        for message_content in messages:
            try:
                response = requests.post(
                    f"https://discord.com/api/v9/channels/{channelID}/messages",
                    headers=headers,
                    json={"content": message_content}
                )

                response.raise_for_status()

            except requests.exceptions.HTTPError as errh:
                print(f"HTTP Error: {errh}\nResponse content: {response.content}")
            except requests.exceptions.ConnectionError as errc:
                print(f"Error Connecting: {errc}")
            except requests.exceptions.Timeout as errt:
                print(f"Timeout Error: {errt}")
            except requests.exceptions.RequestException as err:
                print(f"Request Exception: {err}")

            time.sleep(10)

if __name__ == "__main__":
    main()
