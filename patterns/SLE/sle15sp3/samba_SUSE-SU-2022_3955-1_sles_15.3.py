#!/usr/bin/python3
#
# Title:       Important Security Announcement for samba SUSE-SU-2022:3955-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-November/012905.html
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
meta_component = "samba"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-November/012905.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = False
	name = 'samba'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2022:3955-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 3 ):
			packages = {
				'libsamba-policy-devel': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'libsamba-policy-python3-devel': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'libsamba-policy0-python3': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'libsamba-policy0-python3-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-ad-dc-libs': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-ad-dc-libs-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-client': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-client-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-client-libs': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-client-libs-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-debugsource': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-devel': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-dsdb-modules': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-dsdb-modules-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-gpupdate': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-ldb-ldap': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-ldb-ldap-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-libs': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-libs-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-libs-python3': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-libs-python3-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-python3': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-python3-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-tool': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-winbind': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-winbind-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-winbind-libs': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
				'samba-winbind-libs-debuginfo': '4.15.8+git.527.8d0c05d313e-150300.3.40.2',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

