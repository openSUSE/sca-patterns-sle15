#!/usr/bin/python3
#
# Title:       Important Security Announcement for ceph SUSE-SU-2021:1834-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3
# Source:      Security Announcement Parser v1.6.1
# Modified:    2021 Jul 02
#
##############################################################################
# Copyright (C) 2021 SUSE LLC
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
#   Jason Record <jason.record@suse.com>
#
##############################################################################

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "ceph"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2021-June/008915.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'ceph'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2021:1834-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'ceph-common': '15.2.12.83+g528da226523-3.25.1',
			'ceph-common-debuginfo': '15.2.12.83+g528da226523-3.25.1',
			'ceph-debugsource': '15.2.12.83+g528da226523-3.25.1',
			'libcephfs-devel': '15.2.12.83+g528da226523-3.25.1',
			'libcephfs2': '15.2.12.83+g528da226523-3.25.1',
			'libcephfs2-debuginfo': '15.2.12.83+g528da226523-3.25.1',
			'librados-devel': '15.2.12.83+g528da226523-3.25.1',
			'librados-devel-debuginfo': '15.2.12.83+g528da226523-3.25.1',
			'librados2': '15.2.12.83+g528da226523-3.25.1',
			'librados2-debuginfo': '15.2.12.83+g528da226523-3.25.1',
			'libradospp-devel': '15.2.12.83+g528da226523-3.25.1',
			'librbd-devel': '15.2.12.83+g528da226523-3.25.1',
			'librbd1': '15.2.12.83+g528da226523-3.25.1',
			'librbd1-debuginfo': '15.2.12.83+g528da226523-3.25.1',
			'librgw-devel': '15.2.12.83+g528da226523-3.25.1',
			'librgw2': '15.2.12.83+g528da226523-3.25.1',
			'librgw2-debuginfo': '15.2.12.83+g528da226523-3.25.1',
			'python3-ceph-argparse': '15.2.12.83+g528da226523-3.25.1',
			'python3-ceph-common': '15.2.12.83+g528da226523-3.25.1',
			'python3-cephfs': '15.2.12.83+g528da226523-3.25.1',
			'python3-cephfs-debuginfo': '15.2.12.83+g528da226523-3.25.1',
			'python3-rados': '15.2.12.83+g528da226523-3.25.1',
			'python3-rados-debuginfo': '15.2.12.83+g528da226523-3.25.1',
			'python3-rbd': '15.2.12.83+g528da226523-3.25.1',
			'python3-rbd-debuginfo': '15.2.12.83+g528da226523-3.25.1',
			'python3-rgw': '15.2.12.83+g528da226523-3.25.1',
			'python3-rgw-debuginfo': '15.2.12.83+g528da226523-3.25.1',
			'rados-objclass-devel': '15.2.12.83+g528da226523-3.25.1',
			'rbd-nbd': '15.2.12.83+g528da226523-3.25.1',
			'rbd-nbd-debuginfo': '15.2.12.83+g528da226523-3.25.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

