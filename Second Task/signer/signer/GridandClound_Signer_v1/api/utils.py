from flask import Response


def resp_xml(text, status):
    r = Response(response=text, status=status, mimetype="application/xml")
    r.headers["Content-Type"] = "text/xml; charset=utf-8"
    return r