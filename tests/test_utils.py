import pytest
from src.utils import *

def test_get_operations_date():
    assert get_operations_date([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]
    assert get_operations_date([{}]) == []


def test_sort_operations_date():
    assert sort_operations_date([{"date": "2019-07-03T18:35:29.512364"},
                                 {"date": "2018-06-30T02:08:58.425572"},
                                 {"date": "2019-04-04T23:20:05.206878"},
                                 {"date": "2019-03-23T01:09:46.296404"},
                                 {"date": "2018-12-20T16:43:26.929246"},
                                 {"date": "2019-07-12T20:41:47.882230"}]) == [{'date': '2019-07-12T20:41:47.882230'},
                                                                              {'date': '2019-07-03T18:35:29.512364'},
                                                                              {'date': '2019-04-04T23:20:05.206878'},
                                                                              {'date': '2019-03-23T01:09:46.296404'},
                                                                              {'date': '2018-12-20T16:43:26.929246'}]


def test_change_data():
    assert change_data([{"date": "2018-08-19T04:27:37.904916"}]) == ["19.08.2018"]


def test_mask_amount_number():
    assert mask_amount_number([{"to": "Счет 38976430693692818358"}]) == ["**1835"]


def test_mask_card_number():
    assert mask_card_number([{"description": "Перевод организации", "from": "Счет 48894435694657014368"}]) == ["Счет 4889 44** **** 5701 4368"]


