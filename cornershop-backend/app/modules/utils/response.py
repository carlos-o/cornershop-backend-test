import json


class ResponseDetail:
    code = 500
    data = {}
    message = "internal server error"
    errors = {}
    success = False

    def success_detail(self, code=200, data=None, message="ok", success=True):
        info = {
            "success": self.success if success is None else success,
            "code": self.code if code is None else code,
            "data": self.data if data is None else data,
            "message": self.message if message is None else message,
        }
        return info

    def errors_detail(self, code=500, data=None, message="Internal Server Error", error={}, success=False):
        if error:
            if type(error) is str:
                try:
                    error = json.loads(error)
                except json.decoder.JSONDecodeError:
                    pass
        info = {
            "success": self.success if success is None else success,
            "code": self.code if code is None else code,
            "data": self.data if data is None else data,
            "message": self.message if message is None else message,
            "errors": self.errors if error is None else error,
        }
        return info

    def not_found_detail(self, code=404, data=None, message="Not found.", success=True):
        info = {
            "success": self.success if success is None else success,
            "code": self.code if code is None else code,
            "data": self.data if data is None else data,
            "message": self.message if message is None else message,
            "errors": {"error": message}
        }
        return info
