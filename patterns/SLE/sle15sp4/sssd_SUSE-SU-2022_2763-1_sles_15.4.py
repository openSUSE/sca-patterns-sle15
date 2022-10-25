#!/usr/bin/python3
#
# Title:       Moderate Security Announcement for sssd SUSE-SU-2022:2763-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP4
# URL:         https://lists.suse.com/pipermail/sle-security-updates/2022-August/011887.html
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
META_COMPONENT = "sssd"
pattern_filename = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-August/011887.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, pattern_filename, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'sssd'
MAIN = ''
SEVERITY = 'Moderate'
TAG = 'SUSE-SU-2022:2763-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'libipa_hbac-devel': '2.5.2-150400.4.5.14',
			'libipa_hbac0': '2.5.2-150400.4.5.14',
			'libipa_hbac0-debuginfo': '2.5.2-150400.4.5.14',
			'libsss_certmap-devel': '2.5.2-150400.4.5.14',
			'libsss_certmap0': '2.5.2-150400.4.5.14',
			'libsss_certmap0-debuginfo': '2.5.2-150400.4.5.14',
			'libsss_idmap-devel': '2.5.2-150400.4.5.14',
			'libsss_idmap0': '2.5.2-150400.4.5.14',
			'libsss_idmap0-debuginfo': '2.5.2-150400.4.5.14',
			'libsss_nss_idmap-devel': '2.5.2-150400.4.5.14',
			'libsss_nss_idmap0': '2.5.2-150400.4.5.14',
			'libsss_nss_idmap0-debuginfo': '2.5.2-150400.4.5.14',
			'libsss_simpleifp-devel': '2.5.2-150400.4.5.14',
			'libsss_simpleifp0': '2.5.2-150400.4.5.14',
			'libsss_simpleifp0-debuginfo': '2.5.2-150400.4.5.14',
			'python3-sssd-config': '2.5.2-150400.4.5.14',
			'python3-sssd-config-debuginfo': '2.5.2-150400.4.5.14',
			'sssd': '2.5.2-150400.4.5.14',
			'sssd-ad': '2.5.2-150400.4.5.14',
			'sssd-ad-debuginfo': '2.5.2-150400.4.5.14',
			'sssd-common': '2.5.2-150400.4.5.14',
			'sssd-common-debuginfo': '2.5.2-150400.4.5.14',
			'sssd-dbus': '2.5.2-150400.4.5.14',
			'sssd-dbus-debuginfo': '2.5.2-150400.4.5.14',
			'sssd-debugsource': '2.5.2-150400.4.5.14',
			'sssd-ipa': '2.5.2-150400.4.5.14',
			'sssd-ipa-debuginfo': '2.5.2-150400.4.5.14',
			'sssd-kcm': '2.5.2-150400.4.5.14',
			'sssd-kcm-debuginfo': '2.5.2-150400.4.5.14',
			'sssd-krb5': '2.5.2-150400.4.5.14',
			'sssd-krb5-common': '2.5.2-150400.4.5.14',
			'sssd-krb5-common-debuginfo': '2.5.2-150400.4.5.14',
			'sssd-krb5-debuginfo': '2.5.2-150400.4.5.14',
			'sssd-ldap': '2.5.2-150400.4.5.14',
			'sssd-ldap-debuginfo': '2.5.2-150400.4.5.14',
			'sssd-proxy': '2.5.2-150400.4.5.14',
			'sssd-proxy-debuginfo': '2.5.2-150400.4.5.14',
			'sssd-tools': '2.5.2-150400.4.5.14',
			'sssd-tools-debuginfo': '2.5.2-150400.4.5.14',
			'sssd-winbind-idmap': '2.5.2-150400.4.5.14',
			'sssd-winbind-idmap-debuginfo': '2.5.2-150400.4.5.14',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

