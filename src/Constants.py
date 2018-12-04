IMG_DIR = '../images'
DATA_DIR = '../data'			
test = True			
normalize = False			
updateRate = 300					# update rate in ms
consecutiveFactor = 5				# when predict is more than consecutiveFactor, we set the real prediction as curr_prediction
goodPosture = {}				# the value of the normal posture
alarmParams = {'phone':150, 'pop_up': 100, 'vibrate': 3}		# the peroid of each notification (unit: timestamp)


# constants related to email
defaultParas = {}
defaultParas['password'] = 'zerodudepublic'
defaultParas['sender'] = 'publicdudezero@gmail.com'
defaultParas['destination'] = 'swimm1rsu@gmail.com'
defaultParas['subject'] = 'Posture alarm'
