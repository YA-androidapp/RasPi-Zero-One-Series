#!/usr/bin/python3
#coding: utf-8
#####!�Ŏn�܂�1�s�ڂ̋L�q��Shebang�X�N���v�g���̂����s
#####2�s�ڂɁA�}�W�b�N�R�����g���L�q�����G���R�[�f�B���O
#
#
# �t�@�C�����F/home/pi/zeroone/adrszLX/adrszLX_sample.py
# �o�[�W�����F2018/6/8 v1.0  python3�p
#          
#
# �r�b�g�E�g���[�h�E�����В񋟂�zeroone�V���[�Y ���邳�Z���T���W���[��(�^�ԁFADRSZLX)�p�̗��v���O����
#�@���쌠��:(C) 2015 �r�b�g�E�g���[�h�E������
#�@���C�Z���X: ADL(Assembly Desk License)
#
#  ���s���@�F ./adrszLX_sample.py
#�@���s����Ɓ@�Ɠx�Flumi�@�ߐڋ����Fproxi�@�����L�̂悤�ɏo�͂��܂��B
#  ���s���ʁ@�@{'lumi': 2555 ,'proxi': 2281}
#�@�Ɠx�Flumi�@�͑�����x�͈́F10�`16383 Lux
#�@�@�@�Z���T����̂�鐔�l�́Aambient Light Signal(cts)�l�ł��B
#�@�@�@���l�́A�f�[�^�V�[�g�ɗ��ΐ��O���t�ŕ\������Ă��܂��B
#�@�@�@�@�@�@�@���ΐ��O���t�́Aambient Light Signal(cts)�΁AAmbient Light Value(lx)�ł��B
#�@�@�@�@�@�@�@�O���t���Alx�l�����Z���A���ЂŎ������܂��Ă݂܂����B
#�@�@�@�@�@�@�@�@�@�@�@�@�@���̏�́A�u����������ƁF1500lux�A�����ƁF750lux���x�ł����B
#�@�ߐڋ����Fproxi�@���苗���͈�: 1�`200 mm�@�œK�Ȕ͈�: 10�`150 mm�iAdafruit���ׁj
#�@�@�@���ЂɂĎ��������Ƃ���A10�����`30�������x�ŁA�l��8000�`2500���x�ω����܂���
#�@�@�@���l�́A�f�[�^�V�[�g�ɑΐ��O���t�ŕ\������Ă���̂ŁA���l�ƁA�����̊��Z�͍���ł�
#�@�@�@���l��2500�ȏ�Ȃ�30�����ȓ��ɁA���̂�������x�̎g�p�@�ɂȂ�Ǝv���܂��B
#
# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# VCNL4010
# This code is designed to work with the VCNL4010_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Light?sku=VCNL4010_I2CS#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# VCNL4010 address, 0x13(19)
# Select command register, 0x80(128)
#		0xFF(255)	Enable ALS and proximity measurement, LP oscillator
bus.write_byte_data(0x13, 0x80, 0xFF)
# VCNL4010 address, 0x13(19)
# Select proximity rate register, 0x82(130)
#		0x00(00)	1.95 proximity measeurements/sec
bus.write_byte_data(0x13, 0x82, 0x00)
# VCNL4010 address, 0x13(19)
# Select ambient light register, 0x84(132)
#		0x9D(157)	Continuos conversion mode, ALS rate 2 samples/sec
bus.write_byte_data(0x13, 0x84, 0x9D)

time.sleep(0.8)

#while (1):
# VCNL4010 address, 0x13(19)
# Read data back from 0x85(133), 4 bytes
# luminance MSB, luminance LSB, Proximity MSB, Proximity LSB
data = bus.read_i2c_block_data(0x13, 0x85, 4)

# Convert the data
luminance = data[0] * 256 + data[1]
proximity = data[2] * 256 + data[3]

# Output data to screen
#print ("Ambient Light Luminance : %d lux" %luminance)
#print ("Proximity of the Device : %d" %proximity)
print ("{'lumi': %d " %luminance +",'proxi': %d"%proximity + "}")
#time.sleep(1.0)

