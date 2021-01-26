#!/usr/bin/python

# Title:       Graphic Interface Failure
# Description: Graphic interface no longer working after patches
# Modified:    2021 Jan 26
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

import re
import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "X"
META_COMPONENT = "Schema"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019825"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

PACKAGE_NAME = 'gsettings-desktop-schemas'

##############################################################################
# Local Function Definitions
##############################################################################

def errorFound():
	fileOpen = "messages.txt"
	section = "/var/log/messages"
	content = {}
	ERROR_MSG = re.compile("gnome-session-binary.*GLib-GIO-ERROR.*No GSettings schemas are installed on the system", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if ERROR_MSG.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if ( SUSE.packageInstalled(PACKAGE_NAME) ):
	if( errorFound() ):
		Core.updateStatus(Core.WARN, "If you have graphical interface issues, check gschemas.compiled permissions")
	else:
		Core.updateStatus(Core.IGNORE, "No GLib-GIO-ERROR message found")
else:
        Core.updateStatus(Core.IGNORE, "The package " + PACKAGE_NAME + " is NOT installed")

Core.printPatternResults()

