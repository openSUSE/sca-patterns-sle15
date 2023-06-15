#!/usr/bin/python3
#
# Title:       Important Security Announcement for cyrus-sasl SUSE-SU-2022:3549-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0 LTSS
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-October/012519.html
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
meta_component = "cyrus-sasl"
pattern_filename = os.path.basename(__file__)
primary_link = "META_LINK_Security"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-October/012519.html"
Core.init(meta_class, meta_category, meta_component, pattern_filename, primary_link, overall, overall_info, other_links)

def main():
	ltss = True
	name = 'cyrus-sasl'
	main = ''
	severity = 'Important'
	tag = 'SUSE-SU-2022:3549-1'
	packages = {}
	server = SUSE.getHostInfo()

	if ( server['DistroVersion'] == 15):
		if ( server['DistroPatchLevel'] == 0 ):
			packages = {
				'cyrus-sasl': '2.1.26-150000.5.13.1',
				'cyrus-sasl-crammd5': '2.1.26-150000.5.13.1',
				'cyrus-sasl-crammd5-debuginfo': '2.1.26-150000.5.13.1',
				'cyrus-sasl-debuginfo': '2.1.26-150000.5.13.1',
				'cyrus-sasl-debugsource': '2.1.26-150000.5.13.1',
				'cyrus-sasl-devel': '2.1.26-150000.5.13.1',
				'cyrus-sasl-digestmd5': '2.1.26-150000.5.13.1',
				'cyrus-sasl-digestmd5-debuginfo': '2.1.26-150000.5.13.1',
				'cyrus-sasl-gssapi': '2.1.26-150000.5.13.1',
				'cyrus-sasl-gssapi-debuginfo': '2.1.26-150000.5.13.1',
				'cyrus-sasl-otp': '2.1.26-150000.5.13.1',
				'cyrus-sasl-otp-debuginfo': '2.1.26-150000.5.13.1',
				'cyrus-sasl-plain': '2.1.26-150000.5.13.1',
				'cyrus-sasl-plain-debuginfo': '2.1.26-150000.5.13.1',
				'cyrus-sasl-saslauthd': '2.1.26-150000.5.13.1',
				'cyrus-sasl-saslauthd-debuginfo': '2.1.26-150000.5.13.1',
				'cyrus-sasl-saslauthd-debugsource': '2.1.26-150000.5.13.1',
				'cyrus-sasl-sqlauxprop': '2.1.26-150000.5.13.1',
				'cyrus-sasl-sqlauxprop-debuginfo': '2.1.26-150000.5.13.1',
				'libsasl2-3': '2.1.26-150000.5.13.1',
				'libsasl2-3-debuginfo': '2.1.26-150000.5.13.1',
			}
			SUSE.securityAnnouncementPackageCheck(name, main, ltss, severity, tag, packages)
		else:
			Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the service pack scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + name + " Security Announcement: Outside the distribution scope")

	Core.printPatternResults()

if __name__ == "__main__":
	main()

