#!/usr/bin/python

# Title:       openssh patch breaks gssapi
# Description: OpenSSH maintenance update breaks GSSAPI login
# Modified:    2018 Nov 19
#
##############################################################################
# Copyright (C) 2018 SUSE
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
META_CATEGORY = "OpenSSH"
META_COMPONENT = "Login"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=7023532|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1115654"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def gssapiEnabled():
	FILE_OPEN = "ssh.txt"
	SECTION = "sshd_config"
	GSSAPI = re.compile("^GSSAPIAuthentication.*yes", re.IGNORECASE)
	CONTENT = []
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if GSSAPI.search(LINE):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'openssh'
RPM_VERSION = '7.6p1-9.3.1'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION)
	if( INSTALLED_VERSION == 0 ):
		if gssapiEnabled():
			Core.updateStatus(Core.CRIT, "GSSAPI Logins may fail, update system to resolve")
		else:
			Core.updateStatus(Core.IGNORE, "GSSAPI authentication disabled")
	else:
		Core.updateStatus(Core.IGNORE, "GSSAPI Login issue mitigated")
else:
	Core.updateStatus(Core.ERROR, "ERROR: RPM package not installed: " + RPM_NAME)


Core.printPatternResults()


