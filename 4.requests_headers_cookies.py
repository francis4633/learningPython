import requests

#国外网站，执行速度会慢一些
url = "https://github.com/francis4633"

#构建请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'cookie': '_octo=GH1.1.551206552.1634890254; tz=Asia%2FShanghai; _device_id=e68f3f6549c7205a942623fe6df58ddf; has_recent_activity=1; user_session=3Oel7voV_SFxLMlDiT-Fajn31ru9Vqyx6eNcB3f17iLQVWgn; __Host-user_session_same_site=3Oel7voV_SFxLMlDiT-Fajn31ru9Vqyx6eNcB3f17iLQVWgn; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=francis4633; _gh_sess=pktShEiSF7sokD0Sy03A%2FJihn3iGGlk4IPJfLrTtyovd7OqxZu%2F1V5pVkjmcjqM%2BaDpxMmdBbtzQHujVHX83yueq6BdALiSuLTaY1zrqTQlnTfNbCvZvFeqwyeSr0IrRQHhgNVycB4zjJeB4I3b1%2FARquFXE9lt20kNURvDl9PYyKj3hD12AE%2FOynFhBqawjFSJ6jp%2FoZOv0fMp07wuzdKwq51mYQE5rOP%2BCLC2OVQ7dzb3UDjxxJXSSgYIvJF%2Bzfmz76R09WotYb3EUtWOU6mJ7FHa1OsDuVEyTskKlOb779mjxPZrfu6QkuDWUrBXhnXT6fSCye9eu7jguDyny%2Beaz%2F%2Fzq%2B8VftqZ77QU2IiXTKQhOhNkjLlmWHfef21pUI1aT6F%2BFIz8GALRXHCpjFa1MkTemYN%2FSPPBUIy1slEGx%2FcT11HE82xYEQEPETBDhWK3mKPyco27mOJMujfQc4dnhO2VUCefg6AF1v18mbg16oOx2WFnBvpveidWJRpDpk11b%2Bp8%2F7Yl62xJ7Q5of%2FxB5w5ITy4L96vaq%2BBIw6rNzAZ98w3GAvtj6hcOQM2yZlh4fuVZotgU0r2t4%2Bde4e1Dz%2BdH6Mkeq6l253m2zDyDfmCmiYCZ4eA1PVg%2FiVI74u984SbWZo1rk7n6isxq4vas%2FIygDSjwZeEQobRZ9a21rpzCGHMCYv7bm4LrHkv0wK%2FFtDSOVn15lLu43F%2BqiDehsVh97WUCkcMOQxeq0LTkxeXDmwdK1Vo3i7CDCqgBD7fupU2lccXUT7Te4jjMf3iAEj4J7XGKOSbAYw%2F1UM74W69JpH2wAdOeIIu8M%2FFje8c3uPCh4PfzTPa3hdSve7aAKGXg8wf4CP65TiAp5pFypaBCJmrz01hNR6ZXNEGI9U%2FwuCDjQEvv3q2seqaYgWrXIokn7ZM9xDBi2xw%3D%3D--PeH%2FgHBXgy4w4BOt--zhZXUH3gw74AH0SRcpQtoA%3D%3D'
}


response = requests.get(url, headers=headers)

#将文件写入到github_with_cookies.html文件中，并生成一个github_with_cookies.html文件
with open("github_with_cookies1.html", 'wb')as f:
    f.write(response.content)
'''
#将文件写入到github_without_cookies2.html文件中，并生成一个github_without_cookies.html文件
with open("github_without_cookies2.html", 'wb')as f:
    f.write(response.content)
'''


