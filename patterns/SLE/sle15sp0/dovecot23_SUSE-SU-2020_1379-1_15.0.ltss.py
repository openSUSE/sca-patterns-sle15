#!/usr/bin/python3
#
# Title:       Important Security Announcement for dovecot23 SUSE-SU-2020:1379-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0 LTSS
# Source:      Security Announcement Parser v1.5.2
# Modified:    2020 Nov 16
#
##############################################################################
# Copyright (C) 2020 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jason.record@suse.com)
#
##############################################################################

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "dovecot23"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-May/006846.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'dovecot23'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:1379-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'dovecot23': '2.3.10-4.22.1',
			'dovecot23-backend-mysql': '2.3.10-4.22.1',
			'dovecot23-backend-mysql-debuginfo': '2.3.10-4.22.1',
			'dovecot23-backend-pgsql': '2.3.10-4.22.1',
			'dovecot23-backend-pgsql-debuginfo': '2.3.10-4.22.1',
			'dovecot23-backend-sqlite': '2.3.10-4.22.1',
			'dovecot23-backend-sqlite-debuginfo': '2.3.10-4.22.1',
			'dovecot23-debuginfo': '2.3.10-4.22.1',
			'dovecot23-debugsource': '2.3.10-4.22.1',
			'dovecot23-devel': '2.3.10-4.22.1',
			'dovecot23-fts': '2.3.10-4.22.1',
			'dovecot23-fts-debuginfo': '2.3.10-4.22.1',
			'dovecot23-fts-lucene': '2.3.10-4.22.1',
			'dovecot23-fts-lucene-debuginfo': '2.3.10-4.22.1',
			'dovecot23-fts-solr': '2.3.10-4.22.1',
			'dovecot23-fts-solr-debuginfo': '2.3.10-4.22.1',
			'dovecot23-fts-squat': '2.3.10-4.22.1',
			'dovecot23-fts-squat-debuginfo': '2.3.10-4.22.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

