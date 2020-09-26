import datetime


class GetUsersRequestInfo:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        with open("info/users_info.txt", "a+") as file:
            time_info = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            url_info = request.build_absolute_uri()
            method_info = request.META.get("REQUEST_METHOD")
            file.write(f"{time_info} {url_info} {method_info}\n")

        response = self.get_response(request)

        return response
