import time

from django.core.exceptions import PermissionDenied


count_ip_request = {}


class FilterIpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ban_ips = []
        ip = request.META.get("REMOTE_ADDR")
        if ip in ban_ips:
            raise PermissionDenied

        response = self.get_response(request)

        return response


class CountIpRequest:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")

        if ip not in count_ip_request:
            count_ip_request[ip] = {"count": 1, "time": int(time.time()), "start_count": 1}
        else:
            count_ip_request[ip]["count"] += 1

        if not count_ip_request[ip]["count"] % 5:
            time.sleep(3)
        response = self.get_response(request)
        return response


class MaxIpRequestInNSecond:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if int(time.time()) - count_ip_request[ip]["time"] <= 15:
            if count_ip_request[ip]["count"] - count_ip_request[ip]["start_count"] >= 6:
                raise PermissionDenied
        else:
            count_ip_request[ip]["time"] = int(time.time())
            count_ip_request[ip]["start_count"] = count_ip_request[ip]["count"]

        response = self.get_response(request)

        return response

