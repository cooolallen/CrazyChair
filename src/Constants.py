IMG_DIR = '../images'
DATA_DIR = '../data'			
test = False			
normalize = False			
updateRate = 150					# update rate in ms
consecutiveFactor = 5				# when predict is more than consecutiveFactor, we set the real prediction as curr_prediction
goodPosture = {0, 1, 2}				# the value of the normal posture
<<<<<<< HEAD
alarmParams = {'phone':150, 'pop_up': 100, 'vibrate': 3}		# the peroid of each notification (unit: timestamp)
=======
alarmParams = {'phone':150, 'pop_up': 100, 'vibrate': 10}		# the peroid of each notification (unit: timestamp)
>>>>>>> 265d5b25486d0c4b59af3494a61666dcd88439c1


# constants related to email
defaultParas = {}
defaultParas['password'] = 'zerodudepublic'
defaultParas['sender'] = 'publicdudezero@gmail.com'
defaultParas['destination'] = 'swimm1rsu@gmail.com'
defaultParas['subject'] = 'Posture alarm'
