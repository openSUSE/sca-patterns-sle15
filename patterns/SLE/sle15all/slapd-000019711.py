#!/usr/bin/python3
#
# Title:       Pattern for TID000019711
# Description: slapd.service not enabled/failed after upgrade from SLES 11 SP4 to SLES 15
# Source:      Package Version Pattern Template v0.3.1
# Options:     SLE,Services,LDAP,slapd,000019711,0,2,1,1
# Modified:    2021 Apr 05
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
META_CATEGORY = "Services"
META_COMPONENT = "LDAP"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019711"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def configChange():
	fileOpen = "y2log.txt"
	section = "YaST2/config_diff.*log"
	content = []
	CONFIRMED = re.compile("Changed configuration file.*for openldap2-[0-9]", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	return False

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

PACKAGE = "openldap2"
SERVICE_NAME = 'slapd.service'
SERVICE_INFO = SUSE.getServiceDInfo(SERVICE_NAME)

if( SUSE.packageInstalled(PACKAGE) ):
	if( SERVICE_INFO['UnitFileState'] == 'enabled' ):
		if( SERVICE_INFO['SubState'] == 'running' ):
			Core.updateStatus(Core.IGNORE, "Service enabled and running: " + str(SERVICE_NAME))
		else:
			if( configChange() ):
				if( upgraded() ):
					Core.updateStatus(Core.WARN, "The " + SERVICE_NAME + " is not enabled or running after upgrade, confirm it's status")
				else:
					Core.updateStatus(Core.WARN, "If you use " + SERVICE_NAME + ", confirm it's status")
			else:
				Core.updateStatus(Core.ERROR, "No configuration change found")
	else:
		if( configChange() ):
			if( upgraded() ):
				Core.updateStatus(Core.CRIT, "The " + SERVICE_NAME + " is not enabled or running after upgrade, confirm it's status")
			else:
				Core.updateStatus(Core.WARN, "If you use " + SERVICE_NAME + ", confirm it's status")
		else:
			Core.updateStatus(Core.ERROR, "No configuration change found")
else:
	Core.updateStatus(Core.ERROR, "ERROR: RPM package " + PACKAGE + " not installed")

Core.printPatternResults()

