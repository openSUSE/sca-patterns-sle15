#!/usr/bin/python3
#
# Title:       Pattern for TID000019889
# Description: System with FCoE connected devices fails to boot randomly due to wicked ordering cycle problems
# Source:      Package Version Pattern Template v0.3.8
# Options:     SLE,FCoE,Boot,fcoe,000019889,1176140,yast2-storage-ng,4.2.115-3.17,0,1
# Distro:      SLES15 SP2
# Modified:    2021 Apr 23
#
##############################################################################
# Copyright (C) 2021, SUSE LLC
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
META_CATEGORY = "FCoE"
META_COMPONENT = "Boot"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019889|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1176140"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def netDev():
	fileOpen = "fs-diskio.txt"
	section = "/etc/fstab"
	content = []
	CONFIRMED = re.compile("_netdev", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				return True
	return False

def wickedError():
	fileOpen = "boot.txt"
	section = "journalctl.*--boot"
	content = []
	CONFIRMED = re.compile("wickedd-nanny.*Interface.getManagedObjects failed", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'yast2-storage-ng'
RPM_VERSION_FIXED = '4.2.115-3.17'

if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION_FIXED)
	if( INSTALLED_VERSION >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME)
	else:
		if( netDev() ):
			if( wickedError() ):
				Core.updateStatus(Core.CRIT, "FCoE connected devices will cause boot irregularities, update system for fixes")
			else:
				Core.updateStatus(Core.WARN, "FCoE connected devices may cause boot irregularities, update system for fixes")
		else:
			Core.updateStatus(Core.ERROR, "ERROR: No _netdev devices found")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")

Core.printPatternResults()

