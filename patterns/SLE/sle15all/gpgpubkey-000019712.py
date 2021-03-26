#!/usr/bin/python

# Title:       Unsupported V3 Key
# Description: zypper or rpm warns about unsupported V3 key after upgrade
# Distros:     SLE15*
# Modified:    2021 Mar 26
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
META_CATEGORY = "Update"
META_COMPONENT = "Keys"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000019712|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1158913"
RMKEY = ''

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)
##############################################################################
# Local Function Definitions
##############################################################################

def unsupportedV3key():
	fileOpen = "rpm.txt"
	section = "rpm.*uniq"
	content = []
	CONFIRMED = re.compile("warning: Unsupported version of key: V3", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				return True
	return False

def getV3Key():
	global RMKEY

	fileOpen = "updates.txt"
	section = "patch-check"
	content = []
	CONFIRMED = re.compile("gpg-pubkey-", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					RMKEY = line.strip()
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( unsupportedV3key() ):
	if( getV3Key() ):
		Core.updateStatus(Core.WARN, "Detected unsupported V3 key, remove " + str(RMKEY))
	else:
		Core.updateStatus(Core.WARN, "Detected unsupported V3 key")
else:
	Core.updateStatus(Core.IGNORE, "No unsupported V3 keys found")

Core.printPatternResults()

