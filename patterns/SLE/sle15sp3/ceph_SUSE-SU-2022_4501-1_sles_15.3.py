#!/usr/bin/python3
#
# Title:       Important Security Announcement for ceph SUSE-SU-2022:4501-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-December/013249.html
# Source:      Security Announcement Generator (sagen.py) v2.0.6
# Modified:    2023 Jun 13
#
##############################################################################
# Copyright (C) 2023 SUSE LLC
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

meta_class = "Security"
meta_category = "SLE"
meta_component = "ceph"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-December/013249.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = False
	name = 'ceph'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2022:4501-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 3 ):
			packages = {
				'ceph-common': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'ceph-common-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'ceph-debugsource': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'fmt-debugsource': '8.0.1-150300.7.5.1',
				'libcephfs-devel': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'libcephfs2': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'libcephfs2-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'libfmt8': '8.0.1-150300.7.5.1',
				'libfmt8-debuginfo': '8.0.1-150300.7.5.1',
				'librados-devel': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'librados-devel-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'librados2': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'librados2-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'libradospp-devel': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'librbd-devel': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'librbd1': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'librbd1-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'librgw-devel': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'librgw2': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'librgw2-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'python3-ceph-argparse': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'python3-ceph-common': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'python3-cephfs': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'python3-cephfs-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'python3-rados': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'python3-rados-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'python3-rbd': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'python3-rbd-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'python3-rgw': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'python3-rgw-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'rados-objclass-devel': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'rbd-nbd': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
				'rbd-nbd-debuginfo': '16.2.9.536+g41a9f9a5573-150300.6.3.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

