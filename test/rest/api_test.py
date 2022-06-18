import http.client
import os
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_multiply_zero(self):
        url = f"{BASE_URL}/calc/multiply/0/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_multiply_negative(self):
        url = f"{BASE_URL}/calc/multiply/-2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide_zero(self):
        url = f"{BASE_URL}/calc/divide/0/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/2/0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, 400)

    def test_api_divide_negative(self):
        url = f"{BASE_URL}/calc/divide/-2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_pow(self):
        url = f"{BASE_URL}/calc/pow/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_pow_zero(self):
        url = f"{BASE_URL}/calc/pow/2/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_pow_negative(self):
        url = f"{BASE_URL}/calc/pow/-2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_sqrt_zero(self):
        url = f"{BASE_URL}/calc/sqrt/0"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_sqrt_negative(self):
        url = f"{BASE_URL}/calc/sqrt/-4"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, 400)

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_log10_zero(self):
        url = f"{BASE_URL}/calc/log10/0"
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, 400)

    def test_api_log10_negative(self):
        url = f"{BASE_URL}/calc/log10/-4"
        
        with self.assertRaises(HTTPError) as cm:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(cm.exception.code, 400)