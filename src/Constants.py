IMG_DIR = '../images'
DATA_DIR = '../data'			
test = False						
updateRate = 150					# update rate in ms
consecutiveFactor = 5				# when predict is more than consecutiveFactor, we set the real prediction as curr_prediction
goodPosture = {0, 1, 2}				# the value of the normal posture
alarmParams = {'phone':1000, 'pop_out': 100, 'vibrate': 10}		# the peroid of each notification (unit: timestamp)


# constants related to email
defaultParas = {}
defaultParas['password'] = 'zerodudepublic'
defaultParas['sender'] = 'publicdudezero@gmail.com'
defaultParas['destination'] = 'swimm1rsu@gmail.com'
defaultParas['subject'] = 'Posture alarm'
