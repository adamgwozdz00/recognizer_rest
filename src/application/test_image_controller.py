import unittest
import requests


class TestImageController(unittest.TestCase):

    URL = "..."
    TEST_IMAGE_PNG = "./resources/test.png"
    TEST_IMAGE_JPG = "./resources/test.jpg"

    def test_upload_image(self) -> None:
        self.__send_image(self.TEST_IMAGE_PNG)

        self.assertEqual('test'.upper(), 'TEST')

    def __send_image(self, path_to_img: str) -> None:
        files = {'file': open(path_to_img, 'rb')}
        requests.post(self.URL, files=files)


if __name__ == '__main__':
    unittest.main()
