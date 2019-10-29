#!/usr/bin/env python

# Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
# [GCC 5.4.0 20160609] on linux2

# a rather simple mac changing script
# must have an external list of viable mac addresses, called full_list
# also works on a file MAC.txt to write and compute mac addresses

# takes list of MAC addresses (and a lot of stuff), extracts only MAC addresses, writes it to MAC.txt

full_list = "oui-macs.txt"
extracted_macs = "MAC.txt"

def mac_front():
	# counts file lines
	def file_len():
	    with open(full_list, "r") as f:
	        for i, l in enumerate(f):
	            pass
	    return i + 1
	
	# writes lines with MAC addresses to MAC.txt
	with open(full_list, "r") as input_:
	        with open(extracted_macs, "w") as output:
	                for j in xrange(file_len()):
	                        readline = input_.readline()
	                        if readline == "\n":
	                                continue
				# checks if a line contains a MAC in **-**-** format (with dashes)
	                        if readline[2] == "-" and readline[5] == "-":
	                                output.write(readline[0:8])
	                                output.write("\n")

# generates a random, legitimate MAC address
def random_mac():
	from random import randint

	# imports MAC fronts from MAC.txt to a list MAC_front
	# it is definetely not a perfect way of obtaining
	# a random MAC from a file, but whatever
	# alas, this imports addresses with the \n new line
	MAC_front = []
	with open(extracted_macs, "r") as f:
		for line in f:
			MAC_front.append(line)
	hex = [i for i in xrange(10)]
	hex += ['A','B','C','D','E','F']
	MAC_back = []
	
	# generates back part of fake MAC
	for i in xrange(8):
	        if i == 2 or i == 5:
	                MAC_back.append("-")
	        else:
	                MAC_back.append(str(hex[randint(0,15)]))
	
	# converts MAC_back (back part of MAC) into a string
	temp = ''
	for h in xrange(len(MAC_back)):
		temp += str(MAC_back[h])
	MAC_back = str(temp)
	
	# slices off the \n new line character from a randomly chosen MAC
        # also randomly picks vendor bytes of mac address
	MAC_front_random = MAC_front[randint(0,len(MAC_front)-1)]
	MAC_front_random = MAC_front_random[0:len(MAC_front_random)-1]

	# concatenates MAC front and back part	
	MAC_final = MAC_front_random + "-" + MAC_back

        # changes dashes in an address to colons, just cosmetics
        mac = ''
        for i in MAC_final:
            if i != '-':
                mac += i
            else:
                mac += ':'

	#return (MAC_final)
        return (mac)

mac_front()
print random_mac()
