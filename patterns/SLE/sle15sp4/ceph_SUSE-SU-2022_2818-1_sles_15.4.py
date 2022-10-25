#!/usr/bin/python3
#
# Title:       Important Security Announcement for ceph SUSE-SU-2022:2818-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP4
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-August/011918.html
# Source:      Security Announcement Generator (sagen.py) v2.0.0-beta4
# Modified:    2022 Oct 25
#
##############################################################################
# Copyright (C) 2022 SUSE LLC
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
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-August/011918.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'ceph'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:2818-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'ceph-common': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'ceph-common-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'ceph-debugsource': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'libcephfs-devel': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'libcephfs2': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'libcephfs2-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'librados-devel': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'librados-devel-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'librados2': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'librados2-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'libradospp-devel': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'librbd-devel': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'librbd1': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'librbd1-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'librgw-devel': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'librgw2': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'librgw2-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'python3-ceph-argparse': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'python3-ceph-common': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'python3-cephfs': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'python3-cephfs-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'python3-rados': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'python3-rados-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'python3-rbd': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'python3-rbd-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'python3-rgw': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'python3-rgw-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'rados-objclass-devel': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'rbd-nbd': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
			'rbd-nbd-debuginfo': '16.2.9.536+g41a9f9a5573-150400.3.3.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

