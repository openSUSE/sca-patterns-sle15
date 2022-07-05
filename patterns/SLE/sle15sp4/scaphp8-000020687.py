#!/usr/bin/python3
#
# Title:       Pattern for TID000020687
# Description: PHP Version ERROR and Additional Required Packages ERROR from setup-sca Utility
# Source:      Package Version Pattern Template v1.0.0
# Options:     SLE,SCA,Setup,scaphp8,000020687,1201011,sca-appliance-broker,1.3.1-1,0,1
# Modified:    2022 Jul 05
#
##############################################################################
# Copyright (C) 2022, SUSE LLC
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
META_CATEGORY = "SCA"
META_COMPONENT = "Setup"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc/?id=000020687|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1201011"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def scaConfigured():
	fileOpen = "etc.txt"
	CONFIGURED = True
	content = []
	section = "/etc/sca/sdbroker.conf"
	CONFIRMED = re.compile("Run setup-sdbroker", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				CONFIGURED = False
	content = []
	section = "/etc/sca/sdagent.conf"
	CONFIRMED = re.compile("Run sdagent-config", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				CONFIGURED = False
	content = []
	section = "/etc/sca/sdp.conf"
	CONFIRMED = re.compile("Run setup-sdp", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if CONFIRMED.search(line):
				CONFIGURED = False

	return CONFIGURED


def servicesRunning():
	RUNNING=0
	SERVICE_INFO = SUSE.getServiceDInfo('mariadb.service')
	if( 'SubState' in SERVICE_INFO ):
		if( SERVICE_INFO['SubState'] == 'running' ):
			RUNNING+=1
	SERVICE_INFO = SUSE.getServiceDInfo('apache2.service')
	if( 'SubState' in SERVICE_INFO ):
		if( SERVICE_INFO['SubState'] == 'running' ):
			RUNNING+=1
	if( RUNNING == 2 ):
		return True
	else:
		return False

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'sca-appliance-broker'
RPM_VERSION = '1.3.1-1'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION)
	if( INSTALLED_VERSION <= 0 ):
		if( scaConfigured() ):
			Core.updateStatus(Core.IGNORE, "PHP8 Workaround applied")
		else:
			if( servicesRunning() ):
				Core.updateStatus(Core.CRIT, "PHP version mismatch for setup-sca")
			else:
				Core.updateStatus(Core.WARN, "Running setup-sca may fail with PHP errors")
	else:
		Core.updateStatus(Core.IGNORE, "PHP8 fix applied")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")


Core.printPatternResults()

