import numpy as np
# Example sales and expenses data for 12 months
sales_data = np.array([10000, 12000, 13000, 11000, 12500, 15000, 16000, 14500, 13500, 14000, 15500, 17000])
expenses_data = np.array([5000, 6000, 7000, 6500, 6800, 7500, 8000, 7700, 7100, 7300, 7900, 8200])
profit_data=sales_data-expenses_data
print(profit_data)
mean_sales=np.mean(sales_data)
mean_expenses=np.mean(expenses_data)
mean_profit=np.mean(profit_data)
print(f"mean of sales data: {mean_sales}")
print(f"mean of expenses data: {mean_expenses}")
print(f"mean of profit data: {mean_profit}")
median_sales=np.median(sales_data)
median_expenses=np.median(expenses_data)
median_profit=np.median(profit_data)
print(f"median of sales data: {median_sales}")
print(f"median of expenses data: {median_expenses}")
print(f"median of profit data: {median_profit}")
sd_sales=np.std(sales_data)
sd_expenses=np.std(expenses_data)
sd_profit=np.std(profit_data)
print(f"standard deviation of sales data: {sd_sales}")
print(f"standard deviation  of expenses data: {sd_expenses}")
print(f"standard deviation of profit data: {sd_profit}")
#to find max profit in which month
max_p=np.max(profit_data)
max_profit=np.argmax(profit_data)+1
print(f"the max profit of the year is in {max_profit} month of profit {max_p}")
#to find min sales in which month
min_s=np.min(sales_data)
min_sales=np.argmin(sales_data)+1
print(f"the minimum sale of the year is in {min_sales} month of sale {min_s}")




