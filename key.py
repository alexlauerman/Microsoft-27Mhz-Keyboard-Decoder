#!/usr/bin/env python
# #################################################
# Gnuradio Python Flow Graph
# Title: Key
# Generated: Sun Nov  2 12:24:30 2014
# #################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import gr_queue
from gnuradio.gr import firdes
import osmosdr
import sys


class Key(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, "Key")

        # super(Key, self).__init__()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2016000  #1920000#2000000
        self.offset_freq_keyboard = offset_freq_keyboard = 27195000
        self.offset_freq = offset_freq = 27175000
        self.center_freq = center_freq = 28000000
        self.target_rate = target_rate = 48000#16000#96000
        self.offset_keyboard = offset_keyboard = offset_freq_keyboard - center_freq
        self.offset = offset = offset_freq - center_freq
        #self.firdes_tap_overall = firdes_tap_overall = firdes.low_pass(1, samp_rate, 50000, 0100, firdes.WIN_HAMMING,
        #                                                               6.76)
        self.firdes_tap_keyboard = firdes_tap_keyboard = firdes.low_pass(1, samp_rate, 20000, 0100,#5000, 5000, #20000, 10000,
                                                                         firdes.WIN_HAMMING,
                                                                         6.76)

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_source_c_0 = osmosdr.source_c(args="nchan=" + str(1) + " " + "")
        self.osmosdr_source_c_0.set_sample_rate(samp_rate)
        self.osmosdr_source_c_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_c_0.set_freq_corr(0, 0)
        self.osmosdr_source_c_0.set_dc_offset_mode(1, 0)
        self.osmosdr_source_c_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_c_0.set_gain_mode(0, 0)
        self.osmosdr_source_c_0.set_gain(01, 0)
        self.osmosdr_source_c_0.set_if_gain(20, 0)
        self.osmosdr_source_c_0.set_bb_gain(20, 0)
        self.osmosdr_source_c_0.set_antenna("", 0)
        self.osmosdr_source_c_0.set_bandwidth(0, 0)

        self.low_pass_filter_0 = gr.fir_filter_fff(1, firdes.low_pass(
            1, target_rate, 5e3, 01e3, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(int(samp_rate / target_rate),
                                                                                  (firdes_tap_keyboard),
                                                                                  offset_keyboard, samp_rate)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/root/sdr/keyboard/44.1Ks_27Mf_quad3_keyboard.wav", 1,
                                                         target_rate, 8)

        #ACL
        #self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float * 1, "/root/sdr/keyboard/96k_27M_float", False)
        #self.blocks_file_sink_2 = blocks.file_sink(gr.sizeof_float * 1, "/root/sdr/keyboard/96k_27M_float")
        #self.blocks_file_sink_2.set_unbuffered(False)
        self.sink = gr_queue.queue_sink_f()


        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(-5, 1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(2)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_c_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_simple_squelch_cc_0, 0))
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), self.sink)
        #self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.blocks_file_sink_2, 0))

    def __iter__(self):
        return self.sink.__iter__()


def get_samp_rate(self):
    return self.samp_rate


def set_samp_rate(self, samp_rate):
    self.samp_rate = samp_rate
    # self.set_firdes_tap_overall(firdes.low_pass(1, self.samp_rate, 50000, 0100, firdes.WIN_HAMMING, 6.76))
    self.osmosdr_source_c_0.set_sample_rate(self.samp_rate)


def get_offset_freq_keyboard(self):
    return self.offset_freq_keyboard


def set_offset_freq_keyboard(self, offset_freq_keyboard):
    self.offset_freq_keyboard = offset_freq_keyboard
    self.set_offset_keyboard(self.offset_freq_keyboard - self.center_freq)


def get_offset_freq(self):
    return self.offset_freq


def set_offset_freq(self, offset_freq):
    self.offset_freq = offset_freq
    self.set_offset(self.offset_freq - self.center_freq)


def get_center_freq(self):
    return self.center_freq


def set_center_freq(self, center_freq):
    self.center_freq = center_freq
    self.set_offset_keyboard(self.offset_freq_keyboard - self.center_freq)
    self.set_offset(self.offset_freq - self.center_freq)
    self.osmosdr_source_c_0.set_center_freq(self.center_freq, 0)


def get_target_rate(self):
    return self.target_rate


def set_target_rate(self, target_rate):
    self.target_rate = target_rate
    self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.target_rate, 5e3, 01e3, firdes.WIN_HAMMING, 6.76))


def get_offset_keyboard(self):
    return self.offset_keyboard


