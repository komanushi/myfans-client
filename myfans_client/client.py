from __future__ import annotations

import httpx

from myfans_client.exceptions import MyFansException
# https://api.myfans.jp/api/v2/users/f6257cde-61cc-428f-834b-c95d138d21fb/followers?page=1


class MyFansClient:
    def __init__(self, email: str, password: str, base_url: str = 'https://api.myfans.jp', debug: bool = False):
        self._email = email
        self._password = password
        self._base_url = base_url
        self._session = httpx.Client()
        self.debug = debug
        self._xsrf_token = None
        if self.debug:
            import logging
            logging.basicConfig(
                format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                level=logging.DEBUG
            )

        self.logged_in = self.login()

    @property
    def base_url(self):
        return self._base_url

    @property
    def header(self):
        base = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Origin': 'https://myfans.jp',
            'Referer': 'https://myfans.jp/',
            'google-ga-data': 'event328',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        return base

    def login(self) -> bool:
        try:
            res = self._post(
                'api/v1/sign_in',
                json={
                    'email': self._email,
                    'password': self._password,
                    'locale': 'ja',
                },
                headers=self.header,
            )
            return True
        except MyFansException as e:
            raise e

    def _post(self, path: str, *arg, **kwargs):
        return self._request('POST', path, *arg, **kwargs)

    def _get(self, path: str, *arg, **kwargs):
        return self._request('GET', path, *arg, **kwargs)

    def _put(self, path: str, *arg, **kwargs):
        return self._request('PUT', path, *arg, **kwargs)

    def _request(self, method: str, path: str, *arg, **kwargs):
        url = f'{self.base_url}/{path}'
        response = self._session.request(method, url, *arg, **kwargs)
        response_json = response.json()
        if 'error' in response_json:
            raise MyFansException(response_json['error'])

        return response_json
