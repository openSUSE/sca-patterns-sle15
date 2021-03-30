#!/usr/bin/python

# Title:       No System Log Service
# Description: no syslog service after upgrade from SLES 11 SP4 to SLES 15
# Modified:    2021 Mar 27
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

##############################################################################
# Module Definition
##############################################################################

import os
import re
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Services"
META_COMPONENT = "syslog"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019710|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1158912"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def upgraded():
	fileOpen = "y2log.txt"
	section = "y2start.log"
	content = []
	UPGRADE = re.compile("Upgrade.*1", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if UPGRADE.search(line):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################
PACKAGE_SYSLOG = 'rsyslog'

if( SUSE.packageInstalled(PACKAGE_SYSLOG) ):
	Core.updateStatus(Core.IGNORE, "The " + PACKAGE_SYSLOG + " package is installed")
else:
	if( upgraded() ):
		Core.updateStatus(Core.CRIT, "The rsyslog package was not installed after upgrade, system logging is disabled")
	else:
		Core.updateStatus(Core.WARN, "The rsyslog package is missing, system logging is disabled")

Core.printPatternResults()