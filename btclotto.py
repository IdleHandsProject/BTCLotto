#To run you need to have cgminer running already, then run 
#sudo python btclotto.py <local ip>

import socket
import urlparse
import urllib
import time
import math


from neopixel import *


# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

BLOCK = '000000000000000000e04b20fb1ddd3305d4e7112a9c4247e59d224a89f96d5a'
FOUND = 0

def loser(strip, wait_ms=20):
        for j in range(32):
                strip.setPixelColorRGB(0, 255,255,0)
                strip.setPixelColorRGB(1, 255,255,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,8*j,0)
                strip.setPixelColorRGB(4, 0,8*j,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(6, 0,0,0)
                strip.setPixelColorRGB(7, 0,0,0)
                strip.show()
                time.sleep(0.05)
                strip.setPixelColorRGB(6, 255,255,0)
                strip.setPixelColorRGB(7, 255,255,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,8*j,0)
                strip.setPixelColorRGB(4, 0,8*j,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(0, 0,0,0)
                strip.setPixelColorRGB(1, 0,0,0)
                strip.show()
                time.sleep(0.05)
        for q in range(8):
                strip.setPixelColorRGB(6, 255,0,0)
                strip.setPixelColorRGB(7, 255,0,0)
                strip.setPixelColorRGB(2, 255,0,0)
                strip.setPixelColorRGB(3, 255,0,0)
                strip.setPixelColorRGB(4, 255,0,0)
                strip.setPixelColorRGB(5, 255,0,0)
                strip.setPixelColorRGB(0, 255,0,0)
                strip.setPixelColorRGB(1, 255,0,0)
                strip.show()
                time.sleep(0.3)
                strip.setPixelColorRGB(6, 0,0,0)
                strip.setPixelColorRGB(7, 0,0,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,0,0)
                strip.setPixelColorRGB(4, 0,0,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(0, 0,0,0)
                strip.setPixelColorRGB(1, 0,0,0)
                strip.show()
                time.sleep(0.3)

def winner(strip, wait_ms=20):
        for j in range(32):
                strip.setPixelColorRGB(0, 255,255,0)
                strip.setPixelColorRGB(1, 255,255,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,8*j,0)
                strip.setPixelColorRGB(4, 0,8*j,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(6, 0,0,0)
                strip.setPixelColorRGB(7, 0,0,0)
                strip.show()
                time.sleep(0.05)
                strip.setPixelColorRGB(6, 255,255,0)
                strip.setPixelColorRGB(7, 255,255,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,8*j,0)
                strip.setPixelColorRGB(4, 0,8*j,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(0, 0,0,0)
                strip.setPixelColorRGB(1, 0,0,0)
                strip.show()
                time.sleep(0.05)
        for q in range(30):
                strip.setPixelColorRGB(6, 0,255,0)
                strip.setPixelColorRGB(7, 0,255,0)
                strip.setPixelColorRGB(2, 0,255,0)
                strip.setPixelColorRGB(3, 0,255,0)
                strip.setPixelColorRGB(4, 0,255,0)
                strip.setPixelColorRGB(5, 0,255,0)
                strip.setPixelColorRGB(0, 0,255,0)
                strip.setPixelColorRGB(1, 0,255,0)
                strip.show()
                time.sleep(0.1)
                strip.setPixelColorRGB(6, 0,0,0)
                strip.setPixelColorRGB(7, 0,0,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,0,0)
                strip.setPixelColorRGB(4, 0,0,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(0, 0,0,0)
                strip.setPixelColorRGB(1, 0,0,0)
                strip.show()
                time.sleep(0.1)

def dispBlock(strip,block, wait_ms=20):
        for j in range(1,2):
                for q in range(7):
                        r = int(block[j+0+(6*q)]+block[j+1+(6*q)],16)
                        g = int(block[j+2+(6*q)]+block[j+3+(6*q)],16)
                        b = int(block[j+4+(6*q)]+block[j+5+(6*q)],16)
                        strip.setPixelColorRGB(q, r,g,b)
        strip.show()
        time.sleep(3)




CONV_4G = 4295.0 # 4096 or 4295
CONV_60_SHARE = CONV_4G / 60.0 # 4096 / 60 = 68.27 or 4295 / 60 = 71.58
def value_split(s):
  r = s.split('=')
  if len(r) == 2: return r
  return r[0], ''

def response_split(s):
  try:
    r = s.split(',')
    title = r[0]
    d = dict(map(value_split, r[1:]))
    return title, d
  except ValueError:
    print s

# https://github.com/ckolivas/cgminer/blob/master/API-README
def cg_rpc(host, port, command):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(command)
    time.sleep(0.02)
    data = s.recv(8192)
    s.close()
  except Exception as e:
    print str(e)
    data = ''
  if data:
    d = data.strip('\x00|').split('|')
    return map(response_split, d)
  return None

def parse_time(t):
  r = []
  m = t // 60
  if t >= 86400:
    r.append('%d day' % (t // 86400))
    t = t % 86400
  r.append('%02d:%02d:%02d / %d min' % (t // 3600, (t % 3600) // 60, t % 60, m))
  return ' '.join(r)

def lucky(p, base):
  if p == 0.0: p = 0.00001
  return 1.0 - math.exp(-p / float(base)), float(base) / p

def parse_summary(r):
  global FOUND
  if not (isinstance(r, (list, tuple)) and len(r) == 2):
    return
  try:
    if not r[0][0] == 'STATUS=S' and r[1][0] == 'SUMMARY':
      return
    d = r[1][1]
    FOUND = int(d['Found Blocks'])
    print 'Miner Status'
    print '  Uptime %s (Net Blocks %s)' % (parse_time(int(d['Elapsed'])), d['Network Blocks'])
    print '  Local / Work / Remote Speed: %.2f / %.2f / %.2f MHash/s' % (float(d['MHS av']), float(d['Work Utility']) * CONV_60_SHARE, float(d['Difficulty Accepted']) / int(d['Elapsed']) * CONV_4G)
    print '  Get / Remote Failures / HW Errors: %s / %s / %s' % (d['Get Failures'], \
              d['Remote Failures'], d['Hardware Errors'])
    print '  Getwork / Local Work / Discarded: %s / %s / %s' % (d['Getworks'], d['Local Work'], d['Discarded'])
    total = float(d['Difficulty Stale']) + float(d['Difficulty Rejected']) + float(d['Difficulty Accepted'])
    if total > 0:
      print '  Accepted / Rejected / Stale: %.2f (%s) / %.2f (%s) / %.2f (%s)' % (\
                     100. * float(d['Difficulty Accepted']) / total, d['Accepted'], \
                     100. * float(d['Difficulty Rejected']) / total, d['Rejected'], \
                     100. * float(d['Difficulty Stale']) / total, d['Stale'])
      print '  PPS Luck: %.2f %%' % (6000. * float(d['Difficulty Accepted']) / (float(d['Work Utility']) * int(d['Elapsed']))) # 4096 MH is 1 share, 100%*4096
      print '  Best Share / D1A: %s / %.2f (%s Blocks Found)' % (d['Best Share'], float(d['Difficulty Accepted']), d['Found Blocks'])
    else:
      print '  No Submited Shares Currently'
  except Exception as e:
    print str(e)

def get_lastshare(d, remote_time):
  last_share_time = remote_time - int(d['Last Share Time']) 
  return last_share_time

def get_lastshare_str(d, remote_time):
  last_share_time = get_lastshare(d, remote_time)
  if last_share_time >= 7200:
    last_share = 'None'
  else:
    last_share = '%d s ago' % (last_share_time)
  return last_share

def parse_pools(r):
  if not isinstance(r, (list, tuple)):
    return
  try:
    if not r[0][0] == 'STATUS=S':
      return
    remote_time = int(r[0][1]['When'])
    for rp in r[1:]:
      if rp[0][0:4] != 'POOL': continue
      d = rp[1]
#      print d
      pool_type = 'Getwork'
      if d.get('Has Stratum', None) == 'true':
        pool_type = 'Stratum'
        if d.get('Stratum Active') == 'true':
          pool_type += ' (Activated)'
      elif d.get('Has GBT', None) == 'true':
        pool_type = 'GBT'
      elif d.get('Long Poll', None) == 'Y':
        pool_type = 'Getwork (LP)'

      last_share = get_lastshare_str(d, remote_time)      
      if d['URL'].startswith('stratum+tcp://'): d['URL'] = d['URL'][14:]
      if d['URL'].startswith('http://'): d['URL'] = d['URL'][7:]
      d['URL'] = d['URL'].rstrip('/')

      print 'Pool (%s) %s (%s), Prio %s, %s' % (d['Status'], d['URL'], d['User'], d['Priority'], pool_type)
      print '  Last share %s, Diff %.2f' % (last_share, float(d['Last Share Difficulty']))
      print '  Get / Remote Failures: %s / %s' % (d['Get Failures'], \
              d['Remote Failures'])
      print '  Getwork / Discarded: %s / %s' % (d['Getworks'], d['Discarded'])
      total = float(d['Difficulty Stale']) + float(d['Difficulty Rejected']) + float(d['Difficulty Accepted'])
      if total > 0:
        print '  Accepted / Rejected / Stale: %.2f (%s, D1A %.2f, Best Share %s) / %.2f (%s) / %.2f (%s)' % (\
                     100. * float(d['Difficulty Accepted']) / total, d['Accepted'], float(d['Difficulty Accepted']), d.get('Best Share','Unknown'), \
                     100. * float(d['Difficulty Rejected']) / total, d['Rejected'], \
                     100. * float(d['Difficulty Stale']) / total, d['Stale'])
        print '  PPS Luck: %.2f %%' % (float(d['Difficulty Accepted']) / float(d['Diff1 Shares']) * 100.) # 4096 MH is 1 share, 100%*4096
      else:
        print '  No Shares Submitted'
#      print d
  except Exception as e:
    print str(e)

DEVICE_MAPPING = {'AVA': 'Avalon_ASIC', 'ICA': 'Icarus', 'BFL': 'BFL'}
def parse_dev(r):
  if not isinstance(r, (list, tuple)):
    return
  try:
    if not r[0][0] == 'STATUS=S':
      return
    remote_time = int(r[0][1]['When'])
    for rr in r[1:]:
      d = rr[1]
      device_type = 'Unknown'
      status = ''
      temp = d.get('Temperature', '0.00')
      if temp == '0.00': temp = 'Unknown'
      if rr[0].startswith('PGA') or rr[0].startswith('ASC'):
        device_type = DEVICE_MAPPING.get(d.get('Name', ''), 'Unknown FPGA')
        freq = d.get('Frequency', '0.00')
        if freq == '0.00':
          freq = d.get('frequency', 'Unknown')
        status = 'Freq %s, Temp %s C' % (freq, temp)

      if rr[0].startswith('GPU'):
        device_type = 'GPU'
        status = 'GPU %s Mem %s @ %s V, Temp %s C' % (d.get('GPU Clock','Unknown'), d.get('Memory Clock','Unknown'), d.get('GPU Voltage', 'Unknown'), temp)
        if d.get('Fan Speed', '-1') != '-1':
          status += ', Fan %s RPM (%s %%)' % (d['Fan Speed'], d.get('Fan Percent', 'Unknown'))
        elif d.get('Fan Percent', '-1') != -1:
          status += ', Fan %s %%' % (d['Fan Percent'])
        status += ', I: %s, Load %s %%' % (d.get('Intensity', 'Unknown'), d.get('GPU Activity', 'Unknown'))
        if d.get('Powertune', '0') != '0': status += ', PowerTune'

      last_share = get_lastshare(d, remote_time)
      enabled = d.get('Enabled', 'N')
      enabled_str = '*Disabled* ' if enabled != 'Y' else ''
      print '%s %sStatus: %s' % (device_type, enabled_str, d['Status'])
      if status:
        print '  ' + status
      if float(d['MHS 5s']) == 0.0 and enabled:
        print '  *Warning*: Dead Device?'
      print '  5s / Avg Speed: %.2f / %.2f MHash/s' % (float(d['MHS 5s']), float(d['MHS av']))
      est_shareavg = float(d['Last Share Difficulty']) / (float(d['MHS av']) + 0.00001) * CONV_4G
      print '  Total D1W %s, Last share %s, Diff %.2f (Est %.2f sec per share)' % (d['Diff1 Work'], get_lastshare_str(d, remote_time), float(d['Last Share Difficulty']), est_shareavg)
      if int(d['Hardware Errors']) > 0:
        print '  HW Error: %s (%.2f %%)' % (d['Hardware Errors'], 100. * int(d['Hardware Errors']) / (int(d['Hardware Errors']) + int(d['Diff1 Work'])))
      else:
        print '  HW Error: None'
      print '  PPS Luck: %.2f %%' % (float(d['Difficulty Accepted']) / float(d['Diff1 Work']) * 100.)
  except Exception as e:
    print str(e)

def parse_notify(r):
  if not isinstance(r, (list, tuple)):
    return
  try:
    if not r[0][0] == 'STATUS=S':
      return
    remote_time = int(r[0][1]['When'])
    notification_count = 0
    print 'Notices'
    for rr in r[1:]:
      d = rr[1]
      if d['Last Not Well'] == '0': continue
      notification_count += 1
      print '  Problem Device %s / %s: %s (%d sec ago)' % (d['ID'], d['Name'], d['Reason Not Well'], remote_time - int(d['Last Not Well']))
    if notification_count == 0:
      print '  All devices running fine.'
  except Exception as e:
    print str(e)

def parse_coin(r):
  if not isinstance(r, (list, tuple)):
    return
  try:
    global BLOCK
    if not r[0][0] == 'STATUS=S':
      return
    if not r[1][0] == 'COIN':
      return
    remote_time = int(r[0][1]['When'])
    d = r[1][1]
    BLOCK = (d['Current Block Hash'][8:64])
    elapsed = int(remote_time - float(d['Current Block Time']))
    luck = lucky(elapsed, 600)
    print 'Block Status'
    print '  Block %s' % (d['Current Block Hash'][8:64])
    print '  Algo %s, Diff %s' % (d['Hash Method'], d['Network Difficulty'])
    print '  Received at %s (%d sec ago, Luck %.2f %%)' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(d['Current Block Time']))), elapsed, luck[0] * 100.0)
  except Exception as e:
    print str(e)

def parse_config(r):
  if not isinstance(r, (list, tuple)):
    return
  try:
    if not r[0][0] == 'STATUS=S':
      return
    if not r[1][0] == 'CONFIG':
      return
    d = r[1][1]
    print 'Devices: %s GPU, %s FPGA, %s ASIC' % (d.get('GPU Count','0'), d.get('PGA Count','0'),d.get('ASC Count','0'))
    print '%s Pool(s) configured with strategy %s' % (d['Pool Count'], d['Strategy'])
  except Exception as e:
    print str(e)

def parse_pools_list(r):
  if not isinstance(r, (list, tuple)):
    return
  ret = []
  try:
    if not r[0][0] == 'STATUS=S':
      return
    remote_time = int(r[0][1]['When'])
    for rp in r[1:]:
      if rp[0][0:4] != 'POOL': continue
      d = rp[1]
      ret.append((d['URL'].replace('://', '://' + urllib.quote(d['User']) + '@'), int(d['Priority'])))
  except:
    pass
  return ret

def conv_prio_dict(p):
  if isinstance(p, (tuple, list, )):
    try:
      pd = dict(p)
    except TypeError: # not able to convert
      pd = zip(p, range(len(p)))
    return pd
  if isinstance(p, dict):
    return p
  return {}

def escape_api(s):
  return s.replace('\\', '\\\\').replace(',', '\\,')

# Note: p2 should have pass
def matching_pools(p1, p2=None):
  p1 = conv_prio_dict(p1)
  p2 = conv_prio_dict(p2)
  p1_s = sorted(p1, key=p1.get)
  # if d['URL'].startswith('stratum+tcp://'): d['URL'] = d['URL'][14:]
  # if d['URL'].startswith('http://'): d['URL'] = d['URL'][7:]

oldblock = '0'

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2: raise Exception('Usage: python %s IP [PORT]' % sys.argv[0])
  host = str(sys.argv[1]).strip()
  port = 4028
  if len(sys.argv) == 3:
    port = int(sys.argv[2])
   # Create NeoPixel object with appropriate configuration.
  strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        # Intialize the library (must be called once before other functions).
  strip.begin()

  while True:
	s = cg_rpc(host, port, 'config')
  	parse_config(s)
  	s = cg_rpc(host, port, 'summary')
  	parse_summary(s)
  	s = cg_rpc(host, port, 'coin')
  	parse_coin(s)
  	s = cg_rpc(host, port, 'notify')
  	parse_notify(s)
  	s = cg_rpc(host, port, 'pools')
  	matching_pools(parse_pools_list(s))
  	parse_pools(s)
  	s = cg_rpc(host, port, 'devs')
  	parse_dev(s)
	
        block = BLOCK[1:]
	print BLOCK
	print FOUND
        dispBlock(strip, block)
	if (block!=oldblock):
		oldblock = block
        	if(FOUND>0):
        		winner(strip)
		elif(FOUND ==0):
			loser(strip)
	time.sleep(1)
  #print s
  # TODO: config, devdetails, stats
