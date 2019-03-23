#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Converts SysVerilog generated MESM-6 ROMs to logisim representation

with open('jmp16.txt','w') as out:
    out.write("v2.0 raw\n")
    with open('jumptab16.v') as f:
        for line in f.readlines():
            addr, entry = line.split(':')
            out.write(hex(int(entry.strip().split(',')[0][3:]))[2:])
            out.write(' ')

with open('jmp64.txt','w') as out:
    out.write("v2.0 raw\n")
    with open('jumptab64.v') as f:
        for line in f.readlines():
            addr, entry = line.split(':')
            out.write(hex(int(entry.strip().split(',')[0][3:]))[2:])
            out.write(' ')

mc_l = open('mc_l.txt', 'w')
mc_h = open('mc_h.txt', 'w')

mc_l.write("v2.0 raw\n")
mc_h.write("v2.0 raw\n")

with open('microcode.v') as f:
    for line in f.readlines():
        l = line.split(':')[1].strip()[4:-1]
        mc_low  = hex(int(l,8) & 0xffffffff)
        mc_high = hex((int(l,8) >> 32) & 0xffffffff)
        mc_l.write(mc_low[2:]);  mc_l.write(' ')
        mc_h.write(mc_high[2:]); mc_h.write(' ')