def set_offset_keyboard(self, offset_keyboard):
    self.offset_keyboard = offset_keyboard
    self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.offset_keyboard)


def get_offset(self):
    return self.offset


def set_offset(self, offset):
    self.offset = offset


def get_firdes_tap_overall(self):
    return self.firdes_tap_overall


def set_firdes_tap_overall(self, firdes_tap_overall):
    self.firdes_tap_overall = firdes_tap_overall


def get_firdes_tap_keyboard(self):
    return self.firdes_tap_keyboard


def set_firdes_tap_keyboard(self, firdes_tap_keyboard):
    self.firdes_tap_keyboard = firdes_tap_keyboard
    self.freq_xlating_fir_filter_xxx_0_0.set_taps((self.firdes_tap_keyboard))


def transition(data, level=0.20):
    """Threshold a stream and yield transitions and their associated timing.
        Used to detect the On-Off-Keying (OOK)"""

    last = "off"
    last_i = 0  # stores last time i changed
    position = "none"
    printwindow = 0



    for i, val in enumerate(data):
        if (val > level):
            state = "high"
            # print val
        elif (-val > level):
            state = "low"
            # print val
        else:
            state = "off"

        #if val != 0 and printwindow == 0:
        #    printwindow = 1
        #if printwindow > 0 and printwindow < 3000:
        #    print "on: " + str(val) + " " + str(i)
        #    printwindow += 1
        #else:
        #    printwindow = 0



        if (state != last and i - last_i > 1) or (
                        state == "off" and (i - last_i) > 200):  #if new state or we've been off for a while, return data
            yield (last, i - last_i, i)
            last_i = i
            last = state




def decode(stream):
    packet = []

    #for i in transition(stream):
    for signalstate, time, abstime in transition(stream):

        if signalstate != "off":  #just finsihed a "bit", and high/low is returned
            #debug time print
            #print signalstate, millertime(time), time, abstime
            #pass
            #print i
            if millertime(time) > 0 and millertime(time) < 7:
                if (signalstate == "high"):
                    packet.append(millertime(time))
                else:
                    packet.append(-millertime(time))
                    #if millertime(time)== 7 and time != 01001:
                    #print "7 time: " + str(time)
        if millertime(time) == 7 and packet != []:
            #print "YIELDING PACKET------------"
            #print "7 time: " + str(time)
            yield packet
            packet = []


def millertime(time):  # 16 (only 3)  35 55 75 95 115 (only 6)  hundreds of thousands (break)  #after changing samp rate: 34 53 72 91, 101

    #basetime = 34
    #t1 = basetime *.75  #26
    #t2 = basetime       #34
    #t3 = basetime * 1.5 #52
    #t4 = basetime * 2   #68
    #t5 = basetime * 2.5 #84
    #t6 = basetime * 3   #010


    decimationfactor = 96000/48000#samp_rate / target_rate
    t1 = 25 / decimationfactor  #basetime *.75  #26
    t2 = 45 / decimationfactor#basetime        #34
    t3 = 64 / decimationfactor#basetime * 1.5 #52
    t4 = 84 / decimationfactor#basetime * 2   #68
    t5 = 010 / decimationfactor#basetime * 2.5 #84
    t6 = 195 / decimationfactor#basetime * 3   #010

    #with 2.016M samples, breaks at 25,45,64,87,010,195
    #print "Time" + str(time)
    if (time > 1 and time <= t1):
        return 1  #"short " + str(time)
    if (time > t1 and time <= t2):
        return 2  #"medium " + str(time)
    if (time > t2 and time <= t3):
        return 3  #"mediumlong " + str(time)
    if (time > t3 and time <= t4):
        return 4  #"long " + str(time)
    if (time > t4 and time <= t5):
        return 5  #"verylong " + str(time)
    if (time > t5 and time <= t6):
        return 6  #"veryverylong " + str(time)
    if (time > t6):
        return 7  #"break " + str(time)
    else:
        print "Cant handle Time: " + str(time)
        return 1


# 2=A
#3=B
#4=C
#5=start/stop (if started)
#6=sync

