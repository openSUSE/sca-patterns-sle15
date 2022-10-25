#!/usr/bin/python3
#
# Title:       New location for drbd scripts
# Description: Pattern for TID000020749
# Template:    SCA Tool Python Pattern Generator v1.0.2
# Modified:    2022 Oct 04
#
##############################################################################
# Copyright (C) 2022 SUSE LLC
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

meta_class = "HAE"
meta_category = "DRBD"
meta_component = "Resource"
pattern_id = os.path.basename(__file__)
primary_link = "META_LINK_TID"
overall = Core.TEMP
overall_info = "NOT SET"
other_links = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020749|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1203220"
Core.init(meta_class, meta_category, meta_component, pattern_id, primary_link, overall, overall_info, other_links)
resource_scripts = {}

##############################################################################
# Local Function Definitions
##############################################################################

def drbd_configured():
	global resource_scripts
	file_open = "ha.txt"
	section = "/crm configure show"
	content = []
	confirmed = re.compile("primitive.*ocf:linbit:drbd", re.IGNORECASE)
	configured = False
	in_state = False
	if Core.isFileActive(file_open):
		if Core.getRegExSection(file_open, section, content):
			for line in content:
				if in_state:
					if "params drbd_resource=" in line:
						resource = line.split()[-2].split("=")[-1]
						resource_scripts[resource] = False
				elif confirmed.search(line):
					in_state = True
					configured = True
#	print("drbd_configured(" + str(configured) + "): " + str(resource_scripts))
	return configured

def invalid_resource_handlers():
	global resource_scripts
	file_open = "drbd.txt"
	section = "/drbdadm dump"
	content = []
	confirmed = re.compile("^resource .* {", re.IGNORECASE)
	handlers = re.compile(" fence-peer .* /lib/drbd/| after-resync-target .* /lib/drbd/", re.IGNORECASE)
	status = False
	in_state = False
	this_resource= ''
	if Core.isFileActive(file_open):
		if Core.getRegExSection(file_open, section, content):
			for line in content:
				if in_state:
					if line.startswith("}"):
						in_state = False
					else:
						if handlers.search(line):
							resource_scripts[this_resource] = True
							status = True
				elif confirmed.search(line):
					in_state = True
					for resource in resource_scripts.keys():
						if resource in line:
							this_resource = resource
#	print("invalid_resource_handlers(" + str(status) + "): " + str(resource_scripts))
	return status

##############################################################################
# Main
##############################################################################

package = 'drbd-utils'
package_version_fixed = '9.19.0-150400.2.3.1'
invalid_resources = []

if( SUSE.packageInstalled(package) ):
	package_version_installed = SUSE.compareRPM(package, package_version_fixed)
	if( package_version_installed >= 0 ):
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + package + "")
	else:
		if( drbd_configured() ):
			if( invalid_resource_handlers() ):
				for key in resource_scripts.keys():
					if resource_scripts[key]:
						invalid_resources.append(key)
				#print("Critical: " + ' '.join(invalid_resources))
				Core.updateStatus(Core.CRIT, "Detected possible DRBD resource level fencing issue with " + ' '.join(invalid_resources))
			else:
				#print("Ignore")
				Core.updateStatus(Core.IGNORE, "Found valid drbd resource script directories")
		else:
			Core.updateStatus(Core.ERROR, "ERROR: drbd is not a configure HAE resource")
else:
	Core.updateStatus(Core.ERROR, "ERROR: RPM package " + package + " not installed")

Core.printPatternResults()
