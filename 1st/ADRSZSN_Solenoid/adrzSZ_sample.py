#!/usr/bin/python3
#coding: utf-8
#####!�Ŏn�܂�1�s�ڂ̋L�q��Shebang�X�N���v�g���̂����s
#####2�s�ڂɁA�}�W�b�N�R�����g���L�q�����G���R�[�f�B���O
#
#
# �t�@�C�����FadrszSN_sample.py
# �o�[�W�����F2018/6/20 v1.0  python3�p
#          
#
# �r�b�g�E�g���[�h�E�����В񋟂�zeroone�V���[�Y �\���m�C�h���W���[��(�^�ԁFADRSZSN)�p�̗��v���O����
#�@���쌠��:(C) 2015 �r�b�g�E�g���[�h�E������
#�@���C�Z���X: MIT License
#
#  ���s���@�F ./adrszSN_sample.py
#�@���s����Ɓ@�\���m�C�h��0.5�b�n�m�ɂȂ�2�b�Ԋu�ŌJ��Ԃ��܂��B
#  
#�@


port = 4
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.OUT)
while 1:
    GPIO.output(port, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(port, GPIO.LOW)
    time.sleep(1.5)
GPIO.cleanup()
