#!/usr/bin/python3
#
# Title:       Important Security Announcement for samba SUSE-SU-2022:0283-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP3
# Source:      Security Announcement Parser v1.6.4
# Modified:    2022 May 06
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
META_COMPONENT = "samba"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2022-February/010164.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'samba'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2022:0283-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'apparmor-abstractions': '2.13.6-150300.3.11.2',
			'apparmor-debugsource': '2.13.6-150300.3.11.2',
			'apparmor-docs': '2.13.6-150300.3.11.2',
			'apparmor-parser': '2.13.6-150300.3.11.2',
			'apparmor-parser-debuginfo': '2.13.6-150300.3.11.2',
			'apparmor-parser-lang': '2.13.6-150300.3.11.2',
			'apparmor-profiles': '2.13.6-150300.3.11.2',
			'apparmor-utils': '2.13.6-150300.3.11.2',
			'apparmor-utils-lang': '2.13.6-150300.3.11.2',
			'krb5': '1.19.2-150300.8.3.2',
			'krb5-32bit': '1.19.2-150300.8.3.2',
			'krb5-32bit-debuginfo': '1.19.2-150300.8.3.2',
			'krb5-client': '1.19.2-150300.8.3.2',
			'krb5-client-debuginfo': '1.19.2-150300.8.3.2',
			'krb5-debuginfo': '1.19.2-150300.8.3.2',
			'krb5-debugsource': '1.19.2-150300.8.3.2',
			'krb5-devel': '1.19.2-150300.8.3.2',
			'krb5-plugin-preauth-otp': '1.19.2-150300.8.3.2',
			'krb5-plugin-preauth-otp-debuginfo': '1.19.2-150300.8.3.2',
			'krb5-plugin-preauth-pkinit': '1.19.2-150300.8.3.2',
			'krb5-plugin-preauth-pkinit-debuginfo': '1.19.2-150300.8.3.2',
			'krb5-plugin-preauth-spake': '1.19.2-150300.8.3.2',
			'krb5-plugin-preauth-spake-debuginfo': '1.19.2-150300.8.3.2',
			'ldb-debugsource': '2.4.1-150300.3.10.1',
			'ldb-tools': '2.4.1-150300.3.10.1',
			'ldb-tools-debuginfo': '2.4.1-150300.3.10.1',
			'libapparmor-debugsource': '2.13.6-150300.3.11.1',
			'libapparmor-devel': '2.13.6-150300.3.11.1',
			'libapparmor1': '2.13.6-150300.3.11.1',
			'libapparmor1-32bit': '2.13.6-150300.3.11.1',
			'libapparmor1-32bit-debuginfo': '2.13.6-150300.3.11.1',
			'libapparmor1-debuginfo': '2.13.6-150300.3.11.1',
			'libipa_hbac-devel': '1.16.1-150300.23.17.3',
			'libipa_hbac0': '1.16.1-150300.23.17.3',
			'libipa_hbac0-debuginfo': '1.16.1-150300.23.17.3',
			'libldb-devel': '2.4.1-150300.3.10.1',
			'libldb2': '2.4.1-150300.3.10.1',
			'libldb2-32bit': '2.4.1-150300.3.10.1',
			'libldb2-32bit-debuginfo': '2.4.1-150300.3.10.1',
			'libldb2-debuginfo': '2.4.1-150300.3.10.1',
			'libsamba-policy-devel': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'libsamba-policy-python3-devel': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'libsamba-policy0-python3': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'libsamba-policy0-python3-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'libsss_certmap-devel': '1.16.1-150300.23.17.3',
			'libsss_certmap0': '1.16.1-150300.23.17.3',
			'libsss_certmap0-debuginfo': '1.16.1-150300.23.17.3',
			'libsss_idmap-devel': '1.16.1-150300.23.17.3',
			'libsss_idmap0': '1.16.1-150300.23.17.3',
			'libsss_idmap0-debuginfo': '1.16.1-150300.23.17.3',
			'libsss_nss_idmap-devel': '1.16.1-150300.23.17.3',
			'libsss_nss_idmap0': '1.16.1-150300.23.17.3',
			'libsss_nss_idmap0-debuginfo': '1.16.1-150300.23.17.3',
			'libsss_simpleifp-devel': '1.16.1-150300.23.17.3',
			'libsss_simpleifp0': '1.16.1-150300.23.17.3',
			'libsss_simpleifp0-debuginfo': '1.16.1-150300.23.17.3',
			'libtalloc-devel': '2.3.3-150300.3.3.2',
			'libtalloc2': '2.3.3-150300.3.3.2',
			'libtalloc2-32bit': '2.3.3-150300.3.3.2',
			'libtalloc2-32bit-debuginfo': '2.3.3-150300.3.3.2',
			'libtalloc2-debuginfo': '2.3.3-150300.3.3.2',
			'libtdb-devel': '1.4.4-150300.3.3.2',
			'libtdb1': '1.4.4-150300.3.3.2',
			'libtdb1-32bit': '1.4.4-150300.3.3.2',
			'libtdb1-32bit-debuginfo': '1.4.4-150300.3.3.2',
			'libtdb1-debuginfo': '1.4.4-150300.3.3.2',
			'libtevent-devel': '0.11.0-150300.3.3.2',
			'libtevent0': '0.11.0-150300.3.3.2',
			'libtevent0-32bit': '0.11.0-150300.3.3.2',
			'libtevent0-32bit-debuginfo': '0.11.0-150300.3.3.2',
			'libtevent0-debuginfo': '0.11.0-150300.3.3.2',
			'pam_apparmor': '2.13.6-150300.3.11.2',
			'pam_apparmor-32bit': '2.13.6-150300.3.11.2',
			'pam_apparmor-32bit-debuginfo': '2.13.6-150300.3.11.2',
			'pam_apparmor-debuginfo': '2.13.6-150300.3.11.2',
			'perl-apparmor': '2.13.6-150300.3.11.2',
			'perl-apparmor-debuginfo': '2.13.6-150300.3.11.2',
			'python3-apparmor': '2.13.6-150300.3.11.2',
			'python3-apparmor-debuginfo': '2.13.6-150300.3.11.2',
			'python3-ldb': '2.4.1-150300.3.10.1',
			'python3-ldb-debuginfo': '2.4.1-150300.3.10.1',
			'python3-ldb-devel': '2.4.1-150300.3.10.1',
			'python3-sssd-config': '1.16.1-150300.23.17.3',
			'python3-sssd-config-debuginfo': '1.16.1-150300.23.17.3',
			'python3-talloc': '2.3.3-150300.3.3.2',
			'python3-talloc-debuginfo': '2.3.3-150300.3.3.2',
			'python3-talloc-devel': '2.3.3-150300.3.3.2',
			'python3-tdb': '1.4.4-150300.3.3.2',
			'python3-tdb-debuginfo': '1.4.4-150300.3.3.2',
			'python3-tevent': '0.11.0-150300.3.3.2',
			'python3-tevent-debuginfo': '0.11.0-150300.3.3.2',
			'samba': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-ad-dc-libs': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-ad-dc-libs-32bit': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-ad-dc-libs-32bit-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-ad-dc-libs-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-ceph': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-ceph-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-client': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-client-32bit': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-client-32bit-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-client-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-client-libs': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-client-libs-32bit': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-client-libs-32bit-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-client-libs-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-debugsource': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-devel': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-devel-32bit': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-dsdb-modules': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-dsdb-modules-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-gpupdate': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-ldb-ldap': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-ldb-ldap-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-libs': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-libs-32bit': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-libs-32bit-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-libs-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-libs-python3': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-libs-python3-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-python3': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-python3-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-tool': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-winbind': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-winbind-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-winbind-libs': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-winbind-libs-32bit': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-winbind-libs-32bit-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'samba-winbind-libs-debuginfo': '4.15.4+git.324.8332acf1a63-150300.3.25.3',
			'sssd': '1.16.1-150300.23.17.3',
			'sssd-ad': '1.16.1-150300.23.17.3',
			'sssd-ad-debuginfo': '1.16.1-150300.23.17.3',
			'sssd-common': '1.16.1-150300.23.17.3',
			'sssd-common-debuginfo': '1.16.1-150300.23.17.3',
			'sssd-dbus': '1.16.1-150300.23.17.3',
			'sssd-dbus-debuginfo': '1.16.1-150300.23.17.3',
			'sssd-debugsource': '1.16.1-150300.23.17.3',
			'sssd-ipa': '1.16.1-150300.23.17.3',
			'sssd-ipa-debuginfo': '1.16.1-150300.23.17.3',
			'sssd-krb5': '1.16.1-150300.23.17.3',
			'sssd-krb5-common': '1.16.1-150300.23.17.3',
			'sssd-krb5-common-debuginfo': '1.16.1-150300.23.17.3',
			'sssd-krb5-debuginfo': '1.16.1-150300.23.17.3',
			'sssd-ldap': '1.16.1-150300.23.17.3',
			'sssd-ldap-debuginfo': '1.16.1-150300.23.17.3',
			'sssd-proxy': '1.16.1-150300.23.17.3',
			'sssd-proxy-debuginfo': '1.16.1-150300.23.17.3',
			'sssd-tools': '1.16.1-150300.23.17.3',
			'sssd-tools-debuginfo': '1.16.1-150300.23.17.3',
			'sssd-winbind-idmap': '1.16.1-150300.23.17.3',
			'sssd-winbind-idmap-debuginfo': '1.16.1-150300.23.17.3',
			'talloc-debugsource': '2.3.3-150300.3.3.2',
			'talloc-man': '2.3.3-150300.3.3.1',
			'tdb-debugsource': '1.4.4-150300.3.3.2',
			'tdb-tools': '1.4.4-150300.3.3.2',
			'tdb-tools-debuginfo': '1.4.4-150300.3.3.2',
			'tevent-debugsource': '0.11.0-150300.3.3.2',
			'tevent-man': '0.11.0-150300.3.3.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

