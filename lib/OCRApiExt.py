from aip import AipOcr

class ExtAipOcr(AipOcr):

    __tableRecognitionAsyncURL = "https://aip.baidubce.com/api/v1/solution/form_ocr/request"
    __getTableRecognitionResult = "https://aip.baidubce.com/api/v1/solution/form_ocr/get_request_result"
    __testURL = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    def tableRecognitionAsync(self, image, options=None):
        """
            
        """

        options = options or {}
        data = {}
        data['image'] = image

        data = dict(data, **options)

        return self._request(self.__tableRecognitionAsyncURL , data)


    def getTableRecognitionResult(self, image, options=None):
        """
            
        """

        options = options or {}
        data = {}
        data['image'] = image

        data = dict(data, **options)

        return self._request(self.__getTableRecognitionResult , data)
 
    def testurl(self, image, options=None):
        """
            
        """

        options = options or {}
        data = {}
        data['image'] = image

        data = dict(data, **options)

        return self._request(self.__testURL , data)
        