def millerdecodepacket(packet):
    #1 bit different
    data = ""
    state = "off"
    lastdata = 0

    for d in packet:
        d = abs(d)
        #print "D: " + str(d)
        if d == 6:  #sync
            state = "sync"
        if d == 5:  #start/stop
            if state != "data":
                state = "data"
                data += "0"
                lastdata = 0
            else:
                state = "off"

        if state == "data":
            if d == 2:  #diff to last bit
                if lastdata == 0:
                    data += "1"
                    lastdata = 1
                else:
                    data += "0"
                    lastdata = 0
            elif d == 3:  #1 same, 1 different
                if lastdata == 0:
                    data += "0"
                    data += "1"
                    lastdata = 1
                else:
                    data += "1"
                    data += "0"
                    lastdata = 0
            elif d == 4:  #2 bit same as last bit
                if lastdata == 1:
                    data += "1"
                    data += "1"
                    lastdata = 1
                else:
                    data += "0"
                    data += "0"
                    lastdata = 0

    return data


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    stream.stop()


if __name__ == '__main__':

    stream = Key()  #freq, freq_offs, decimate_am=2, play_audio=options.audio)

    sys.stdout.write("\n")
    try:
        #stream.run()
        stream.start()  #rtl433
    except [[KeyboardInterrupt]]:
        print('You pressed Ctrl+C!')
        stream.stop()


def lookupLetter(bits):
    return {

        #these codes have been modified so that they dont wory with my keyboard.  Consider these dummy codes and record your own, or share yours and we'll figure out the keybard ID part.
        '000110101001111100000000001001111001010': 'a',
        '010111001001111100000000011001111001010': 'b',
        '001110101001111100000000000001111001010': 'c',
        '001111001001111100000000010001111001010': 'd',
        '000000101001111100000000001111111001010': 'e',
        '011101001001111100000000011111111001010': 'f',
        '000101001001111100000000000111111001010': 'g',
        '001001001001111100000000010111111001010': 'h',
        '000011001001111100000000001011111001010': 'i',
        '010101001001111100000000011011111001010': 'j',
        '001011001001111100000000000011111001010': 'k',
        '001101001001111100000000010011111001010': 'l',
        '000001101001111100000000001100111001010': 'm',
        '011010101001111100000000011100111001010': 'n',
        '000110101001111100000000000100111001010': 'o',
        '001010101001111100000000010100111001010': 'p',
        '000101101001111100000000001000111001010': 'q',
        '010110101001111100000000011000111001010': 'r',
        '001101101001111100000000000000111001010': 's',
        '001110101001111100000000010000111001010': 't',
        '000000011001111100000000001110111001010': 'u',
        '011110101001111100000000011110111001010': 'v',
        '000100101001111100000000000110111001010': 'w',
        '001000101001111100000000010110111001010': 'x',
        '000010101001111100000000001010111001010': 'y',
        '010100101001111100000000011010111001010': 'z',

        '000111001001111100100000001001111001010': 'A',
        '001011001001111100100000011001111001010': 'B',
        '000110101001111100100000000001111001010': 'C',
        '010111001001111100100000010001111001010': 'D',
        '001101101001110100100000001111111001010': 'E',
        '001110001001111100100000011111111001010': 'F',
        '000000101001111100100000000111111001010': 'G',
        '011101101001110100100000010111111001010': 'H',
        '000101001001111100100000001011111001010': 'I',
        '001001001001111100100000011011111001010': 'J',
        '000011001001111100100000000011111001010': 'K',
        '010101101001110100100000010011111001010': 'L',
        '001010101001111100100000001100111001010': 'M',
        '001100011001110100100000011100111001010': 'N',
        '000001101001111100100000000100111001010': 'O',
        '011010011001110100100000010100111001010': 'P',
        '000110101001111100100000001000111001010': 'Q',
        '001010101001111100100000011000111001010': 'R',
        '000101101001111100100000000000111001010': 'S',
        '010110101001111100100000010000111001010': 'T',
        '001111011001110100100000001110111001010': 'U',
        '001111001001111100100000011110111001010': 'V',
        '000000011001111100100000000110111001010': 'W',
        '011110101001111100100000010110111001010': 'X',
        '000100101001111100100000001010111001010': 'Y',
        '001000101001111100100000011010111001010': 'Z',

        '000011101001111100000000001011011001010': ' ',

        '10100100011000111110101': None, #keyboard ID?
        '':'',

        }.get(bits, None)


def printpacket(packet):
    output = "\n"

    for d in packet:
        output += str(abs(d))

    #print "---------------------------------------PRINTING PACKET ABOVE-------------------------------------"
    #print output

    m = millerdecodepacket(packet)

    #print


    l = lookupLetter(m)

    if l is not None:
        #print l
        #sys.stdout.write(l)
        print l

    #else:
        #debug print
        #print m


for packet in decode(stream):
    printpacket(packet)
print "ended"

