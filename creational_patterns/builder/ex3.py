from urllib.parse import urlencode, urljoin


class URLBuilder():
    def __init__(self, base_url: str):
        self._base_url = base_url.rstrip("/")
        self._paths = []
        self._params = {}
    
    def reset(self) -> None:
        self._paths = []
        self._params = {}

    def add_path(self, path: str):
        self._paths.append(str(path).strip("/"))
        return self

    def add_param(self, key: str, value: str):
        if value:
            self._params[key] = value
        return self

    def build(self) -> str:
        path = "/".join(self._paths)
        full_url = urljoin(self._base_url + "/",  path)

        if self._params:
            query_string = urlencode(self._params)
            full_url = f"{full_url}?{query_string}"
        
        self.reset()
        return full_url
    

if __name__ == "__main__":
    URL_DEFAULT = "https://api.teste.com"
    url_build = URLBuilder(URL_DEFAULT)

    # 1
    print("1")
    url_build.add_path("v1")
    url_build.add_path("libertadores")
    url_build.add_param("vasco", "campeão")
    full_url = url_build.build()
    print(full_url)

    # 2
    print("2")
    full_url = (
        url_build
        .add_path("v2")
        .add_path("campeão")
        .add_param("time", "vasco")
        .build()
    )
    print(full_url)
