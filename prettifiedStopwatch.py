#! python3
# prettifiedStopwatch.py - pretty stopwatch
# that will save output to clipboard.

import pyperclip, time

# Display the program's instructions.
print('Press ENTER to begin. Then, press ENTER to click the stopwatch. Press CTRL-C to quit.')
input()								# Press ENTER to begin.
print('Started.')
startTime = time.time()				# Get the first lap's start time.
lastTime = startTime
lapNum = 1

lapTimes = []

# Start tracking the lap times.
try:
	while True:
	
		# Record input.
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		
		# Format lap.
		lap = 'Lap # %s: ' % lapNum
		ttime = str(totalTime).rjust(7)
		ttimeSep = ' ('
		ltime = str(lapTime).rjust(7)
		ltimeSep = ')'
		formatted = lap + ttime + ttimeSep + ltime + ltimeSep
		
		print(formatted, end='')
		lapNum += 1
		lastTime = time.time()		# Reset the last lap time.
		lapTimes.append(formatted)	# Add to list of saved laps.
		
except KeyboardInterrupt:
	# Handle the CTRL-C exception to keep its error missage from displaying.
	print('\nDone.')
	
	# Copy to pyperclip.
	pyperclip.copy('\n'.join(lapTimes))