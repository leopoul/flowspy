# -*- coding: utf-8 -*- vim:fileencoding=utf-8:
# vim: tabstop=4:shiftwidth=4:softtabstop=4:expandtab

# Copyright (C) 2010-2014 GRNET S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.db import models
from django.contrib.auth.models import User
from peers.models import Peer


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    peer = models.ForeignKey(Peer)
    peers = models.ManyToManyField(Peer, related_name='peer_info')

    class Meta:
        permissions = (
            ("overview", "Can see registered users and rules"),
        )

    def __unicode__(self):
        return "%s:%s" % (self.user.username, self.peer.peer_name)

    def get_address_space(self):
        networks = self.domain.networks.all()
        if not networks:
            return False
        return networks
