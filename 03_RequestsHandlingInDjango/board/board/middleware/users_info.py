import datetime


class GetUsersRequestInfo:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        with open("info/users_info.txt", "a+") as file:
            string = datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + " " + request.build_absolute_uri() + " " + \
                     request.META.get("REQUEST_METHOD") + "\n"
            file.write(str(string))

        response = self.get_response(request)

        return response
