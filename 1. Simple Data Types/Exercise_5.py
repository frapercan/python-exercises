# Write a program that asks the user for the number of hours worked and the cost per hour.
# It should then display on the screen the corresponding pay.
hours_worked= int(input('how many hours have you worked?'))
cost_per_hour=int(input('how much cost the hours?'))
print(f'{hours_worked*cost_per_hour}$')
