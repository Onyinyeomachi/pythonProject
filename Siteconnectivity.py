import urllib.request as urllib


def main(url):
    print("checking connectivity ")
    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was:", response.getcode())


print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check ")


if __name__ == "__main__":
    main(input_url)

