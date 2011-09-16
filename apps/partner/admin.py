#-- encoding: utf-8 --
#
# This file is part of I4P.
#
# I4P is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# I4P is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero Public License for more details.
# 
# You should have received a copy of the GNU Affero Public License
# along with I4P.  If not, see <http://www.gnu.org/licenses/>.
#
from django.db import models
from django.contrib import admin

from .models import Partner, PartnerPicture

class PartnerPictureInline(admin.TabularInline):
    model = PartnerPicture

class PartnerAdmin(admin.ModelAdmin):
    model = Partner
    inlines = (
        PartnerPictureInline,
        )


admin.site.register(Partner, PartnerAdmin)







