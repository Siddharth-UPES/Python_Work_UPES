# import requests
# import os

# def download_file(url, file_name):
#     '''
#     Function to download a file
#     It takes two arguments: URL and Filename
#     '''
#     # Ensure file name doesn't include the URL
#     _, extension = os.path.splitext(url)  # Get the extension from the URL
#     if not extension:  # If no extension is found, default to .bin
#         extension = '.bin'
    
#     file_name = f"{file_name}{extension.lower()}"  # Generate the full file name

#     # Send a GET request to the provided URL
#     response = requests.get(url)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Open a local file in binary write mode and save the content
#         with open(file_name, 'wb') as file:
#             file.write(response.content)
#         print(f"File '{file_name}' downloaded successfully.")
#     else:
#         print(f"Failed to download file. Status code: {response.status_code}")




import requests


def download_file(url, file_name):
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")


if __name__ == "__main__":

    url = 'https://similarpng.com/download/?id=48255&token=907edb0aa6986220dbffb79a788596ee'
    file_name = 'file'
    download_file(url, file_name)
    # label enter url

    # url entry