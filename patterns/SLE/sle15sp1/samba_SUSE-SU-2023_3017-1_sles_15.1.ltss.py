#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for samba SUSE-SU-2023:3017-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP1 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2023-July/015694.html
# Source:      Security Announcement Generator (sagen.py) v2.0.13
# Modified:    2023 Aug 31
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
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2023-July/015694.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = True
	name = 'samba'
	main = ''
	severity = 'Moderate'
	tag = 'SUSE-SU-2023:3017-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 1 ):
			packages = {
				'libdcerpc-binding0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libdcerpc-binding0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libdcerpc0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libdcerpc0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libndr-krb5pac0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libndr-krb5pac0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libndr-nbt0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libndr-nbt0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libndr-standard0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libndr-standard0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libndr0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libndr0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libnetapi0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libnetapi0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamba-credentials0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamba-credentials0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamba-errors0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamba-errors0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamba-hostconfig0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamba-hostconfig0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamba-passdb0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamba-passdb0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamba-util0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamba-util0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamdb0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsamdb0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsmbconf0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsmbconf0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsmbldap2-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libsmbldap2-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libtevent-util0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libtevent-util0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libwbclient0-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'libwbclient0-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'samba-libs-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'samba-libs-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'samba-winbind-32bit': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
				'samba-winbind-32bit-debuginfo': '4.9.5+git.564.996810ca1e3-150100.3.82.3',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

