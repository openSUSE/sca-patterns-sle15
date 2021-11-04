#!/usr/bin/python3
#
# Title:       Pattern for TID000019708
# Description: acpid.service failed to start after upgrade
# Source:      Package Version Pattern Template v0.3.1
# Options:     SLE,Services,acpid,acpid,000019708,1158890,1,1,0
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
META_COMPONENT = "acpid"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019708|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1158890"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

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

##############################################################################
# Main Program Execution
##############################################################################

PACKAGE = "acpid"
SERVICE = 'acpid.service'

if( SUSE.packageInstalled(PACKAGE) ):
	if( serviceFailed() ):
		Core.updateStatus(Core.WARN, "Please remove the " + PACKAGE + " package, the " + SERVICE + " has failed")
	else:
		Core.updateStatus(Core.WARN, "Please remove the depricated " + PACKAGE + " package")
else:
	Core.updateStatus(Core.ERROR, "ERROR: RPM package " + PACKAGE + " not installed")

Core.printPatternResults()

