import simpy
import random
import statistics as stats
from time import sleep

delivery_times = []

branches = {1 : 'North Delhi (Zone 1)', 2 : 'South Delhi (Zone 2)', 3 : 'East Delhi (Zone 3)', 4 : 'West Delhi (Zone 4)', 5 : 'Central Delhi (Zone 5)'}
price = [100.00, 150.00, 200.00]

class restaurant(object):									#defining the restaurant environment
	def __init__(self, env, chef_no, del_exec_no, small, med, large):
		self.env = env
		self.chef = simpy.Resource(env, chef_no)
		self.del_exec = simpy.Resource(env, del_exec_no)
		self.small = small
		self.med = med
		self.large = large

	def prepare_dish(self, customer, small, med, large):
		c = small + med + large
		if c > 5:
			yield self.env.timeout(random.uniform(25,30))
		elif c in range(2,6):
			yield self.env.timeout(random.uniform(15,20))
		else:
			if small != 0:
				yield self.env.timeout(10)
			elif med != 0:
				yield self.env.timeout(15)
			else:
				yield self.env.timeout(17)	

	def hygiene(self):
		yield self.env.timeout(random.uniform(1,2))		#time to comply with covid precautions

	def deliver_order(self, customer, n):
		if n == 1 or n == 3 or n == 4:
			yield self.env.timeout(random.uniform(10,15))	
		
		else:
			yield self.env.timeout(random.uniform(15,20))

def new_order(env, customer, restro, n, small, med, large):
	order_time = env.now 								#time of order placement

	with restro.chef.request() as request:
		yield request
		yield env.process(restro.prepare_dish(customer, small, med, large))

	with restro.del_exec.request() as request:
		yield request
		yield env.process(restro.deliver_order(customer,n))

	del_time = env.now - order_time
	delivery_times.append(del_time)
	
def run_restaurant(env, chef_no, del_exec_no, n, small, med, large):
	restro = restaurant(env, chef_no, del_exec_no, small, med, large)		#creating object of restaurant class
	customer = 0
	
	while True:
		yield env.timeout(5)							#new order every 5 mins
		customer += 1
		env.process(new_order(env, customer, restro, n, small, med, large))

def calc_time(delivery_times):
	avg_time = stats.mean(delivery_times)
	mins, frac_mins = divmod(avg_time, 1)
	secs = frac_mins*60
	return round(mins), round(secs)

def manager_input():
	chef_no = random.randint(10,15)
	del_exec_no = random.randint(5,10)

	attributes = [chef_no, del_exec_no]

	if all(str(i).isdigit() for i in attributes):
		attributes = [int(x) for x in attributes]
		return attributes
	else:
		print("Invalid input!")

def order_details(small, med, large):
	qty = [small, med, large]
	size_names = ['Small pizza', 'Medium pizza', 'Large pizza']
	total = 0
	for i in range(3):
		if qty[i] != 0:
			print(size_names[i], '\t ', qty[i], '\t   ', qty[i]*price[i])
			total += qty[i]*price[i]

	print('----------------------------------')
	print('Total payable = Rs.', total)
	print('----------------------------------')
	
def main():												#the main fn for execution
	random.seed(42)
	'''
	words = ["Name", "Hours Worked", "Hourly Rate", "Taxes Owed", "Net Pay"]
	words = ["\u0332".join(word+' ')[:-1] for word in words]
	print('{:<20} {:^5} {:>6} {:>10} {:>10}'.format(*words))
	'''
	print('\t\t\t\t\t\t\t\t\t\t\t   -------------------------------------')
	print('\t\t\t\t\t\t\t\t\t\t\t\tSK Pizza Delivery Management Server')
	print('\t\t\t\t\t\t\t\t\t\t\t   -------------------------------------')
	print('Enter your name : ', end = '')
	Name = input()
	print('Welcome', Name, '!')

	while True:
		print('\nMain Menu : ')
		print('-----------')
		print('1. Place new order \n2. Exit\n')
		choice = int(input('Choose from above : '))

	#switch
		if choice == 1:
			print('\nOur registered branches : ')
			print('-------------------------')
			for i in range(5):
				print('-> Branch', i+1,':', branches[i+1])

			print('\nEnter delivery zone : ', end = '')
			zone = int(input())
			
			if zone not in range(1,6):
				print('Invalid command! Aborting program...')
				print('Try again.')
				sleep(1)
				continue
			
			print('Order will be safely delivered from', branches[zone], 'branch.')

			print('\nEnter quantity for each :')
			print('-> Small pizza : ', end = '')
			small = int(input())
			
			print('-> Medium pizza : ', end = '')
			med = int(input())
			
			print('-> Large pizza : ', end = '')
			large = int(input())

			print('\nEnter delivery address : ', end = '')
			address = input()

			chef_no, del_exec_no = manager_input()

			env = simpy.Environment()

			print('\nOrder #', end = '')
			print(random.randint(10000,20000), ':')
			print('\tItem \t\t Qty \t\tPrice')
			print('----------------------------------')
			order_details(small, med, large)
			print('\nDeliver to :', Name, ',', address)
			print('------------')
			
			print('\nEstimating delivery time...')
			sleep(2)
			env.process(run_restaurant(env, chef_no, del_exec_no, zone, small, med, large))
			env.run(until = 60)

			mins, secs = calc_time(delivery_times)
			print("\nYour order is arriving in around {} minutes and {} seconds.".format(mins, secs))
			print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t-x-x-x-')
			delivery_times.clear()

		elif choice == 2:
			print('\nThank you for ordering from us.')
			print('Looking forward to serving you delicious pizzas in the future as well :)')
			break
		
		else:
			print('Invalid command! Aborting program...')
			print('Try again.')
			sleep(1)

if __name__ == '__main__':
	main()