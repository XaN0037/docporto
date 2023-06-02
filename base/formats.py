from collections import OrderedDict

from api.models.news import *
from api.models.contact import *
from api.models.doctors import *


def contact_format(data,lan):
    return OrderedDict([
        ("Id", data.id),

        ("phone_mobile", data.phone_mobile),
        ("phone_clinica", data.phone_clinica),
        ("email", data.email),
        ("adress", eval(f"data.adress_{lan}")),
        ("instagramm", data.instagramm),
        ("telegram", data.telegram),
        ("facebook", data.facebook),
        ("twitter", data.twitter),
        ("odnoklassniki", data.odnoklassniki),
        ("youtube", data.youtube),
        ("locatsiya", data.locatsiya),
    ])


def doctor_format(data, lan="uz"):
    return OrderedDict([
        ("Id", data.id),
        ("name", eval(f"data.name_{lan}")),
        ("first_name", eval(f"data.first_name_{lan}")),
        ("middle_name", eval(f"data.middle_name_{lan}")),
        ("specialty", eval(f"data.specialty_{lan}")),
        ("about_doctor", eval(f"data.about_doctor_{lan}")),
        # ("motto", eval(f"data.motto_{lan}")),
        ("phone", data.phone),

        ("email", data.email),

        ("instagramm", data.instagramm),
        ("telegram", data.telegram),
        ("facebook", data.facebook),
        ("twitter", data.twitter),
        ("odnoklassniki", data.odnoklassniki),
        ("img", data.img.url),

    ])


def new_format(data,lan):
    return OrderedDict([
        ("Id", data.id),
        ("img", data.img.url),
        ("title", eval(f"data.title_{lan}")),
        ("short_desc", eval(f"data.short_desc_{lan}")),

    ])


def new_format_all(data,lan):
    return OrderedDict([
        ("Id", data.id),
        ("img", data.img.url),
        ("title", eval(f"data.title_{lan}")),
        ("short_desc", eval(f"data.short_desc_{lan}")),
        ("desc", eval(f"data.desc_{lan}")),
        ("date", data.date)

    ])
