import time
# import cv2
# import os
# import re
# import subprocess
# from threading import Thread

nanoseconds_per_second = 1e9

def fmt_to_stmp(tm,*arg):
    fmt= "%Y-%m-%d %H:%M:%S" if not arg else arg[0]
    timeArray = time.strptime(tm, fmt)
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

def stmp_to_fmt(time_stamp):
#     timeStamp=1631343812
    time_array = time.localtime(time_stamp)
    time_fmt = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return time_fmt

# def mp4_to_png(dir, video_name, imgname_interval=1, frame_step=1):
#     img_name = re.findall('[0-9]+',video_name.split('.')[0]) # substract time in string of number
#     folder_name = "".join(img_name) 
#     # img_name = '20210910152124'
#     if not img_name: # verify video name
#         print('video name shall contains number, quit...')

#     img_name = fmt_to_stmp(folder_name,'%Y%m%d%H%M%S') #convert to time stamp format
#     start_time=img_name
#     print('folder name: ', folder_name)
# #     print('image name:',img_name)
#     if not os.path.isdir(dir+folder_name):
#         os.mkdir(dir+folder_name)

#     vc = cv2.VideoCapture(dir+video_name)
#     is_opened= vc.isOpened
#     width = int (vc.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height =int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fps=vc.get(cv2.CAP_PROP_FPS)
#     print('original image size, fps: ', width, 'x',height,',', fps) 
#     i=0
#     while is_opened:
#         is_opened, img = vc.read()
#         if is_opened:
#             file_name= str(img_name)+'.png'             
#     #         print(img_name)            
#             if i%frame_step==0:
#                 cv2.imwrite(dir+folder_name+'/'+file_name,img,\
#                         [cv2.IMWRITE_PNG_COMPRESSION,9]) # 0 -9 : best to worst
#                 img_name+= imgname_interval
#             i+=1
#         else:
#             is_opend= False  # if false , then break the while loop
#         end_time=img_name- imgname_interval
#         count = int((i-1)/frame_step) +1
#     vc.release()
#     print('Save success!, total ', count ,'images')
#     return start_time, end_time

# class SurfaceFlingerFPS():
	
# 	def __init__(self, view, ip):
# 		try:
# 			self.view = view
# 			self.ip = ip
# 			self.refresh_period, self.base_timestamp, self.timestamps = self.__init_frame_data__(self.view)
# 			self.recent_timestamps = self.timestamps[-2]
# 			self.fps = 0
# 		except Exception:
# 			self.fps=0
			
# 	def __init_frame_data__(self, view):
# 		try:
# 			out = subprocess.check_output(['adb', '-s', self.ip, 'shell', 'dumpsys', 'SurfaceFlinger', '--latency-clear', view])
# 			out = out.decode('utf-8')
# 			if out.strip() != '':
# 				raise RuntimeError("Not supported.")
# 				time.sleep(0.1)
# 			(refresh_period, timestamps) = self.__frame_data__(view)
# 			base_timestamp = 0
# 			base_index = 0
# 			for timestamp in timestamps:
# 				if timestamp != 0:
# 					base_timestamp = timestamp
# 					break
# 				base_index += 1
# 	# 		if base_timestamp == 0:
# 	# 			raise RuntimeError("Initial frame collect failed")
# 			return (refresh_period, base_timestamp, timestamps[base_index:])
# 		except Exception:
# 			self.fps=0

# 	def __frame_data__(self, view):
# 		try:
# 			out = subprocess.check_output(['adb', '-s', self.ip, 'shell', 'dumpsys', 'SurfaceFlinger', '--latency', view])
# 			out = out.decode('utf-8')
# 			results = out.splitlines()
# 			refresh_period = int(results[0]) / nanoseconds_per_second
# 			timestamps = []
# 			for line in results[1:]:
# 				fields = line.split()
# 				if len(fields) != 3:
# 					continue
# 				(start, submitting, submitted) = map(int, fields)
# 				if submitting == 0:
# 					continue

# 				timestamp = submitting/nanoseconds_per_second
# 				timestamps.append(timestamp)
# 			return (refresh_period, timestamps)
# 		except Exception:
# 			self.fps=0
			
# 	def collect_frame_data(self,view):
# 		try:
# 			if view is None:
# 				self.fps =0 # roy add
# 	# 			raise RuntimeError("Fail to get current SurfaceFlinger view") #roy hide

# 			#refresh_period, base_timestamp, timestamps = self.__init_frame_data__(view)
# 			#while True:

# 			self.refresh_period, self.timestamps = self.__frame_data__(view)
# 			#print(self.timestamps)
# 			time.sleep(1)
# 			self.refresh_period, tss = self.__frame_data__(view)
# 			#print(tss)
# 			self.last_index = 0
# 			#print(tss)
# 			if self.timestamps:
# 					self.recent_timestamp = self.timestamps[-2]
# 					self.last_index = tss.index(self.recent_timestamp)
# 			self.timestamps = self.timestamps[:-2] + tss[self.last_index:]
# 			#time.sleep(1)

# 			ajusted_timestamps = []
# 			for seconds in self.timestamps[:]:
# 					seconds -= self.base_timestamp
# 					if seconds > 1e6: # too large, just ignore
# 						continue
# 					ajusted_timestamps.append(seconds)

# 			from_time = ajusted_timestamps[-1] - 1.0
# 			fps_count = 0
# 			for seconds in ajusted_timestamps:
# 					if seconds > from_time:
# 						fps_count += 1
# 			self.fps = fps_count                        
# 		except Exception:
# 			self.fps=0


# 	def start(self):
# 		th = Thread(target=self.collect_frame_data, args=(self.view,))
# 		th.start()
	
# 	def getFPS(self):
# 		self.collect_frame_data(self.view)
# 		return self.fps

