#!/usr/bin/python3
#
# Title:       Important Security Announcement for mozilla-nss SUSE-SU-2020:1677-1
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
META_COMPONENT = "mozilla-nss"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-June/006980.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'mozilla-nss'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:1677-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libfreebl3': '3.53-3.40.1',
			'libfreebl3-32bit': '3.53-3.40.1',
			'libfreebl3-32bit-debuginfo': '3.53-3.40.1',
			'libfreebl3-debuginfo': '3.53-3.40.1',
			'libfreebl3-hmac': '3.53-3.40.1',
			'libfreebl3-hmac-32bit': '3.53-3.40.1',
			'libsoftokn3': '3.53-3.40.1',
			'libsoftokn3-32bit': '3.53-3.40.1',
			'libsoftokn3-32bit-debuginfo': '3.53-3.40.1',
			'libsoftokn3-debuginfo': '3.53-3.40.1',
			'libsoftokn3-hmac': '3.53-3.40.1',
			'libsoftokn3-hmac-32bit': '3.53-3.40.1',
			'mozilla-nspr': '4.25-3.12.1',
			'mozilla-nspr-32bit': '4.25-3.12.1',
			'mozilla-nspr-32bit-debuginfo': '4.25-3.12.1',
			'mozilla-nspr-debuginfo': '4.25-3.12.1',
			'mozilla-nspr-debugsource': '4.25-3.12.1',
			'mozilla-nspr-devel': '4.25-3.12.1',
			'mozilla-nss': '3.53-3.40.1',
			'mozilla-nss-32bit': '3.53-3.40.1',
			'mozilla-nss-32bit-debuginfo': '3.53-3.40.1',
			'mozilla-nss-certs': '3.53-3.40.1',
			'mozilla-nss-certs-32bit': '3.53-3.40.1',
			'mozilla-nss-certs-32bit-debuginfo': '3.53-3.40.1',
			'mozilla-nss-certs-debuginfo': '3.53-3.40.1',
			'mozilla-nss-debuginfo': '3.53-3.40.1',
			'mozilla-nss-debugsource': '3.53-3.40.1',
			'mozilla-nss-devel': '3.53-3.40.1',
			'mozilla-nss-sysinit': '3.53-3.40.1',
			'mozilla-nss-sysinit-debuginfo': '3.53-3.40.1',
			'mozilla-nss-tools': '3.53-3.40.1',
			'mozilla-nss-tools-debuginfo': '3.53-3.40.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

