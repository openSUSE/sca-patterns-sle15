#!/usr/bin/python
#
# Title:       Important Security Announcement for pcp SUSE-SU-2020:0357-1
# Description: Security fixes for SUSE Linux Enterprise 15 SP0
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
META_COMPONENT = "pcp"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.suse.com/pipermail/sle-security-updates/2020-February/006470.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'pcp'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2020:0357-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 15):
	if ( SERVER['DistroPatchLevel'] == 0 ):
		PACKAGES = {
			'libpcp-devel': '3.11.9-5.8.1',
			'libpcp3': '3.11.9-5.8.1',
			'libpcp3-debuginfo': '3.11.9-5.8.1',
			'libpcp_gui2': '3.11.9-5.8.1',
			'libpcp_gui2-debuginfo': '3.11.9-5.8.1',
			'libpcp_import1': '3.11.9-5.8.1',
			'libpcp_import1-debuginfo': '3.11.9-5.8.1',
			'libpcp_mmv1': '3.11.9-5.8.1',
			'libpcp_mmv1-debuginfo': '3.11.9-5.8.1',
			'libpcp_trace2': '3.11.9-5.8.1',
			'libpcp_trace2-debuginfo': '3.11.9-5.8.1',
			'libpcp_web1': '3.11.9-5.8.1',
			'libpcp_web1-debuginfo': '3.11.9-5.8.1',
			'pcp': '3.11.9-5.8.1',
			'pcp-conf': '3.11.9-5.8.1',
			'pcp-debuginfo': '3.11.9-5.8.1',
			'pcp-debugsource': '3.11.9-5.8.1',
			'pcp-devel': '3.11.9-5.8.1',
			'pcp-devel-debuginfo': '3.11.9-5.8.1',
			'pcp-doc': '3.11.9-5.8.1',
			'pcp-export-pcp2graphite': '3.11.9-5.8.1',
			'pcp-export-pcp2influxdb': '3.11.9-5.8.1',
			'pcp-export-zabbix-agent': '3.11.9-5.8.1',
			'pcp-export-zabbix-agent-debuginfo': '3.11.9-5.8.1',
			'pcp-gui': '3.11.9-5.8.1',
			'pcp-gui-debuginfo': '3.11.9-5.8.1',
			'pcp-import-collectl2pcp': '3.11.9-5.8.1',
			'pcp-import-collectl2pcp-debuginfo': '3.11.9-5.8.1',
			'pcp-import-ganglia2pcp': '3.11.9-5.8.1',
			'pcp-import-iostat2pcp': '3.11.9-5.8.1',
			'pcp-import-mrtg2pcp': '3.11.9-5.8.1',
			'pcp-import-sar2pcp': '3.11.9-5.8.1',
			'pcp-manager': '3.11.9-5.8.1',
			'pcp-manager-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-activemq': '3.11.9-5.8.1',
			'pcp-pmda-apache': '3.11.9-5.8.1',
			'pcp-pmda-apache-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-bash': '3.11.9-5.8.1',
			'pcp-pmda-bash-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-bind2': '3.11.9-5.8.1',
			'pcp-pmda-bonding': '3.11.9-5.8.1',
			'pcp-pmda-cifs': '3.11.9-5.8.1',
			'pcp-pmda-cifs-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-cisco': '3.11.9-5.8.1',
			'pcp-pmda-cisco-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-dbping': '3.11.9-5.8.1',
			'pcp-pmda-dm': '3.11.9-5.8.1',
			'pcp-pmda-dm-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-docker': '3.11.9-5.8.1',
			'pcp-pmda-docker-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-ds389': '3.11.9-5.8.1',
			'pcp-pmda-ds389log': '3.11.9-5.8.1',
			'pcp-pmda-elasticsearch': '3.11.9-5.8.1',
			'pcp-pmda-gfs2': '3.11.9-5.8.1',
			'pcp-pmda-gfs2-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-gluster': '3.11.9-5.8.1',
			'pcp-pmda-gpfs': '3.11.9-5.8.1',
			'pcp-pmda-gpsd': '3.11.9-5.8.1',
			'pcp-pmda-json': '3.11.9-5.8.1',
			'pcp-pmda-kvm': '3.11.9-5.8.1',
			'pcp-pmda-lmsensors': '3.11.9-5.8.1',
			'pcp-pmda-lmsensors-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-logger': '3.11.9-5.8.1',
			'pcp-pmda-logger-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-lustre': '3.11.9-5.8.1',
			'pcp-pmda-lustrecomm': '3.11.9-5.8.1',
			'pcp-pmda-lustrecomm-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-mailq': '3.11.9-5.8.1',
			'pcp-pmda-mailq-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-memcache': '3.11.9-5.8.1',
			'pcp-pmda-mic': '3.11.9-5.8.1',
			'pcp-pmda-mounts': '3.11.9-5.8.1',
			'pcp-pmda-mounts-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-mysql': '3.11.9-5.8.1',
			'pcp-pmda-named': '3.11.9-5.8.1',
			'pcp-pmda-netfilter': '3.11.9-5.8.1',
			'pcp-pmda-news': '3.11.9-5.8.1',
			'pcp-pmda-nfsclient': '3.11.9-5.8.1',
			'pcp-pmda-nginx': '3.11.9-5.8.1',
			'pcp-pmda-nutcracker': '3.11.9-5.8.1',
			'pcp-pmda-nvidia-gpu': '3.11.9-5.8.1',
			'pcp-pmda-nvidia-gpu-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-oracle': '3.11.9-5.8.1',
			'pcp-pmda-pdns': '3.11.9-5.8.1',
			'pcp-pmda-postfix': '3.11.9-5.8.1',
			'pcp-pmda-postgresql': '3.11.9-5.8.1',
			'pcp-pmda-redis': '3.11.9-5.8.1',
			'pcp-pmda-roomtemp': '3.11.9-5.8.1',
			'pcp-pmda-roomtemp-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-rpm': '3.11.9-5.8.1',
			'pcp-pmda-rpm-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-rsyslog': '3.11.9-5.8.1',
			'pcp-pmda-samba': '3.11.9-5.8.1',
			'pcp-pmda-sendmail': '3.11.9-5.8.1',
			'pcp-pmda-sendmail-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-shping': '3.11.9-5.8.1',
			'pcp-pmda-shping-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-slurm': '3.11.9-5.8.1',
			'pcp-pmda-snmp': '3.11.9-5.8.1',
			'pcp-pmda-summary': '3.11.9-5.8.1',
			'pcp-pmda-summary-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-systemd': '3.11.9-5.8.1',
			'pcp-pmda-systemd-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-trace': '3.11.9-5.8.1',
			'pcp-pmda-trace-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-unbound': '3.11.9-5.8.1',
			'pcp-pmda-vmware': '3.11.9-5.8.1',
			'pcp-pmda-weblog': '3.11.9-5.8.1',
			'pcp-pmda-weblog-debuginfo': '3.11.9-5.8.1',
			'pcp-pmda-zimbra': '3.11.9-5.8.1',
			'pcp-pmda-zswap': '3.11.9-5.8.1',
			'pcp-system-tools': '3.11.9-5.8.1',
			'pcp-system-tools-debuginfo': '3.11.9-5.8.1',
			'pcp-testsuite': '3.11.9-5.8.1',
			'pcp-testsuite-debuginfo': '3.11.9-5.8.1',
			'pcp-webapi': '3.11.9-5.8.1',
			'pcp-webapi-debuginfo': '3.11.9-5.8.1',
			'perl-PCP-LogImport': '3.11.9-5.8.1',
			'perl-PCP-LogImport-debuginfo': '3.11.9-5.8.1',
			'perl-PCP-LogSummary': '3.11.9-5.8.1',
			'perl-PCP-MMV': '3.11.9-5.8.1',
			'perl-PCP-MMV-debuginfo': '3.11.9-5.8.1',
			'perl-PCP-PMDA': '3.11.9-5.8.1',
			'perl-PCP-PMDA-debuginfo': '3.11.9-5.8.1',
			'python-pcp': '3.11.9-5.8.1',
			'python-pcp-debuginfo': '3.11.9-5.8.1',
			'python3-pcp': '3.11.9-5.8.1',
			'python3-pcp-debuginfo': '3.11.9-5.8.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

