#!/usr/bin/python
#
# Title:       Important Security Announcement for kgraft-patch SUSE-SU-2020:0868-1
# Description: Security fixes for SUSE Linux Kernel Live Patch 15 SP1
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
META_COMPONENT = "kgraft-patch"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-April/006672.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kgraft-patch'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:0868-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'kernel-livepatch-4_12_14-195-default': '10-28.2',
			'kernel-livepatch-4_12_14-197_10-default': '6-2.1',
			'kernel-livepatch-4_12_14-197_15-default': '6-2.1',
			'kernel-livepatch-4_12_14-197_18-default': '5-2.1',
			'kernel-livepatch-4_12_14-197_21-default': '5-2.1',
			'kernel-livepatch-4_12_14-197_26-default': '3-2.1',
			'kernel-livepatch-4_12_14-197_29-default': '3-2.1',
			'kernel-livepatch-4_12_14-197_4-default': '9-2.1',
			'kernel-livepatch-4_12_14-197_7-default': '8-2.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

