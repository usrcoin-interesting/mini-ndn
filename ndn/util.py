# -*- Mode:python; c-file-style:"gnu"; indent-tabs-mode:nil -*- */
#
# Copyright (C) 2015-2017, The University of Memphis,
#                          Arizona Board of Regents,
#                          Regents of the University of California.
#
# This file is part of Mini-NDN.
# See AUTHORS.md for a complete list of Mini-NDN authors and contributors.
#
# Mini-NDN is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mini-NDN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mini-NDN, e.g., in COPYING.md file.
# If not, see <http://www.gnu.org/licenses/>.

from subprocess import call
from mininet.cli import CLI
import sys

sshbase = [ 'ssh', '-q', '-t', '-i/home/mininet/.ssh/id_rsa' ]
scpbase = [ 'scp', '-i', '/home/mininet/.ssh/id_rsa' ]
devnull = open('/dev/null', 'w')

def ssh(login, cmd):
    rcmd = sshbase + [login, cmd]
    call(rcmd, stdout=devnull, stderr=devnull)

def scp(*args):
    tmp = []
    for arg in args:
        tmp.append(arg)
    rcmd = scpbase + tmp
    call(rcmd, stdout=devnull, stderr=devnull)

class MiniNDNCLI(CLI):
    prompt = 'mini-ndn> '
    def __init__(self, mininet, stdin=sys.stdin, script=None):
        CLI.__init__(self, mininet, stdin=sys.stdin, script=None)
