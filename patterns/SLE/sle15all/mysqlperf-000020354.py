#!/usr/bin/python3
#
# Title:       Pattern for TID000020354
# Description: mysqld segfault when the system is under stress
# Source:      Basic Python Pattern Template v0.3.4
# Options:     SLE,MySQL,Performance,mysqlperf,000020354,1186792,1,0,1
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
META_CATEGORY = "MySQL"
META_COMPONENT = "Performance"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020354|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1186792"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def segFaultFound():
	fileOpen = "boot.txt"
	section = "dmesg -T"
	content = []
	CONFIRMED = re.compile("mysqld.*segfault at.*ip.*sp.*error.*in mysqld", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

SERVICE_NAME = 'mariadb.service'
SERVICE_INFO = SUSE.getServiceDInfo(SERVICE_NAME)
if( SERVICE_INFO ):
	if( SERVICE_INFO['UnitFileState'] == 'enabled' ):
		if( segFaultFound() ):
			Core.updateStatus(Core.WARN, "Performance issues may be related to semaphore wait times")
		else:
			Core.updateStatus(Core.IGNORE, "No segfaults found")
	else:
		Core.updateStatus(Core.ERROR, "Service is disabled: " + str(SERVICE_NAME))
else:
	Core.updateStatus(Core.ERROR, "Service details not found: " + str(SERVICE_NAME))

Core.printPatternResults()

