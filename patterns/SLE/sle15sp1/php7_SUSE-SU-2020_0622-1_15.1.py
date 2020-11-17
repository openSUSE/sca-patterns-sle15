#!/usr/bin/python
#
# Title:       Important Security Announcement for php7 SUSE-SU-2020:0622-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP1
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
META_COMPONENT = "php7"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-March/006589.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'php7'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:0622-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'apache2-mod_php7': '7.2.5-4.52.4',
			'apache2-mod_php7-debuginfo': '7.2.5-4.52.4',
			'php7': '7.2.5-4.52.4',
			'php7-bcmath': '7.2.5-4.52.4',
			'php7-bcmath-debuginfo': '7.2.5-4.52.4',
			'php7-bz2': '7.2.5-4.52.4',
			'php7-bz2-debuginfo': '7.2.5-4.52.4',
			'php7-calendar': '7.2.5-4.52.4',
			'php7-calendar-debuginfo': '7.2.5-4.52.4',
			'php7-ctype': '7.2.5-4.52.4',
			'php7-ctype-debuginfo': '7.2.5-4.52.4',
			'php7-curl': '7.2.5-4.52.4',
			'php7-curl-debuginfo': '7.2.5-4.52.4',
			'php7-dba': '7.2.5-4.52.4',
			'php7-dba-debuginfo': '7.2.5-4.52.4',
			'php7-debuginfo': '7.2.5-4.52.4',
			'php7-debugsource': '7.2.5-4.52.4',
			'php7-devel': '7.2.5-4.52.4',
			'php7-dom': '7.2.5-4.52.4',
			'php7-dom-debuginfo': '7.2.5-4.52.4',
			'php7-embed': '7.2.5-4.52.4',
			'php7-embed-debuginfo': '7.2.5-4.52.4',
			'php7-enchant': '7.2.5-4.52.4',
			'php7-enchant-debuginfo': '7.2.5-4.52.4',
			'php7-exif': '7.2.5-4.52.4',
			'php7-exif-debuginfo': '7.2.5-4.52.4',
			'php7-fastcgi': '7.2.5-4.52.4',
			'php7-fastcgi-debuginfo': '7.2.5-4.52.4',
			'php7-fileinfo': '7.2.5-4.52.4',
			'php7-fileinfo-debuginfo': '7.2.5-4.52.4',
			'php7-fpm': '7.2.5-4.52.4',
			'php7-fpm-debuginfo': '7.2.5-4.52.4',
			'php7-ftp': '7.2.5-4.52.4',
			'php7-ftp-debuginfo': '7.2.5-4.52.4',
			'php7-gd': '7.2.5-4.52.4',
			'php7-gd-debuginfo': '7.2.5-4.52.4',
			'php7-gettext': '7.2.5-4.52.4',
			'php7-gettext-debuginfo': '7.2.5-4.52.4',
			'php7-gmp': '7.2.5-4.52.4',
			'php7-gmp-debuginfo': '7.2.5-4.52.4',
			'php7-iconv': '7.2.5-4.52.4',
			'php7-iconv-debuginfo': '7.2.5-4.52.4',
			'php7-intl': '7.2.5-4.52.4',
			'php7-intl-debuginfo': '7.2.5-4.52.4',
			'php7-json': '7.2.5-4.52.4',
			'php7-json-debuginfo': '7.2.5-4.52.4',
			'php7-ldap': '7.2.5-4.52.4',
			'php7-ldap-debuginfo': '7.2.5-4.52.4',
			'php7-mbstring': '7.2.5-4.52.4',
			'php7-mbstring-debuginfo': '7.2.5-4.52.4',
			'php7-mysql': '7.2.5-4.52.4',
			'php7-mysql-debuginfo': '7.2.5-4.52.4',
			'php7-odbc': '7.2.5-4.52.4',
			'php7-odbc-debuginfo': '7.2.5-4.52.4',
			'php7-opcache': '7.2.5-4.52.4',
			'php7-opcache-debuginfo': '7.2.5-4.52.4',
			'php7-openssl': '7.2.5-4.52.4',
			'php7-openssl-debuginfo': '7.2.5-4.52.4',
			'php7-pcntl': '7.2.5-4.52.4',
			'php7-pcntl-debuginfo': '7.2.5-4.52.4',
			'php7-pdo': '7.2.5-4.52.4',
			'php7-pdo-debuginfo': '7.2.5-4.52.4',
			'php7-pear': '7.2.5-4.52.4',
			'php7-pear-Archive_Tar': '7.2.5-4.52.4',
			'php7-pgsql': '7.2.5-4.52.4',
			'php7-pgsql-debuginfo': '7.2.5-4.52.4',
			'php7-phar': '7.2.5-4.52.4',
			'php7-phar-debuginfo': '7.2.5-4.52.4',
			'php7-posix': '7.2.5-4.52.4',
			'php7-posix-debuginfo': '7.2.5-4.52.4',
			'php7-readline': '7.2.5-4.52.4',
			'php7-readline-debuginfo': '7.2.5-4.52.4',
			'php7-shmop': '7.2.5-4.52.4',
			'php7-shmop-debuginfo': '7.2.5-4.52.4',
			'php7-snmp': '7.2.5-4.52.4',
			'php7-snmp-debuginfo': '7.2.5-4.52.4',
			'php7-soap': '7.2.5-4.52.4',
			'php7-soap-debuginfo': '7.2.5-4.52.4',
			'php7-sockets': '7.2.5-4.52.4',
			'php7-sockets-debuginfo': '7.2.5-4.52.4',
			'php7-sodium': '7.2.5-4.52.4',
			'php7-sodium-debuginfo': '7.2.5-4.52.4',
			'php7-sqlite': '7.2.5-4.52.4',
			'php7-sqlite-debuginfo': '7.2.5-4.52.4',
			'php7-sysvmsg': '7.2.5-4.52.4',
			'php7-sysvmsg-debuginfo': '7.2.5-4.52.4',
			'php7-sysvsem': '7.2.5-4.52.4',
			'php7-sysvsem-debuginfo': '7.2.5-4.52.4',
			'php7-sysvshm': '7.2.5-4.52.4',
			'php7-sysvshm-debuginfo': '7.2.5-4.52.4',
			'php7-tidy': '7.2.5-4.52.4',
			'php7-tidy-debuginfo': '7.2.5-4.52.4',
			'php7-tokenizer': '7.2.5-4.52.4',
			'php7-tokenizer-debuginfo': '7.2.5-4.52.4',
			'php7-wddx': '7.2.5-4.52.4',
			'php7-wddx-debuginfo': '7.2.5-4.52.4',
			'php7-xmlreader': '7.2.5-4.52.4',
			'php7-xmlreader-debuginfo': '7.2.5-4.52.4',
			'php7-xmlrpc': '7.2.5-4.52.4',
			'php7-xmlrpc-debuginfo': '7.2.5-4.52.4',
			'php7-xmlwriter': '7.2.5-4.52.4',
			'php7-xmlwriter-debuginfo': '7.2.5-4.52.4',
			'php7-xsl': '7.2.5-4.52.4',
			'php7-xsl-debuginfo': '7.2.5-4.52.4',
			'php7-zip': '7.2.5-4.52.4',
			'php7-zip-debuginfo': '7.2.5-4.52.4',
			'php7-zlib': '7.2.5-4.52.4',
			'php7-zlib-debuginfo': '7.2.5-4.52.4',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

