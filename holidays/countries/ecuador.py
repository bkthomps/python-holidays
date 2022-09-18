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

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAY, AUG, OCT, NOV, DEC
from holidays.constants import TUE, WED, THU, SAT, SUN
from holidays.holiday_base import HolidayBase


class Ecuador(HolidayBase):
    country = "EC"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _set_holiday(self, dt: date, name: str) -> None:
        if dt.weekday() == SAT:
            self[dt] = name
            if self.observed and dt.month != JAN and dt.day != 1:
                self[dt + rd(days=-1)] = name + " (Observed)"
        elif dt.weekday() == SUN:
            self[dt] = name
            if self.observed:
                self[dt + rd(days=+1)] = name + " (Observed)"
        if not self.observed:
            self[dt] = name
        elif dt.weekday() == TUE:
            if dt.month != JAN and dt.day != 1:
                self[dt + rd(days=-1)] = name + " (Observed)"
        elif dt.weekday() == WED:
            self[dt + rd(days=+2)] = name + " (Observed)"
        elif dt.weekday() == THU:
            self[dt + rd(days=+1)] = name + " (Observed)"

        if self.observed and dt.month == JAN and dt.day == 1:
            next_year = date(dt.year + 1, JAN, 1)
            if next_year.weekday() == TUE or next_year.weekday() == SAT:
                self[date(dt.year, DEC, 31)] = name + " (Observed)"

    def _populate(self, year):
        """
        https://www.turismo.gob.ec/wp-content/uploads/2022/01/FERIADOS-NACIONALES_2022.pdf

        If a holiday is on a Saturday, it gets observed on the Friday right before it.
        If a holiday is on a Sunday, it gets observed on the Monday right after it.

        If a holiday is on a Tuesday, it gets moved to Monday right before it.
        If a holiday is on a Wednesday or Thursday, it gets move to the Friday.
        """

        self._set_holiday(date(year, JAN, 1), "Año Nuevo [New Year's]")

        self[
            easter(year) - rd(days=48)
        ] = "Lunes de Carnaval [Monday of Carnival]"

        self[
            easter(year) - rd(days=47)
        ] = "Martes de Carnaval [Tuesday of Carnival]"

        self[easter(year) - rd(days=2)] = "Viernes Santo [Good Friday]"

        self._set_holiday(date(year, MAY, 1), "Día del Trabajo [Labor Day]")

        self._set_holiday(
            date(year, MAY, 24),
            "Batalla del Pinchincha [Battle of Pinchincha]",
        )

        self._set_holiday(
            date(year, AUG, 10),
            "Primer Grito de Independencia [Independence Day]",
        )

        self._set_holiday(
            date(year, OCT, 9),
            "Independencia de Guayaquil [Independence of Guayaquil]",
        )

        # TODO: these next two holidays have interesting logic, change the
        # fewest number of them so that there are no gaps in days off

        self._set_holiday(
            date(year, NOV, 2), "Día de los Difuntos [Day of the Dead]"
        )

        self._set_holiday(
            date(year, NOV, 3),
            "Independencia de Cuenca [Independence of Cuenca]",
        )

        self._set_holiday(date(year, DEC, 25), "Navidad [Christmas]")


class EC(Ecuador):
    pass


class ECU(Ecuador):
    pass
