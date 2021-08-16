#!/usr/bin/python
#
# Title:       Pattern for TID000020252
# Description: vsftpd and other processes terminated due to OOM scenario
# Source:      Basic Python Pattern Template v0.3.4
# Options:     SLE,vsftpd,Memory,oomvsftpd,000020252,1182905,2,0,1
# Modified:    2021 Aug 16
#
##############################################################################
# Copyright (C) 2021 SUSE LLC
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

import re
import os
import Core
import SUSE

META_CLASS = "SLE"
META_CATEGORY = "vsftpd"
META_COMPONENT = "Memory"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020252|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1182905"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def wordAroundApplied():
	fileOpen = "etc.txt"
	section = "vsftpd.conf"
	content = []
	CONFIRMED = re.compile("isolate_network=NO", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	return False

def instancesExceeded():
	LIMIT = 25
	INST_COUNT = 0
	fileOpen = "systemd.txt"
	section = "systemd-cgls --no-pager --all --full"
	content = []
	CONFIRMED = re.compile("vsftpd .*vsftpd.conf", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					INST_COUNT += 1

	if( INST_COUNT > LIMIT ):
		return True
	else:
		return False

def vsftpdOOMFound():
	fileOpen = "boot.txt"
	section = "dmesg -T"
	content = []
	CONFIRMED = re.compile("vsftpd invoked oom-killer", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

AFFECTED_KERNEL = '5.3'
SERVICE_NAME = 'vsftpd.service'
SERVICE_INFO = SUSE.getServiceDInfo(SERVICE_NAME)
if( SERVICE_INFO ):
	if( SERVICE_INFO['UnitFileState'] == 'enabled' ):
		INSTALLED_VERSION = SUSE.compareKernel(AFFECTED_KERNEL)
		if( INSTALLED_VERSION >= 0 ):
			if( wordAroundApplied() ):
				Core.updateStatus(Core.IGNORE, "OOM workaround applied for " + str(SERVICE_NAME))
			else:
				if( vsftpdOOMFound() ):
					Core.updateStatus(Core.CRIT, "The vsftpd service invoked oom-killer, update configuration file")
				else:
					if( instancesExceeded() ):
						Core.updateStatus(Core.WARN, "The vsftpd service may invoke the oom-killer, consider an unisolated network configuration")
					else:
						Core.updateStatus(Core.IGNORE, "vsftpd instances within limits")
		else:
			Core.updateStatus(Core.ERROR, "ERROR: Outside the kernel version scope")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: Service is disabled: " + str(SERVICE_NAME))
else:
	Core.updateStatus(Core.ERROR, "Service details not found: " + str(SERVICE_NAME))

Core.printPatternResults()

