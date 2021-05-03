import requests
import pprint


def main():
    params = {"zipcode": '1620063'}
    url = "http://zipcloud.ibsnet.co.jp/api/search"

    response = requests.post(url, params=params)

    json_response = response.json()

    pprint.pprint(json_response)
    print(json_response)
    print(json_response["results"])
    print(json_response["results"][0]["address1"])


if __name__ == '__main__':
    main()
