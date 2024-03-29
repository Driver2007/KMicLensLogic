#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        Stigmator1.py
#
#  Project :     Stigmator1
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      sergey.v.babenkov$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["Stigmator1", "Stigmator1Class", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(Stigmator1.additionnal_import) ENABLED START -----#
from math import cos, sin, pi
import time
import threading
import Tkinter
import tkMessageBox
#----- PROTECTED REGION END -----#	//	Stigmator1.additionnal_import

# Device States Description
# No states for this device


class Stigmator1 (PyTango.Device_4Impl):
    """Stigmator1"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(Stigmator1.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	Stigmator1.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        Stigmator1.init_device(self)
        #----- PROTECTED REGION ID(Stigmator1.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(Stigmator1.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_DeflX_read = 0.0
        self.attr_DeflY_read = 0.0
        self.attr_Stig2a_read = 0.0
        self.attr_Stig2b_read = 0.0
        self.attr_Stig4_read = 0.0
        self.attr_Offset_read = 0.0
        self.attr_Angle_read = 0.0
        self.attr_Status_oct_read = False
        self.attr_VoltageOutput_read = False
        self.attr_Setting_Valid_read = False
        #----- PROTECTED REGION ID(Stigmator1.init_device) ENABLED START -----#         
        self.DX  = 0.0 # values which are used for calculation
        self.DY  = 0.0
        self.S2a = 0.0
        self.S2b = 0.0
        self.S4  = 0.0
        self.A   = 0.0
        self.OFF = 0.0
        
        self.ISEG=PyTango.DeviceProxy("ktof/logic/lens1")
        self.DevStat = [False for i in range(8)]
        self.DevStat_check = [True for i in range(8)]
        
        if not 'pingthread' in dir(self):
            self.pingthread = threading.Thread(target=self.check_voltages)
            self.pingthread.setDaemon(True)
            self.pingthread.start()
        #----- PROTECTED REGION END -----#	//	Stigmator1.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(Stigmator1.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.always_executed_hook

    # -------------------------------------------------------------------------
    #    Stigmator1 read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_DeflX(self, attr):
        self.debug_stream("In read_DeflX()")
        #----- PROTECTED REGION ID(Stigmator1.DeflX_read) ENABLED START -----#
        attr.set_value(self.attr_DeflX_read)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.DeflX_read
        
    def write_DeflX(self, attr):
        self.debug_stream("In write_DeflX()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Stigmator1.DeflX_write) ENABLED START -----#
        self.attr_DeflX_read=data
        self.DX=data
        
        self.update_outputs()
        #----- PROTECTED REGION END -----#	//	Stigmator1.DeflX_write
        
    def read_DeflY(self, attr):
        self.debug_stream("In read_DeflY()")
        #----- PROTECTED REGION ID(Stigmator1.DeflY_read) ENABLED START -----#
        attr.set_value(self.attr_DeflY_read)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.DeflY_read
        
    def write_DeflY(self, attr):
        self.debug_stream("In write_DeflY()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Stigmator1.DeflY_write) ENABLED START -----#
        self.attr_DeflY_read=data
        self.DY=data
        
        self.update_outputs()
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.DeflY_write
        
    def read_Stig2a(self, attr):
        self.debug_stream("In read_Stig2a()")
        #----- PROTECTED REGION ID(Stigmator1.Stig2a_read) ENABLED START -----#
        attr.set_value(self.attr_Stig2a_read)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.Stig2a_read
        
    def write_Stig2a(self, attr):
        self.debug_stream("In write_Stig2a()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Stigmator1.Stig2a_write) ENABLED START -----#
        self.attr_Stig2a_read=data
        self.S2a=data
        
        self.update_outputs()
        #----- PROTECTED REGION END -----#	//	Stigmator1.Stig2a_write
        
    def read_Stig2b(self, attr):
        self.debug_stream("In read_Stig2b()")
        #----- PROTECTED REGION ID(Stigmator1.Stig2b_read) ENABLED START -----#
        attr.set_value(self.attr_Stig2b_read)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.Stig2b_read
        
    def write_Stig2b(self, attr):
        self.debug_stream("In write_Stig2b()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Stigmator1.Stig2b_write) ENABLED START -----#
        self.attr_Stig2b_read=data
        self.S2b=data
        
        self.update_outputs()
        #----- PROTECTED REGION END -----#	//	Stigmator1.Stig2b_write
        
    def read_Stig4(self, attr):
        self.debug_stream("In read_Stig4()")
        #----- PROTECTED REGION ID(Stigmator1.Stig4_read) ENABLED START -----#
        attr.set_value(self.attr_Stig4_read)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.Stig4_read
        
    def write_Stig4(self, attr):
        self.debug_stream("In write_Stig4()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Stigmator1.Stig4_write) ENABLED START -----#
        self.attr_Stig4_read=data
        self.S4=data
       
        self.update_outputs()
        #----- PROTECTED REGION END -----#	//	Stigmator1.Stig4_write
        
    def read_Offset(self, attr):
        self.debug_stream("In read_Offset()")
        #----- PROTECTED REGION ID(Stigmator1.Offset_read) ENABLED START -----#
        attr.set_value(self.attr_Offset_read)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.Offset_read
        
    def write_Offset(self, attr):
        self.debug_stream("In write_Offset()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Stigmator1.Offset_write) ENABLED START -----#
        self.attr_Offset_read=data
        self.OFF=data
        
        self.update_outputs()
        #----- PROTECTED REGION END -----#	//	Stigmator1.Offset_write
        
    def read_Angle(self, attr):
        self.debug_stream("In read_Angle()")
        #----- PROTECTED REGION ID(Stigmator1.Angle_read) ENABLED START -----#
        attr.set_value(self.attr_Angle_read)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.Angle_read
        
    def write_Angle(self, attr):
        self.debug_stream("In write_Angle()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Stigmator1.Angle_write) ENABLED START -----#
        self.attr_Angle_read=data
        self.A=data        
        
        self.update_outputs()
        #----- PROTECTED REGION END -----#	//	Stigmator1.Angle_write
        
    def read_Status_oct(self, attr):
        self.debug_stream("In read_Status_oct()")
        #----- PROTECTED REGION ID(Stigmator1.Status_oct_read) ENABLED START -----#
        if self.ISEG.state()==PyTango.DevState.ON:
            for i in range(8):
                self.DevStat[i]=self.ISEG.read_attribute("CH"+str(i)+"_Conn").value
            if self.DevStat==self.DevStat_check:
                self.attr_Status_oct_read=True
        attr.set_value(self.attr_Status_oct_read)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.Status_oct_read
        
    def write_Status_oct(self, attr):
        self.debug_stream("In write_Status_oct()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Stigmator1.Status_oct_write) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.Status_oct_write
        
    def read_VoltageOutput(self, attr):
        self.debug_stream("In read_VoltageOutput()")
        #----- PROTECTED REGION ID(Stigmator1.VoltageOutput_read) ENABLED START -----#
        attr.set_value(self.attr_VoltageOutput_read)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.VoltageOutput_read
        
    def write_VoltageOutput(self, attr):
        self.debug_stream("In write_VoltageOutput()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(Stigmator1.VoltageOutput_write) ENABLED START -----#
        self.setOutputOnOnff(data)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.VoltageOutput_write
        
    def read_Setting_Valid(self, attr):
        self.debug_stream("In read_Setting_Valid()")
        #----- PROTECTED REGION ID(Stigmator1.Setting_Valid_read) ENABLED START -----#
        attr.set_value(self.attr_Setting_Valid_read)
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.Setting_Valid_read
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(Stigmator1.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.read_attr_hardware


    # -------------------------------------------------------------------------
    #    Stigmator1 command methods
    # -------------------------------------------------------------------------
    

    #----- PROTECTED REGION ID(Stigmator1.programmer_methods) ENABLED START -----#
    def update_outputs(self):
        print self.attr_DeflX_read, self.attr_DeflY_read, self.attr_Stig2a_read, self.attr_Stig2b_read, self.attr_Stig4_read, self.attr_Offset_read, self.attr_Angle_read    
        A=self.attr_Angle_read/180.*pi  
        V = [0 for i in range(8)]
        for i in range(8):
            V[i] = self.DX*cos(i*pi/4.0-A) +\
                self.DY*cos(i*pi/4.0-A-pi/2) +\
                self.S2a*cos(i*pi/2.0-A) +\
                self.S2b*cos(i*pi/2.0-A-pi/2) +\
                self.S4*cos(i*pi-A) +\
                self.OFF
        for i in range(8):
            V[i]=round(V[i],2)
            print V[i]
            if V[i]>2000 or V[i]<0:
                self.attr_Setting_Valid_read=False
                break
            else:
                self.attr_Setting_Valid_read=True
        print ("settings status", self.attr_Setting_Valid_read)
        if self.attr_Setting_Valid_read==True:
            self.write_voltage(V)
    
    def write_voltage(self, V):
        self.ISEG.write_attribute("CH3_0_VUSet",V[5])#bottom left
        self.ISEG.write_attribute("CH3_1_VUSet",V[2])
        self.ISEG.write_attribute("CH3_2_VUSet",V[0])
        self.ISEG.write_attribute("CH3_3_VUSet",V[7])
        self.ISEG.write_attribute("CH3_4_VUSet",V[6])
        self.ISEG.write_attribute("CH3_5_VUSet",V[3])
        self.ISEG.write_attribute("CH3_6_VUSet",V[4])
        self.ISEG.write_attribute("CH3_7_VUSet",V[1])
        self.ISEG.write_attribute("COL1_VUSet",self.OFF)
    def setOutputOnOnff(self, OnOff):
        if self.ISEG.state()==PyTango.DevState.ON:
            if OnOff==True:
                print ("channels ON")
                self.attr_VoltageOutput_read=True
                self.ISEG.CH3_0_VSetOn=True
                self.ISEG.CH3_1_VSetOn=True
                self.ISEG.CH3_2_VSetOn=True
                self.ISEG.CH3_3_VSetOn=True
                self.ISEG.CH3_4_VSetOn=True
                self.ISEG.CH3_5_VSetOn=True
                self.ISEG.CH3_6_VSetOn=True
                self.ISEG.CH3_7_VSetOn=True
                self.ISEG.COL1_VSetOn=True
            elif OnOff == False:
                self.attr_VoltageOutput_read=False
                self.ISEG.CH3_0_VSetOn=False
                self.ISEG.CH3_1_VSetOn=False
                self.ISEG.CH3_2_VSetOn=False
                self.ISEG.CH3_3_VSetOn=False
                self.ISEG.CH3_4_VSetOn=False
                self.ISEG.CH3_5_VSetOn=False
                self.ISEG.CH3_6_VSetOn=False
                self.ISEG.CH3_7_VSetOn=False   
                self.ISEG.COL1_VSetOn=False
    def check_voltages(self):
        voltage_ch=[0.0]*9
        VoltageLim=20
        while True:
            if self.ISEG.state()==PyTango.DevState.ON:
                for i in range (8):
                    voltage_ch[i]=self.ISEG.read_attribute("CH3_"+str(i)+"_VURead").value
                voltage_ch[8]=self.ISEG.read_attribute("COL1_VURead").value
                for i in range (8):
                    if abs(voltage_ch[i]-voltage_ch[i+1])>VoltageLim:
                        self.setOutputOnOnff(False)
                        root = Tkinter.Tk()
                        root.withdraw()
                        tkMessageBox.showinfo("Stigmator 1 protector", "Voltage difference is too high /n or one of the channels is off")

            time.sleep(0.2)
            

    #----- PROTECTED REGION END -----#	//	Stigmator1.programmer_methods

class Stigmator1Class(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(Stigmator1.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	Stigmator1.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        }


    #    Attribute definitions
    attr_list = {
        'DeflX':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'Memorized':"true"
            } ],
        'DeflY':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'Memorized':"true"
            } ],
        'Stig2a':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'Memorized':"true"
            } ],
        'Stig2b':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'Memorized':"true"
            } ],
        'Stig4':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'Memorized':"true"
            } ],
        'Offset':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'Memorized':"true"
            } ],
        'Angle':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'Memorized':"true"
            } ],
        'Status_oct':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'Memorized':"true"
            } ],
        'VoltageOutput':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'Memorized':"true"
            } ],
        'Setting_Valid':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ]],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(Stigmator1Class, Stigmator1, 'Stigmator1')
        #----- PROTECTED REGION ID(Stigmator1.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	Stigmator1.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
