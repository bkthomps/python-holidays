#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

import unittest

from datetime import date
from datetime import timedelta

import holidays
from holidays.constants import JAN, FEB, MAR, APR, MAY, AUG, OCT, NOV, DEC


class TestEcuador(unittest.TestCase):
    def setUp(self):
        self.holidays = holidays.EC(observed=True)

    def _check_all_dates(self, year, expected_holidays):
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        delta = timedelta(days=1)

        while start_date <= end_date:
            if start_date in expected_holidays:
                self.assertIn(start_date, self.holidays)
            else:
                self.assertNotIn(start_date, self.holidays)
            start_date += delta

    def test_2022_observed(self):
        # https://jezl-auditores.com/index.php/tributario/126-feriados-2022-ecuador
        year = 2022
        expected = [
            date(year, JAN, 1),
            date(year, FEB, 28),
            date(year, MAR, 1),
            date(year, APR, 15),
            date(year, MAY, 1),
            date(year, MAY, 2),
            date(year, MAY, 23),
            date(year, AUG, 12),
            date(year, OCT, 9),
            date(year, OCT, 10),
            date(year, NOV, 3),
            date(year, NOV, 4),
            date(year, DEC, 25),
            date(year, DEC, 26),
        ]
        self._check_all_dates(year, expected)
