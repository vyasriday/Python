class AirFlight:
	
	def TicketNumber(self):
		return 'SNB0211J'


	def SeatNumber(self):
		return len(str("SNB0211J"))

# THIS IS HOW WE CREATE OBJECTS IN PYTHON

obj = AirFlight()

print("Ticket Number is ",obj.TicketNumber())
print("Seat Number is ",obj.SeatNumber())


class SelfInitializer:
	def getTicket(self,number):
		self._number = number

	def number(self):
		return self._number

f = SelfInitializer("ABC112")

print(f._number)
