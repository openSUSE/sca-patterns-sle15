#!/usr/bin/python3
#
# Title:       Important Security Announcement for samba SUSE-SU-2023:1683-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP1 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2023-March/014234.html
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
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2023-March/014234.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = True
	name = 'samba'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2023:1683-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 1 ):
			packages = {
				'libdcerpc-binding0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libdcerpc-binding0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libdcerpc0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libdcerpc0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libndr-krb5pac0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libndr-krb5pac0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libndr-nbt0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libndr-nbt0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libndr-standard0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libndr-standard0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libndr0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libndr0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libnetapi0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libnetapi0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamba-credentials0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamba-credentials0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamba-errors0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamba-errors0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamba-hostconfig0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamba-hostconfig0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamba-passdb0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamba-passdb0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamba-util0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamba-util0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamdb0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsamdb0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsmbconf0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsmbconf0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsmbldap2-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libsmbldap2-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libtevent-util0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libtevent-util0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libwbclient0-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'libwbclient0-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'samba-libs-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'samba-libs-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'samba-winbind-32bit': '4.9.5+git.554.abee30cf06-150100.3.77.1',
				'samba-winbind-32bit-debuginfo': '4.9.5+git.554.abee30cf06-150100.3.77.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

