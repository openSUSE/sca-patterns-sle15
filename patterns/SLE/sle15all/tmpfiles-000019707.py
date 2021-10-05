#!/usr/bin/python3
#
# Title:       Pattern for TID000019707
# Description: systemd-tmpfiles-setup.service failed after upgrade from SLES 11 SP4 to SLES 15
# Source:      Package Version Pattern Template v0.3.1
# Options:     SLE,Services,TmpFiles,tmpfiles,000019707,1158911,2,0,0
# Modified:    2021 Mar 31
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

META_CLASS = "SLE"
META_CATEGORY = "Services"
META_COMPONENT = "TmpFiles"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019707|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1158911"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

SERVICE = 'systemd-tmpfiles-setup.service'
##############################################################################
# Local Function Definitions
##############################################################################

def serviceFailed():
	global SERVICE

	fileOpen = "systemd.txt"
	section = "/systemctl --failed"
	content = []
	CONFIRMED = re.compile(SERVICE, re.IGNORECASE)
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

if( serviceFailed() ):
	if( upgraded() ):
		Core.updateStatus(Core.CRIT, str(SERVICE) + " has failed, run systemd-sysuser")
	else:
		Core.updateStatus(Core.WARN, str(SERVICE) + " has failed, consider running systemd-sysuser")
else:
	Core.updateStatus(Core.ERROR, "The " + str(SERVICE) + " did not fail")

Core.printPatternResults()

