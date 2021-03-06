# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
"""
Defines forms for LogFittings and LogCondensers.
"""

# third party
import autocomplete_light

# local
from sifter.condensers.forms import (
    CondenserForm,
    FittingForm,
    FittingInlineForm,
    ParserForm
)
from .models import LogCondenser, LogFitting, LogParser


class LogParserForm(ParserForm):
    """
    Defines a form for adding or updating a LogParser using autocomplete
    fields.
    """

    class Meta(ParserForm.Meta):
        model = LogParser


class LogCondenserForm(CondenserForm):
    """
    Defines a form for adding or updating a LogCondenser using autocomplete
    fields.
    """

    class Meta(CondenserForm.Meta):
        model = LogCondenser


class LogFittingForm(FittingForm):
    """
    Defines a form for adding or updating a LogaFitting using autocomplete
    fields.
    """

    class Meta(FittingForm.Meta):
        model = LogFitting
        autocomplete_names = {
            'target_field': 'FilterTargetFieldsByLogCondenser'
        }


class LogFittingInlineForm(FittingInlineForm):
    """
    Defines an inline form for adding or updating a LogFitting using
    autocomplete fields.
    """

    class Meta(FittingInlineForm.Meta):
        model = LogFitting

