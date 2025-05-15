from abc import ABC, abstractmethod
from urllib.parse import urlencode, urljoin


class Builder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def add_path(self) -> None:
        pass

    @abstractmethod
    def add_param(self) -> None:
        pass


class URL():
    def __init__(self, base_url: str):
        self._base_url = base_url.rstrip("/")
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
        
        return full_url
    
class URLBuilder(Builder):
    def __init__(self, base_url: str):
        self._base_url = base_url.rstrip("/")
        self.reset()
    
    def reset(self) -> None:
        self._product = URL(self._base_url)

    def add_path(self, path: str):
        self._product.add_path(path)
        return self

    def add_param(self, key: str, value: str):
        self._product.add_param(key, value)
        return self

    @property
    def product(self) -> URL:
        product = self._product
        self.reset()
        return product


if __name__ == "__main__":
    URL_DEFAULT = "https://api.teste.com"
    url_build = URLBuilder(URL_DEFAULT)

    # 1
    print("1")
    url_build.add_path("v1")
    url_build.add_path("libertadores")
    url_build.add_param("vasco", "campeão")
    full_url = url_build.product.build()
    print(full_url)

    # 2
    print("2")
    full_url = (
        url_build
        .add_path("v2")
        .add_path("campeão")
        .add_param("time", "vasco")
        .product.build()
    )
    print(full_url)
