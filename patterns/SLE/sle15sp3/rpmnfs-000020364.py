#!/usr/bin/python3
#
# Title:       Pattern for TID000020364
# Description: Upgrading an RPM reports cpio chmod failed
# Source:      Basic Python Pattern Template v0.3.4
# Options:     SLE,RPM,Install,rpmnfs,000020364,1189394,2,0,0
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
META_CATEGORY = "RPM"
META_COMPONENT = "Install"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020364|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1189394"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def nfsShared():
	MOUNT_POINT_LIST = ['/home', '/usr', '/var', '/tmp', '/opt', '/lib', '/lib64', '/srv', '/var/log', '/usr/local']
	FSLIST = SUSE.getFileSystems()
	for FS in FSLIST:
		if( FS['Type'] == 'nfs' ):
#			print(FS['Type'] + ' ' + FS['MountPoint'])
			for MP in MOUNT_POINT_LIST:
				if( FS['MountPoint'] == MP ):
					return True
	return False

def installError():
	fileOpen = "messages.txt"
	section = "/var/log/messages"
	content = []
	CONFIRMED = re.compile("RPM.*install filesystem.*: failure", re.IGNORECASE)
	if Core.isFileActive(fileOpen):
		if Core.getRegExSection(fileOpen, section, content):
			for line in content:
				if CONFIRMED.search(line):
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( nfsShared() ):
	if( installError() ):
		Core.updateStatus(Core.CRIT, "RPM installation failure due to shared mount point")
	else:
		Core.updateStatus(Core.WARN, "RPM packages affecting NFS mount points may need net shared path")
else:
	Core.updateStatus(Core.ERROR, "ERROR: No system NFS mount points")

Core.printPatternResults()

