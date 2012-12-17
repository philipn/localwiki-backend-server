from django.core.urlresolvers import reverse

import recentchanges
from recentchanges import RecentChanges

from models import PageValue


class InfoboxChanges(RecentChanges):
    classname = 'infobox'

    def queryset(self, start_at=None):
        if start_at:
            return PageValue.versions.filter(version_info__date__gte=start_at)
        return PageValue.versions.all()

    def page(self, obj):
        return obj.entity

    def title(self, obj):
        return 'Info on page "%s"' % self.page(obj).name

    def diff_url(self, obj):
        return reverse('infobox:infobox-compare-dates', kwargs={
            'slug': self.page(obj).pretty_slug,
            'date1': obj.version_info.date,
        })

    def as_of_url(self, obj):
        return reverse('infobox:infobox-as_of_date', kwargs={
            'slug': self.page(obj).pretty_slug,
            'date': obj.version_info.date,
        })

recentchanges.register(InfoboxChanges)
